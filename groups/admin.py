from django.contrib import admin
from groups import models
# Register your models here.

'''
 inline gives us functionlity to edit the models on the same page as parent model
 so that when we visit admin page ans see groups we can see the groupmembers as well and edit them
'''
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)