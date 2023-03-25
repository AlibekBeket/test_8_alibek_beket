from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

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
