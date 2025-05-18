from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class BlogListView(ListView):
  model = Post
  template_name = 'pages/home.html'
  context_object_name = 'all_posts_list'

class BlogDetailView(DetailView):
  model = Post
  template_name = 'pages/post_detail.html'

class BlogCreateView(CreateView):
  model = Post
  template_name = 'pages/post_new.html'
  # fields = ['title', 'author', 'body']
  fields = '__all__'

class BlogUpdateView(UpdateView):
  model = Post
  template_name = 'pages/post_edit.html'
  fields = ['title', 'body']

class BlogDeleteView(DeleteView):
  model = Post
  template_name = 'pages/post_delete.html'
  # after deletion go back to home page
  success_url = reverse_lazy('home')
