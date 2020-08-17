# instead an http response we can return a rendered template
from django.shortcuts import render, get_object_or_404
# will require to log in in order to create a new post under 127.0.0:8000/post/mew
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User # will work with the User to show all User posts in UserPostListView
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# a view function that handles the logic from the homepage
# will need an url that corresponds/maps the url path to that view function
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # the render function still returns an HttpResponse in the background
    # views have to return either an HttpResponse or an exception
    return render(request, 'blog/home.html', context)

# should replace the home function and add visual functionalyty to the home url
# this are class based views thats why we imported this class and inherit it here
# by defaul the ListView calls the objects objectlist not "posts" as we did inside the home view
#
class PostListView(ListView):
    # which model should our listview query
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

# showing only post from a certain user after clickin the users name
class UserPostListView(ListView):
    # which model should our listview query
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted'] # will be overriden by the get_query_set method
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) # will get the users name
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # LoginRequiredMixin
    # we need to override the method and enabling posting by setting the author
    def form_valid(self, form):
        # take the instance of the form and take its author and change it to the user who is creating the post
        form.instance.author = self.request.user
        # running the form_valid method on the parent class
        # befor the return statement is run we change or set the author
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # UserPassesTestMixin
    # needs to return true to modify the post, user has to be the post creator
    def test_func(self):
        post = self.get_object() # get the post
        if self.request.user == post.author: # if the requester is the one who created the post return true otherwise False
            return True
        return False # will result in 403


# this only can delete a post if the user is logged in mixin and user is the creater of the post mixin
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # after deletion django will redirect us to the homepage

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title':'Cool Bro'})
