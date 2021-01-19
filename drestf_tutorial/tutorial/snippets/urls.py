from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

# drestf url suffix patterns support, add 'format=None' in methods in views.py
# such as: http://localhost:8000/snippets.json
urlpatterns = format_suffix_patterns(urlpatterns) 
