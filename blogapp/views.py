from django.shortcuts import render, get_object_or_404 , redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋

    #블로그 객체 세 개를 한 페이지로 자르기
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    
    #request된 페이지를 알아내서 변수에 담고 
    page = request.GET.get('page')

    #얻어온 뒤 return
    posts = paginator.get_page(page)

    return render(request, 'home.html' , {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog() #클래스 안에 = 객체()
    blog.title = request.GET['title'] #blog.title이라는 변수 안에 넣어줌
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #.delete도 있음
    return redirect('/blog/'+str(blog.id))


