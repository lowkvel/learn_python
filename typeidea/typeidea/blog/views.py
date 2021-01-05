"""
render(request, template_name, context=None, content_type=None, status=None, using=None)

request:        request object with http information
template_name:  html with path
context:        a dict, will get passed into template
content_type:   page type, default is text/html
status:         status code, default is 200
using:          decode engine, default is django template
"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.db.models import Q

from .models import Post, Tag, Category
from config.models import SideBar
from comment.forms import CommentForm
from comment.models import Comment

# Create your views here.
"""
def post_list(request, category_id=None, tag_id=None):

    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    #context = 'post_list category_id={category_id}, tag_id={tag_id}'.format(category_id=category_id, tag_id=tag_id, )
    #return HttpResponse(context)
    context = {'category': category, 'tag': tag, 'post_list': post_list, 'sidebars': SideBar.get_all()}
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)
"""

"""
def post_detail(request, post_id):

    try:
        post_detail = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post_detail = None
    
    #return HttpResponse('detail')
    context = {'post_detail': post_detail, 'sidebars': SideBar.get_all()}
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)
"""

class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'sidebars': SideBar.get_all(), })
        context.update(Category.get_navs())
        return context

class IndexView(CommonViewMixin, ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list_cbv.html'

class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({'category': category, })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)

class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({'tag': tag, })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)

class PostDetailView(CommonViewMixin, DetailView):
    queryset = Post.latest_posts()
    context_object_name = 'post_detail'
    template_name = 'blog/detail_cbv.html'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'comment_form': CommentForm, 'comment_list': Comment.get_by_target(self.request.path), })
        return context

"""
# replaced by index, category, tag views
class PostListView(ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list_cbv.html'
"""

class SearchView(IndexView):
    def get_context_data(self):
        context = super().get_context_data()
        context.update({'keyword': self.request.GET.get('keyword', '')})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))

class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)