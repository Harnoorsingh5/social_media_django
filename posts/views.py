from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import Http404

from braces.views import SelectRelatedMixin # pip3 install django-braces
from posts import models
from posts import forms
# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()


class PostListView(SelectRelatedMixin, generic.ListView):
    model = models.Post
    template_name = 'posts/post_list.html'
    select_related = ('user', 'group')

class UserPostListView(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    '''
        This method is used by ListView; it determines the list of object that you want to display.
        By default it gives you all or the model you specify, by overriding this method you can extend or completely replace the logic
        
        In this case all the posts will come for particular user, so in order to get the post related to a logged in user
        we have replaced the logic using prefetch_related and __iexact.
    '''
    def get_queryset(self): 
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
            # assign the user who belong to particular post to ->
            # Users object, then prefetch related posts for that particular user
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
    
    '''

    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user 
        return context
    

class PostDetailView(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')
    template_name = 'posts/post_detail.html'

    def get_queryset(self): 
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class PostCreateView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = models.Post
    temoplate_name = 'posts/post_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user' ,'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self): 
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)