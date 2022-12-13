from django.urls import path
from .views import PostListView, PostDetailView, PostCreationView, PostUpdateView, PostDeleteView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name="home-page"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('create-post/', PostCreationView.as_view(), name="create-post"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="update-post"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="delete-post"),
    path('post/<int:pk>/comment', CommentCreateView.as_view(), name="create-comment"),
]
