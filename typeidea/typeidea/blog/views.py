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

# Create your views here.
def post_list(request, category_id=None, tag_id=None):
    
    #return HttpResponse('post_list category_id={category_id}, tag_id={tag_id}'.format(category_id=category_id, tag_id=tag_id, ))
    return render(request, 'blog/list.html', context={'name': 'post_list'})

def post_detail(request, post_id):
    
    #return HttpResponse('detail')
    return render(request, 'blog/detail.html', context={'name': 'post_detail'})




