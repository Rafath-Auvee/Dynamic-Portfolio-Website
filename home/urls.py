
from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name="home"),
    path('blog/' , blog , name="blog"),
    path('login/' , login_view , name="login_view"),
    path('register/' , register_view , name="register_view"),
    path('add-blog/' , add_blog, name="add_blog"),
    path('logout-view/' , logout_view , name="logout_view"),
]