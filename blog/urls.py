#all blug url paths
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
urlpatterns = [
    #parameters (empty path, function that returns response, names help to reference from html in templates)
    path('', PostListView.as_view(), name='blog-home'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #goes to the post with the primary key indicated, pk = "primary key"
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')   
]
