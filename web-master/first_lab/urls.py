from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('test', views.test),
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('contact-form/', contact_form, name='contact_form'),
    path('blogs/', BlogListView, name='blogs'),
    path('lst1', LocalStorage1, name='local_storage1'),
    path('lst2', LocalStorage2, name='local_storage2'),
    path('blog/<int:_id>', BlogDetailView, name='blog'),
]
