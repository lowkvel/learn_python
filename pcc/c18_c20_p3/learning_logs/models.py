from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    # A topic the user is learning about
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return a string representation of the model
        return self.text

class Entry(models.Model):
    # something specific learned about a topic, m-1 relationship
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    """
    The on_delete=models.CASCADE argument tells Django that when a topic is deleted, 
    all the entries associated with that topic should be deleted as well. This is known as a cascading delete.
    """
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # return a string reprentation of the  model
        return f"{self.text[:50]}..."   # only the first 50 characters will be shown

