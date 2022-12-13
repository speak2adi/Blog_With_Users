from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostDb, CommentDb
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm


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

    # getting context for comment and comment form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentDb.objects.filter(post=self.object)
        context['form'] = CommentForm()
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = CommentDb
    form_class = CommentForm
    template_name = 'blog/post_detail.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs['pk']

        return super().form_valid(form)


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
