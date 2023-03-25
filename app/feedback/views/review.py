from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView

from feedback.models import Product, Review

from feedback.forms import ReviewForm


class ReviewAddView(CreateView):
    template_name = 'review_add.html'
    model = Review
    form_class = ReviewForm

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
