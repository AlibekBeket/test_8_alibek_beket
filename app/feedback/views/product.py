from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from feedback.models import Product, Review

from feedback.forms import ProductForm


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        products = Product.objects.all()
        for product in products:
            reviews = Review.objects.filter(product=product)
            count_review = 0
            total_review = 0
            for review in reviews:
                count_review += 1
                total_review += review.grade
            if count_review == 0:
                product.avg = 0
            else:
                product.avg = total_review / count_review
        context = super().get_context_data(object_list=products, **kwargs)
        context['user'] = self.request.user
        return context


class ProductDetailView(ListView):
    template_name = 'product_detail.html'
    model = Review
    context_object_name = 'reviews'
    paginate_by = 5
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['product'] = get_object_or_404(Product, pk=self.kwargs['pk'])
        count_review = 0
        total_review = 0
        for review in Review.objects.filter(product=get_object_or_404(Product, pk=self.kwargs['pk'])):
            count_review += 1
            total_review += review.grade
        if count_review == 0:
            context['avg'] = 0
        else:
            context['avg'] = total_review / count_review
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(product=get_object_or_404(Product, pk=self.kwargs['pk']))
        return queryset


class ProductAddView(CreateView):
    template_name = 'product_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = 'product_update.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    model = Product
    success_url = reverse_lazy('products_list')
