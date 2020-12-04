from django.contrib import admin
from .models import Post

# Register your models here.

# normal registration and admin site
# admin.site.register(Post)     # only the post column shown, from the __str__() method

# customized registration and admin site
@admin.register(Post)   # the decorator @admin.register() performs the same function as admin.site.register() do
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') # the selected column will be shown
    list_filter = ('status', 'created', 'publish', 'author')        # filter component
    search_fields = ('title', 'body')                               # search component, searches for two fields
    prepopulated_fields = {'slug': ('title',)}                      # automatically fill the slug based on title field
    raw_id_fields = ('author',)                                     # change the author field from a drop-down menu to a search field
    date_hierarchy = 'publish'                                      # navigate through a date hierarchy based on publish date
    ordering = ('status', 'publish')                                # default ordering for the list_display


