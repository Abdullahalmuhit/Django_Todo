
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('add_comment/', views.add_comment, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>', views.edit, name='edit'),
    path('update/<id>', views.update, name='update'),
]
