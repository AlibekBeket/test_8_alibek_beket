from django.urls import path

from feedback.views.product import ProductListView, ProductDetailView, ProductAddView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('product/', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductAddView.as_view(), name='product_add'),
]
