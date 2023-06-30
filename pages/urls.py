from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:page_id>/comments/create/', views.comments_create, name='comments_create'),
]
