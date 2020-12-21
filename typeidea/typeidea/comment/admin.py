from django.contrib import admin

from .models import Comment
from typeidea.custom_admin_site import custom_admin_site

# Register your models here.
@admin.register(Comment, site=custom_admin_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')



