from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    # add a new topic to database
    # 1. initial [request] for the new_topic page, blank form shown
    # 2. redirect the filled form, and [redirect] to the topics page
    if request.method != 'POST':
        form = TopicForm()  # no data submitted, create a blank form
    else:
        # make an instance of TopicForm and pass it the data entered by the user, stored in request.POST
        form = TopicForm(data=request.POST)     # POST data submitted, process data
        # checks that all required fields have been filled in (all fields in a form are required by default) and 
        # that the data entered matches the field types expected
        if form.is_valid():             
            form.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    # add a new entry for a particular topic
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()  # no data submitted, create a blank form
    else:
        form = EntryForm(data=request.POST)     # POST data submitted, process data
        if form.is_valid():
            new_entry = form.save(commit=False) # the argument commit=False tell Django to create a new entry object and assign it to new_entry without saving it to the database yet
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    # edit an existing entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)    # create a entry form prefilled with current existing entry object, not blank
        #form = EntryForm()                  # create a empty entry form
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)     # create a form instance based on the information associated with the existing entry object, 
        if form.is_valid():                                     # updated with any relevant data from request.POST
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)





    