from django.shortcuts import render, redirect

# - authentications model and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Blog
from .forms import BlogForm, ReviewForm, CreateUserForm, LogUserForm


def get_user( user):
    verified_user = user
    return verified_user


def user_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'blogs/register.html', context)


def user_login(request):
    form = LogUserForm()
    if request.method == 'POST':
        form = LogUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                get_user(user)
                auth.login(request, user)
                return redirect('articles')
    context = {'form': form}
    return render(request, 'blogs/login.html', context)


def user_logout(request):
    auth.logout(request)

    return redirect('login')


@login_required(login_url='login')
def getarticles(request):
    allblogs = Blog.objects.all()
    context = {'articles': allblogs}
    return render(request, 'blogs/articles.html', context)


# a function that fetches a single article and all its reviews and tags, and if a new revie is made,
#  it is posted into the database

def getsinglearticle(request, pk):
    article = Blog.objects.get(id=pk)   # fetches a particular blod whose id is pk.
    tags = article.tags.all()           # fetches all tags from the database
    reviews = article.review_set.all()  # fetches all reviews from the database
    new_review = None   # Review posted
    if request.method == 'POST':
        reviewForm = ReviewForm(data=request.POST)
        if reviewForm.is_valid():
            new_review = reviewForm.save(commit=False)  # create review bt don't save to database yet.
            new_review.blog = article   # assign the current article to the review
            new_review.save()   #save the review to the database.
            reviewForm = ReviewForm()
    else: # if request.method == 'GET'
        reviewForm = ReviewForm()

    context = {'article': article, 'tags': tags, 'reviews': reviews, 'review_form': reviewForm }
    return render(request, 'blogs/single-article.html', context)


def createBlog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
    context = {'form': form}
    return render(request, 'blogs/blog-form.html', context) 


def updateBlog(request,pk):
    template = 'blogs/blog-form.html'
    context = {}
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('articles')
    context['form'] = form
    return render(request, template, context)


def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('articles')
    return render(request, 'blogs/delete.html', {'object': blog})


