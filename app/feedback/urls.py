from django.urls import path

from feedback.views.product import ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('product/', ProductListView.as_view(), name='products_list'),
]
