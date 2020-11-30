from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    # the home page for learning log
    return render(request, 'learning_logs/index.html')

def topics(request):
    # show all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    """
    A context is a dictionary in which 
    the keys are names we’ll use in the template to access the data, and 
    the values are the data we need to send to the template.
    """
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    # show a single topic and all its entries
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')   # in reverse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


