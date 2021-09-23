  
from django.shortcuts import render , redirect
# Create your views here.
from .models import *
from .form import *
from django.contrib.auth import logout
from django.core import paginator
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View

def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
  return render(request, 'index.html');

def blog(request):
  context = {'blogs' : BlogModel.objects.all()}
  return render(request, 'blog.html' , context)


def login_view(request):
    return render(request , 'login.html')

def  register_view(request):
    return render(request , 'register.html')


def blog_detail(request , slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'blog_detail.html' , context)

@login_required()
def add_blog(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
            print(blog_obj)
            return redirect('/addblog/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_blog.html' , context)
