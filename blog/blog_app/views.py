from django.shortcuts import render
from django.views.generic import (ListView ,DeleteView ,
                                    TemplateView ,CreateView ,
                                    UpdateView ,UpdateView ,DeleteView)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from blog_app.models import *
from blog_app.forms import *

# Create your views here.

class AboutView(TemplateView):
    template_name ='About.html'

class PostListView(ListView):
    model =Post
    template_name = 'post_list.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now).order_by('-published_date')

class PostDetails(DeleteView):
    model = Post
    template_name ='post_details.html'

class createPostview(LoginRequiredMixin , CreateView):
    login_url = '/login'
    model =Post
    form_class = PostForm
    template_name ='post_create.html'
class UpdatePostview(LoginRequiredMixin , UpdateView):
    login_url = '/login'
    model =Post
    form_class = PostForm
    
class POstDeleteView(LoginRequiredMixin , DeleteView):
    model =Post
    success_url = reverse_lazy('post_list')
class DraftListView(LoginRequiredMixin ,ListView):
    login_url ='/login'
    model =Post
    def get_queryset(self):
        return Post.objects.order_by('create_date')
