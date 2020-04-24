# social_media_django

```
social_media_django
|
|———accounts
|	|
|	|———— migrations
|	|
|	|——templates
|	|	 |——accounts
|	|	    |———login.html
|	|		|———signup.html
|	|———— __init__.py
|	|———— admin.py
|	|———— apps.py
|	|———— forms.py
|	|———— models.py
|	|———— tests.py
|	|———— urls.py	
|	|———— views.py
|
|—groups
|	|— migrations
|		|
|		|———— templates
|		|	   |——groups
|		|		   |———group_base.html
|		|   	   |———group_detail.html
|		|    	   |———group_form.html	
|		|		   |———group_list.html
|		|———— __init__.py
|		|———— admin.py
|		|———— apps.py
|		|———— forms.py
|		|———— models.py
|		|———— tests.py
|		|———— urls.py	
|		|———— views.py
|
|——posts
|	|——migrations
|	|
|	|——templates
|	|	|——posts
|	|		|———_post.html
|	|		|———post_base.html
|	|		|———post_confirm_delete.html
|	|		|———post_detail.html					 
|	|		|———post_form.html
|	|		|———post_list.html	
|	|		|———user_post_list.html
|	|———— __init__.py
|	|———— admin.py
|	|———— apps.py
|	|———— forms.py
|	|———— models.py
|	|———— tests.py
|	|———— urls.py	
|	|———— views.py
|
|—social_media_django
|	|———— __init__.py
|	|———— asgi.py
|	|———— settings.py
|	|———— urls.py
|	|———— views.py
|	|———— wsgi.py
|				
|—static
|	|—social_media_django
|		|—css
|		|  |———master.css
|		|—js
|		   |———master.js
|				
|—templates
|	|—base.html
|		|———— index.html
|		|———— test.html
|		|———— thanks.html	
|—manage.py				
```

## STEP 1
* Set up sign in and sign up pages
* For this firstly create an application in your projects-> named; accounts

* In projects template folder create four html file; 
* 1) base.html
```
<!DOCTYPE html>
{% load static %}
<html>
<head>
    <meta charset="utf-8">
    <title>Star Social</title>
    <!--Bootstrap-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <!--Custom CSS-->
    <link rel="stylesheet" href="{% static 'social_media_django/css/master.css' %}">
    <!--Fonts-->
    <link href="https://fonts.googleapis.com/css?family=Montserrat+Alternates|Russo+One&display=swap" rel="stylesheet">

</head>
<body>
    <!--Navbar-->
    <nav class="navbar mynav navbar-expand-lg techfont custom-navbar">
        <a class="navbar-brand bigbrand mynav" href="{% url 'index' %}">Star Social</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent" >
            <ul class="navbar-nav ml-auto navbar-right" >
                {% if user.is_authenticated %}
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'posts:create' %}"> Post <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'groups:all' %}"> Groups <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'groups:create' %}"> Create Group <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'accounts:logout' %}"> Log Out <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link"> Welcome: {{ user.username }} <span class="sr-only">(current)</span></a>
                    </li>
                {% else %}
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'groups:all' %}"> Groups <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'accounts:login' %}"> Log In </span></a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'accounts:signup' %}"> Sign Up </span></a>
                    </li>
                {% endif %}
            </ul>
        </div>
    </nav>

    <div class="container mycontent">
        {% block content %}
            
        {% endblock %}
    </div>
    <script type="text/javascript" src="{% static 'social_media_django/js/master.js' %}"> </script>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
    
</body>
</html>
```
* 2) index.html
```
<!DOCTYPE html>
{% extends 'base.html' %}
{% block content %}
    <h1> Welcome to Star Social! </h1>
{% endblock %}
```
* 3) test.html
```
{% extends 'base.html' %}
{% block content %}
    <h1> You are now logged in! </h1>
{% endblock %}
```
* 4) thanks.html
```
{% extends 'base.html' %}
{% block content %}
    <h1> Thanks for visiting! </h1>
{% endblock %}
```

* After creating these templates link them with projects views.py and urls.py

views.py
```
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
```

urls.py
```
from django.contrib import admin
from django.urls import path,include
from social_media_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name="index"),
    path('test/', views.TestPage.as_view(), name="test"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('groups/', include('groups.urls', namespace='groups')),
]
```

* Now for login and logout we are using Django's inbuilt views that we can directly import in our application's urls.py file
(LoginView and LogoutView)
* accounts urls.py
```
from django.urls import path,include
from django.contrib.auth import views as auth_views # we are using django's inbuilt view for authorization
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), # login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page':'/'}), # logout view
    path('signup/', views.SignUp.as_view(), name='signup'), # we are creating our own signup page
]
```

* accounts views.py
```
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
```

