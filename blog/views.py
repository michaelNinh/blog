from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    # WHEN USING DETAILVIEW, you can reference the model object by using the lowercase version of the model
    # E.G. reference the passed in Post model as 'post'
    model = Post
    template_name = 'post_detail.html'
