from django.urls import path
# imports the viewsn file that contains the view functions (like home()) from the blog (.) directory
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

# mapping of url paths to the view functions
urlpatterns = [
    # we can't use class based views without converting it in an actual view
    # template engine is looking for a html file by the name convention <app>/<model>_<viewtype>
    # this will result in "blog/post_list.html"
    # we could change the directory for where to look but since we already have one we can point the engine to it
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # view.home points to the home() view function that handles the user events on the homepage
    # blog-home is the name for the path that points to the home() view function
    # path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
