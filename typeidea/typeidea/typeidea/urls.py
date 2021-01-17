"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.sitemaps import views as sitemap_views

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

#from blog.views import post_list, post_detail
from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from config.views import LinkListView
from comment.views import CommentView
from .custom_admin_site import custom_admin_site

#from blog.apis import post_list, PostList
from blog.apis import PostViewSet, CategoryViewSet
from blog.apps import BlogConfig

router = DefaultRouter()
router.register('post', PostViewSet, basename='api-post')
router.register('category', CategoryViewSet, basename='api-category')

urlpatterns = [
    
    #url(r'^$', post_list),
    #path('', post_list, name='index'), 
    path('', IndexView.as_view(), name='index_cbv'),

    #url(r'^category/(?P<category_id>\d+)/$', post_list),
    #path('category/<int:category_id>/', post_list, name='post_list_from_category_id'),  
    path('category/<int:category_id>/', CategoryView.as_view(), name='post_list_from_category_id_cbv'),
    #path(),

    #url(r'^tag/(?P<tag_id>\d+)$', post_list),
    #path('tag/<int:tag_id>/', post_list, name='post_list_from_tag_id'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='post_list_from_tag_id_cbv'),

    # django rest framework path
    #path('api/post/', post_list, name='post-list'),
    #path('api/post/', PostList.as_view(), name='post-list'),
    path('api/', include((router.urls, BlogConfig.name), namespace="api")),

    path('api/docs/', include_docs_urls(title='typeidea apis')),
    
    #url(r'^post/(?P<post_id>\d+).html&', post_detail),
    #path('post/<int:post_id>/', post_detail, name='post_detail_from_post_id'),          
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail_from_post_id_cbv'),

    path('search/', SearchView.as_view(), name='search_results'),

    path('author/<int:owner_id>/', AuthorView.as_view(), name='post_list_from_author_id_cbv'),
    
    #url(r'^links/$', links),
    #path('links/', links, name='links'),
    path('links/', LinkListView.as_view(), name='links'),

    path('comment/', CommentView.as_view(), name='comment'),

    path('rss/', LatestPostFeed(), name='rss'),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}), 
    
    path('super_admin/', admin.site.urls, name='super_admin'),      # used for super admin
    path('admin/', custom_admin_site.urls, name='normal_admin'),    # used for normal admin
]
