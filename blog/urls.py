from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),   
    path('post/about/', views.post_about, name='post_about'),
    path('post/quality',views.post_quality, name='post_quality'),
    path('post/home',views.post_home, name='post_home'),
    path('post/portfolio',views.post_portfolio, name='post_portfolio')

    
]