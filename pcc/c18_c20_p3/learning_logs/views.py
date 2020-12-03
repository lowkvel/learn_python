from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
# unprotect view
def index(request):
    # the home page for learning log
    return render(request, 'learning_logs/index.html')

# the decorator @login_required() will be run before the code in topic(), 
# the user will be redirected to the login page if not logged in, check the end of settings.py
@login_required
def topics(request):
    # show all topics
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')    # show topics belong to the logged in user
    context = {'topics': topics}
    """
    A context is a dictionary in which 
    the keys are names we’ll use in the template to access the data, and 
    the values are the data we need to send to the template.
    """
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    # show a single topic and all its entries
    topic = get_object_or_404(Topic, id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')   # in reverse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required 
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
            new_topic = form.save(commit=False) # not saved into the database yet, commit=False
            new_topic.owner = request.user      # modify some attribute
            new_topic.save()                    # then save 
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required 
def new_entry(request, topic_id):
    # add a new entry for a particular topic
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user. Only the correct user can edit their topics.
    if topic.owner != request.user:
        raise Http404
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

@login_required 
def edit_entry(request, entry_id):
    # edit an existing entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure the topic belongs to the current user. Only the correct user can edit their topics.
    if topic.owner != request.user:
        raise Http404
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





    