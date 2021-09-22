  
from django.shortcuts import render , redirect

# Create your views here.


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/')

    
def home(request):
  return render(request, 'index.html');

def blog(request):
  return render(request, 'blog.html');


def login_view(request):
    return render(request , 'login.html')

def  register_view(request):
    return render(request , 'register.html')



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
            return redirect('/add-blog/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_blog.html' , context)
