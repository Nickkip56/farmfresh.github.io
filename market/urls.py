from django.urls import path
from market.views import CategoryDetailView
from . import views



urlpatterns = [
    path('', views.home , name="home"),
    path('market/', views.market),
    path('products/', views.products),
    path('products/', CategoryDetailView, name="category-detail"),
    path('category/<str:cats>/', CategoryDetailView, name="category-detail"),
]
