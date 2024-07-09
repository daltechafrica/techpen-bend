from django.urls import path
# from .views import views getarticles, getsinglearticle, createBlog, updateBlog, deleteBlog,

from . import views


urlpatterns = [
    path('', views.getarticles, name='articles'),

    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('article/<str:pk>/', views.getsinglearticle, name='article'),
    path('add/', views.createBlog, name='create-blog' ),
    path('update/<str:pk>/', views.updateBlog, name='update' ), 
    path('delete/<str:pk>/', views.deleteBlog, name='delete' ), 
]