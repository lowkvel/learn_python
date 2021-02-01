from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [

    #path('snippets/', views.snippet_list),             # used with snippet_list views v1 and v2
    path('snippets/', views.SnippetList.as_view()),     # used with snippet_list views v3 and v4/5

    #path('snippets/<int:pk>/', views.snippet_detail),            # used with snippet_detail views v1 and v2
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),    # used with snippet_detail views v3 and v4/5

]

# drestf url suffix patterns support, add 'format=None' in views in views.py
# such as: http://localhost:8000/snippets.json
urlpatterns = format_suffix_patterns(urlpatterns) 
