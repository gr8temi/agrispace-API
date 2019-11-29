from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Info.as_view() , name='index'),
    path('categories/',views.CategoryView.as_view(), name='category_view')
]