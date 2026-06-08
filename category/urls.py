from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, CategoryCreateView

urlpatterns = [
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),        
    path("categories/create/", CategoryCreateView.as_view(), name="category_create"), 
]