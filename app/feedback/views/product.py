from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from feedback.models import Product

from feedback.forms import ProductForm


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 1


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product


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
