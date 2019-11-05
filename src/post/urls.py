from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="post-index"),
    path('about/', views.about, name="post-about"),
    path('blog/', views.blog, name="post-blog"),
    path('work/', views.work, name="post-work"),
    path('contact/', views.contact, name="post-contact"),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

]