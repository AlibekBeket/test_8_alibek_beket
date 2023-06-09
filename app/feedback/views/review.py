from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from feedback.models import Product, Review

from feedback.forms import ReviewForm


class ReviewAddView(LoginRequiredMixin, CreateView):
    template_name = 'review_add.html'
    model = Review
    form_class = ReviewForm
    permission_required = 'feedback.change_review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            author = request.user
            product = Product.objects.get(id=kwargs['pk'])
            review_text = form.cleaned_data.get('review_text')
            grade = form.cleaned_data.get('grade')
            Review.objects.create(author=author, product=product, review_text=review_text, grade=grade)
            return redirect(reverse('product_detail', kwargs={'pk': kwargs['pk']}))
        return render(request, 'review_add.html',
                      context={'form': form, 'pk': kwargs['pk']})


class ReviewUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    template_name = 'review_update.html'
    model = Review
    form_class = ReviewForm
    groups = ['moderator']
    permission_required = 'feedback.change_review'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.kwargs['project_pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['project_pk']
        return context

    def test_func(self):
        return self.request.user.groups.filter(
            name__in=self.groups).exists() or self.request.user == Review.objects.get(id=self.kwargs['pk']).author


class ReviewDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    template_name = 'review_delete.html'
    model = Review
    permission_required = 'feedback.delete_review'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.kwargs['project_pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['project_pk']
        return context

    def test_func(self):
        return self.request.user == Review.objects.get(id=self.kwargs['pk']).author