* accounts forms.py
we are getting django's in built UserCreation form.
Then we are sellecting the fields in Meta class
```
from django.contrib.auth import get_user_model # getting the in built user model
from django.contrib.auth.forms import UserCreationForm 

class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs): #setting labels for fields
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
```

* accounts models.py
We are getting Django's inbuilt User model
```
from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
```

* accounts/login.html
We are creating login.html that will be accessed by Django's LoginView.

```
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}
<div class="container">
    <h1> Log In </h1>
    <form method="POST">
        {% csrf_token %}
        {% bootstrap_form form%}
        <input type="submit" class="btn btn-primary" value="Login">
    </form>
</div>
{% endblock %}
```

* accounts/signup.html

```
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}
<div class="container">
    <h1> Sign Up </h1>
    <form method="POST">
        {% csrf_token %}
        {% bootstrap_form form%}
        <input type="submit" class="btn btn-primary" value="Sign Up">
    </form>
</div>
{% endblock %}
```

## STEP 2
* After working on account application, we will a create a new application groups and register it in settings.py
* we will be working on groups application

* In projects urls.py include group urls fle
```
    path('groups/', include('groups.urls', namespace='groups')),
```

* First task while creating an application should be to create a model/db in django
* So for that got to models.py
1) First model is -> Group
Group consists of 5 colums; namely,
->  name (Char field), slug (slug field), description (text field), description_html (text field), members (many to many field)

* what exactly is SlugField() ?
```
it's human friendly (eg. /blog/ instead of /1/)
it's good SEO to create consistency in title, heading and URL.
```
2) Second Model is -> GroupMember
GroupMemeber consists of 2 columns; namely,
group and user.
where, group is foreign key 
user is foreign key
* groups models.py
```
from django.db import models
from django.utils.text import slugify # helps remove aplhanumeric chars like _
import misaka # helps in adding links in the text or markdown texts
from django.urls import reverse 

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, blank=True, default='')
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return super().user.username
```

* After creating model creata model form in forms.py
* groups forms.py
Simply link the model with form 
```
from django import forms
from django.contrib.auth.models import User
from groups.models import Group

class GroupForm(forms.ModelForm): 
    
    class Meta():
        fields = ('name', 'description')
        model = Group
```

* After this work on views.py file to create the view for application

1) Create View - for the form or creating group form
2) Detail View - for the single group details 
3) List View - for list of all the groups
4) Redirect View - Join Group (for joining group)
                 - Leave Group (for leaving group)
```
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from groups import forms
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse 
from django.views import generic

from groups.models import Group, GroupMember

class GroupCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.GroupForm
    fields = ('name', 'description')
    model = Group
    template_name = 'groups/group_form.html'

class GroupDetailView(generic.DetailView):
    model = Group
    template_name = 'groups/group_detail.html'

class GroupListView(generic.ListView):
    model = Group
    template_name = 'groups/group_list.html'

class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    '''
        once a person joins the groups where will he redirected to
        is specified by this function.
        In this case we are redirectng to single group detail,
        with slug in the url
    '''
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    '''
        get method is to specify what functionalities need to done 
        get_object_or_404:- Calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception.

    '''
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group) # create is inbuilt class method for inserting a row in Model
        except:
            messages.warning(self.request,'Warning! Already a member')
        else:
            messages.success(self.request,'You are a member now')

        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})
    
    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug')).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this group!')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group!')

        return super().get(request, *args, **kwargs)
    
```
* After this specify the urls in urls.py file:

```
from django.urls import path
from groups import views

app_name = "groups"

urlpatterns = [
    path('', views.GroupListView.as_view(), name='all'),
    path('new/', views.GroupCreateView.as_view(), name='create'),
    path('post/in/<slug:slug>/', views.GroupDetailView.as_view(), name='single'),
    path('join/<slug:slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug:slug>/', views.LeaveGroup.as_view(), name='leave'),
]

```

* Then specify the template files for each view specified:

- group_base.html
```
{% extends 'base.html'%}
{% block content %}
    <div class="container">
        <div class="row">
            {% block pregroup %} 
            {% endblock %}

            {% block group_content %}
            {% endblock %}

            {% block postgroup %}
            {% endblock %}
        </div>
    </div>
{% endblock %}
```

- group_form.html (for GroupCreateView)
```
{% extends 'groups/group_base.html' %}
{% load bootstrap4 %}
{% block group_content %}
    <div class="container">
        <h4> Create a new group! </h4>
        <form class="groupForm" method="POST" action="{% url 'groups:create' %}">
            {% csrf_token %}
            {% bootstrap_form form %}
            <input type="submit" class="btn btn-primary btn-large" value="Create">
        </form>
    </div>
{% endblock %}
```

