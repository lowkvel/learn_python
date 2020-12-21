from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'is_nav', 'post_count', 'created_time')    # for page display
    fields = ('name', 'status', 'is_nav')   # for modification

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

class CategoryOwnerFilter(admin.SimpleListFilter):
    """ 自定义过滤器只展示当前用户创建的分类 """

    title = '分类过滤器'                      # for filter title display, replace the original "分类" from Meta of blog/models.py by "分类过滤器"
    parameter_name = 'owner_category'       # for URL query display, such as: "?owner_category=1"

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()          # for URL queryset value, such as: if "?owner_category=1", then self.value() = 1
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm        # used for admin forms
    
    list_display = ('title', 'category', 'status', 'owner', 'created_time', 'operator')
    list_display_links = None
    #list_display_links = ['owner', ]

    list_filter = (CategoryOwnerFilter, 'tag', )
    search_fields = ('title', 'category__name')

    actions_on_top = True
    actions_on_bottom = False
    save_on_top = False

    #fields = (('category', 'title'), 'desc', 'status', 'content', 'tag')
    fieldsets = (
        ('基础配置', {'description': '基础配置描述',                        # description
                    'fields': ('title', 'category', 'status', ), }),
        ('内容', {                                                      # leave empty
                    'fields': ('desc', 'content', ), }),
        ('额外信息', {'classes': ('collapse', ),                        # classes: collapse/wide/selfdefined css
                    'fields': ('tag', ), }) 
    )

    """
    class Media:
        css = {'all': ("https://https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ), }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )
    """

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id,)))
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        return super(PostAdmin, self).get_queryset(request).filter(owner=request.user)

    