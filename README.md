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






