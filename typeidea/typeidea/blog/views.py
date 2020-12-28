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

from .models import Post, Tag

# Create your views here.
def post_list(request, category_id=None, tag_id=None):

    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            post_list = post_list.filter(category_id=category_id)
    
    #return HttpResponse('post_list category_id={category_id}, tag_id={tag_id}'.format(category_id=category_id, tag_id=tag_id, ))
    return render(request, 'blog/list.html', context={'post_list': post_list})

def post_detail(request, post_id):

    try:
        post_detail = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post_detail = None
    
    #return HttpResponse('detail')
    return render(request, 'blog/detail.html', context={'post_detail': post_detail})




