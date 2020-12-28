"""
render(request, template_name, context=None, content_type=None, status=None, using=None)

request:        request object with http information
template_name:  html with path
context:        a dict, will get passed into template
content_type:   page type, default is text/html
status:         status code, default is 200
using:          decode engine, default is django template
"""
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Tag, Category
from config.models import SideBar

# Create your views here.
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

def post_detail(request, post_id):

    try:
        post_detail = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post_detail = None
    
    #return HttpResponse('detail')
    context = {'post_detail': post_detail, 'sidebars': SideBar.get_all()}
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)




