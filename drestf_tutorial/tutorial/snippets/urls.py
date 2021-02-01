from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [

    #path('snippets/', views.snippet_list),             # used with snippet_list v1 and v2
    path('snippets/', views.SnippetList.as_view()),     # used with snippet_list v3

    #path('snippets/<int:pk>/', views.snippet_detail),            # used with snippet_detail v1 and v2
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),    # used with snippet_detail v3
]

# drestf url suffix patterns support, add 'format=None' in views in views.py
# such as: http://localhost:8000/snippets.json
urlpatterns = format_suffix_patterns(urlpatterns) 
