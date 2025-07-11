from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
    path('products/<int:pk>/update/', ProductUpdateDeleteView.as_view()),
    path('products/<int:product_id>/reviews/', ReviewListView.as_view()),
    path('reviews/create/', ReviewCreateView.as_view()),
]