- group_list.html (for GroupListView) (Contains : Welcome message and list of groups on righ side)
```
{% extends 'groups/group_base.html' %}
{% block pregroup %}
    <div class="col-md-4">
        <div class="content">
            {% if user.is_authenticated %}
                <h2> Welcome back! 
                    <a href="{% url 'posts:for_user' username=user.username %}">
                        @{{user.username}}
                    </a>
                </h2>
            {% endif %}

            <h2>Groups</h2>
            <p> Welcome to groups page! </p>
        </div>

        {% if user.is_authenticated %}
            <a href="{% url 'groups:create' %}" class="btn btn-md btn-fill btn-warning">
                <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"> Create New Group! </span> </a>
        {% endif %}

    </div>
{% endblock %}

{% block group_content %}
    <div class="col-md-8">
        <div class="list-group">
            {% for group in group_list %}
                <a class="list-group-item" href="{% url 'groups:single' slug=group.slug %}"> 
                    <h3 class="title list-group-item-heading"> {{group.name}} </h3>
                    <div class="list-group-item-text container-fluid">
                        {{ group.description_html|safe }}
                        <div class="row">
                            <div class="col-md-4">
                                <span class="badge"> {{ group.members.count }} </span>
                                member{{ group.members.count|pluralize }}
                            </div>
                            <div class="col-md-4">
                                <span class="badge"> {{ group.posts.count }} </span>
                                post{{ group.posts.count|pluralize }}
                            </div>
                        </div>
                    </div>
                </a>
            {% endfor %}
        </div>
    </div>
{% endblock %}
```

- group_detail.html (for GroupDetailView) (contains )
```
{% extends 'groups/group_base.html' %}
{% block pregroup %}
    <h1> {{ group.name }} </h1>
    <h2> {{ group.members.count }} members </h2>
    <div class="container">
        {% if user in group.members.all %}
            <a href="{% url 'groups:leave' slug=group.slug %}" class="btn btn-lg btn-fill btn-warning"> 
                <span class="glyphicon glyphicon-remove-sign" aria-hidden="true"> Leave </span> </a>
        {% else %}
            <a href="{% url 'groups:join' slug=group.slug %}" class="btn btn-lg btn-fill btn-primary"> 
                <span class="glyphicon glyphicon-ok-sign" aria-hidden="true"> Join </span> </a>
        {% endif %}
    </div>
{% endblock %}

{% block group_content %}
    <div class="col-md-8">
        {% if group.posts.count == 0 %}
            <h2> No posts in this group yet! </h2>
        {% else %}
            {% for post in group.posts.all %}
                {% include "posts/_post.html" %}  <!--include is like extends but, it injects the html in this line only-->
                <!--this above file contains the list of all the posts in that particular group-->
            {% endfor %}
        {% endif %}
    </div>
{% endblock %}
```

## STEP 3
* After working on groups application, we will a create a new application posts and register it in settings.py
* we will be working on posts application

* We will start by creating model for Posts
- It consists of 1 table named "Posts" with 5 fields - user, created_at, message, message_html and group
- where user and group is foreign key
* posts models.py
```
from django.db import models
from django.urls import reverse 
from django.conf import settings

import misaka

from groups.models import Group, GroupMember

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.message
    '''
        this save method is to save the post in database
    '''
    def save(self,*args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    '''
        to specify the url after creation of post
    '''
    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username, "pk" : self.pk} )
    
    '''
        some meta data ordering(order by) and uniqueness is specified
    '''
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
```

* After creating model create model form in forms.py
* posts forms.py
```
from django import forms
from django.contrib.auth.models import User
from posts.models import Post

class PostForm(forms.ModelForm): 
    
    class Meta():
        fields = ('message', 'group')
        model = Post
```

* After this create views in views.py
* posts views.py
- 2 List views  : PostListView and UserPostListView
- 1 Detail view : PostDetailView
- 1 Create view : PostCreateView
- 1 Delete view : PostDeleteView
```
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import Http404
from posts import forms
from braces.views import SelectRelatedMixin # pip3 install django-braces
from posts import models
from posts import forms
# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model() # to get in built django user model 


'''
    SelectRelatedMixin: A simple mixin which allows you to specify a list or tuple of foreign key fields to perform a select_related on.
    select_related = ('user', 'group') : over here we are performing select related on two foreign key fields user and group
    select_related does an SQL join and therefore gets the results back as part of the table from the SQL server.
    we want posts related to that particular user who is logged in or for that particular group only
'''
class PostListView(SelectRelatedMixin, generic.ListView):
    model = models.Post
    template_name = 'posts/post_list.html'
    select_related = ('user', 'group')

'''
    This view is only to show or list the post related to logged in user
'''
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
    
'''
    To specify the single post detail view
'''
class PostDetailView(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')
    template_name = 'posts/post_detail.html'

    def get_queryset(self): 
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

'''
    post creat view - post create form
'''
class PostCreateView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    form_class = forms.PostForm
    fields = ('message', 'group')
    model = models.Post
    temoplate_name = 'posts/post_form.html'

    def form_valid(self, form): # Redirects to get_success_url()
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

'''
    post delete view for deleting a post
'''
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
```

