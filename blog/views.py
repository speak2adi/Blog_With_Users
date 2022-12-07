from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostDb
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class PostListView(ListView):
    model = PostDb
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class PostDetailView(DetailView):
    model = PostDb
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class PostCreationView(LoginRequiredMixin, CreateView):
    model = PostDb
    template_name = 'blog/create_post.html'
    fields = ['title', 'content']

    # overiding the form_valid method to save the author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostDb
    template_name = 'blog/create_post.html'
    fields = ['title', 'content']

    # overiding the form_valid method to save the author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # overiding the test function to check if author is equal to the current user
    def test_func(self):
        # gets the post object
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostDb
    template_name = 'blog/confirm_delete.html'
    success_url = '/'

    def test_func(self):
        # gets the post object
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
