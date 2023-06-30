from django.shortcuts import render, redirect
from .models import Page, Comment
from .forms import PageForm, CommentForm

# Create your views here.

def index(request):
    pages = Page.objects.all()
    context = {
        'pages' : pages,
    }
    return render(request, 'pages/index.html', context)

def detail(request, id):
    page = Page.objects.get(id=id)
    comment_form = CommentForm()
    comments = page.comment_set.all()
    
    context = {
        'page' : page,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'pages/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save()
            return redirect('pages:detail', id=page.id)
    else:
        form = PageForm()
    context = {
        'form' : form,
    }
    return render(request, 'pages/form.html', context)

def comments_create(request, page_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.page_id = page_id
            comment.save()
            return redirect('pages:detail', page_id)

    else:
        return redirect('pages:detail', page_id)
    
