from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse 
from django.views import generic

from groups.models import Group, GroupMember

class GroupCreateView(LoginRequiredMixin, generic.CreateView):
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

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
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
    