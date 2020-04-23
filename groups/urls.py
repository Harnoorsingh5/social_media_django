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
