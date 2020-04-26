from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='home'),
    path('blogs/', views.blogs, name = 'blogs'),
    path('contact/', views.contacts, name = 'contacts'),
    path('blogs/<int:blog_id>/', views.detail, name = 'detail'),

]
