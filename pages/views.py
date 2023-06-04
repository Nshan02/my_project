from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts_list'

class DetailPageView(DetailView):
    template_name = 'detail.html'
    model = Post

class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title','author','body',]

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title','body']

class PostDelateView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')