"""Defines URL patterns for learning_logs."""
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # url pattern, index() functions in views.py, name of this pattern
    path('', views.index, name='index'),    # home page
    path('topics/', views.topics, name='topics'),   # pages that shows all topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # detail of a single topic
    path('new_topic', views.new_topic, name='new_topic'),   # form of a new topic, user input
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),   # add entry for a single topic
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),    # edit entry for a single topic
]