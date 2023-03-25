from django.urls import path

from feedback.views.product import ProductListView, ProductDetailView, ProductAddView, ProductUpdateView, ProductDeleteView

from feedback.views.review import ReviewAddView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('product/', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductAddView.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/review_add/', ReviewAddView.as_view(), name='review_add'),
    path('product/<int:project_pk>/review_update/<int:pk>/', ReviewUpdateView.as_view(), name='review_update'),
    path('product/<int:project_pk>/review_delete/<int:pk>/', ReviewDeleteView.as_view(), name='review_delete'),
]
