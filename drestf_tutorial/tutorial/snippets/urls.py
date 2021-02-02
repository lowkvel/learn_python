from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework import renderers
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root

"""
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight',
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list',
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})
"""

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

"""
urlpatterns = [
    
    path('', views.api_root),       # api-root for snippet app

    #path('snippets/', views.snippet_list, name='snippet-list'),             # used with snippet_list views v1 and v2
    #path('snippets/', views.SnippetList.as_view(), name='snippet-list'),     # used with snippet_list views v3 and v4/5
    path('snippets/', snippet_list, name='snippet-list'),     # used with snippet_list views v3 and v4/5

    #path('snippets/<int:pk>/', views.snippet_detail, name='snippet-detail'),           # used with snippet_detail views v1 and v2
    #path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),   # used with snippet_detail views v3 and v4/5
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),   # used with snippet_detail views v3 and v4/5

    #path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'), 
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'), 

    #path('users/', views.UserList.as_view(), name='user-list'),                 # used with user_list
    path('users/', user_list, name='user-list'),                 # used with user_list
    #path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),    # used with user_detail
    path('users/<int:pk>/', user_detail, name='user-detail'),    # used with user_detail
    
]

# drestf url suffix patterns support, add 'format=None' in views in views.py
# such as: http://localhost:8000/snippets.json
urlpatterns = format_suffix_patterns(urlpatterns) 
"""

urlpatterns = [
    path('', include(router.urls)),
]