* cofigure url inurls.py
* posts urls.py

```
from django.urls import path
from posts import views

app_name = "posts"

urlpatterns = [
    path('', views.PostListView.as_view(), name='all'),
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('by/<str:username>/', views.UserPostListView.as_view(), name='for_user'),
    path('by/<str:username>/<int:pk>/', views.PostDetailView.as_view(), name='single'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
]
```

* After all this create different templated required for this application

- post_base.html
```
{% extends 'base.html'%}
{% block content %}
    <div class="posts-page">
        <div class="comtainer">
            <div class="row">
                {% block prepost %}
                {% endblock %}

                {% block post_content %}
                {% endblock %}

                {% block post_post %}
                {% endblock %}
            </div>
        </div>
    </div>
{% endblock %}
```

- _post.html
```
<div class="post media">
    <h3> {{ post.message_html|safe }} </h3>
    <div class="media-body">
        <strong> {{ post.user.username }} </strong>
        <h5 class="media-heading">
            <span class="username">
                <a href="{% url 'posts:for_user' username=post.user.username %}"> @{{ post.user.username }} </a>
            </span>
            <time class="time">
                <a href="{% url 'posts:single' username=post.user.username pk=post.pk %}">{{ post.created_at }}</a>
            </time>
            {% if post.group %}
                <span class="group-name">in <a href="#">{{ post.group.name }}</a></span>
            {% endif %}
        </h5>

        <div class="media-footer">
            {% if user.is_authenticated and post.user == user and not hide_delete %}
                <a href="{% url 'posts:delete' pk=post.pk %}" title="delete" class="btn btn-simple">
                    <span class="glyphicon glyphicon-remove text-danger" aria-hidden="true">  </span>
                    <span class="text-danger icon-label"> Delete </span>
                </a>
            {% endif %}
        </div>
    </div>
</div>
```

- post_list.html
```
{% extends 'posts/post_base.html' %}
{% block pre_post_content %}
    <div class="col-md-4">
        {% if request.user.is_authenticated %}
            <div class="card card-with-shadow">
                <div class="content">
                    <h5 class="title"> Your Groups: </h5>
                    <ul class="list-unstyled">
                        {% for member_group in get_users_group %}
                            <li class="group li-with-bullet"> 
                                <a href="{% url 'groups:single' slug=member_group.group.slug %}">  </a>
                            </li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        {% endif %}
        <div class="card card-with-shadow">
            <div class="content">
                <h5 class="title"> All Groups: </h5>
                <ul class="list-unstyled">
                    {% for other_group in get_other_group %}
                        <li class="group li-with-bullet"> 
                            <a href="{% url 'groups:single' slug=other_group.group.slug %}">  </a>
                        </li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
{% endblock %}

{% block post_content %}
    <div class="col-md-8">
        {% for post in post_list %}
            {% include "posts/_post.html" %}
        {% endfor %}
    </div>
{% endblock %}
```

- user_post_list.html
```
{% extends 'posts/post_base.html' %}

{% block prepost %}
    <div class="col-md-4">
        <h1> @{{ post_user.username }} </h1>
    </div>
{% endblock %}

{% block post_content %}
    <div class="col-md-8">
        {% for post in post_list %}
            {% include "posts/_post.html" %}
        {% endfor %}
    </div>
{% endblock %}
```

- post_detail.html
```
{% extends 'posts/post_base.html' %}

{% block post_content %}
    <div class="col-md-8">
        {% include "posts/_post.html" %}
    </div>
{% endblock %}
```

- post_form.html

```
{% extends 'posts/post_base.html' %}
{% load bootstrap4 %}
{% block post_content %}
    <div class="container">
        <h4> Create a new post! </h4>
        <form class="postForm" method="POST" action="{% url 'posts:create' %}">
            {% csrf_token %}
            {% bootstrap_form form %}
            <input type="submit" class="btn btn-primary btn-large" value="Post">
        </form>
    </div>
{% endblock %}
```

- post_confirm_delete.html
```
{% extends 'posts/post_base.html' %}
{% block post_content %}
    <h3> Are you sure you want to delete this post? </h3>

    <div class="posts">
        {% include "posts/_post.html" with post=object hide_delete=True %}
    </div>
    <form method="POST">
        {% csrf_token %}
        <input type="submit" class="btn btn-danger btn-large" value="Confirm Delete">
        <a href="{% url 'posts:single' username=user.username pk=object.pk %}" class="btn btn-simple btn-large btn-default">Cancel</a>
    </form>
{% endblock %}
```