from django.views.generic import ListView, DetailView

from feedback.models import Product


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 1


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product
