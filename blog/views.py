from .models import Post, Comment #.models dot means in the same directory, quering all post from database
from django.shortcuts import render, get_object_or_404 #easily renders the templates
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.models import User
from django.contrib import messages #for things like flash message
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CommentForm



#all functions take a request
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model?_<viewtype>.html <------------- template with this naming convention is what it looks for
    #blog/post_detail.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #take away minus sign for oldest to newest ordering -> ['date_posted']
    paginate_by = 8

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')
        

class PostDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Post
#bhufbubyuhbajbybyhguerajiewa;ojiionionjewqaiehaifhnewaiofnewaomfei
    def get_context_data(self, **kwargs):
        #context = get_object_or_404(Post, id = self.kwargs.get('id'))
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post = self.kwargs['pk'])
        #context['images'] = User.objects.filter(user = Comment.name)
        return context
    
    



#view with a form that creates a new post
#the login_required decorator cannot be used on classes so the LoginRequiredMixin does the same functionally but for a class
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user #that form that is trying to be sent has an instance where current user of the author is verified
        return super().form_valid(form) #runs the form valid method on the parent class
    
    success_message = "Post Successfully Created!"
        

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user #that form that is trying to be sent has an instance where current user of the author is verified
        return super().form_valid(form) #runs the form valid method on the parent class
    
    def test_func(self):
        post = self.get_object() #gets the post that we are trying to edit
        if self.request.user == post.author: #is the current logged in user the author of the post trying to be updated?
            return True
        return False
    
    success_message = "Post Successfully Updated!"
        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post     
    success_url = '/'

    def test_func(self):
        post = self.get_object() #gets the post that we are trying to edit
        if self.request.user == post.author: #is the current logged in user the author of the post trying to be updated?
            return True
        return False   


    

# Create your views here.
