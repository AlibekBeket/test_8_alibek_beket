from django.views.generic import ListView

from feedback.models import Product


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'
