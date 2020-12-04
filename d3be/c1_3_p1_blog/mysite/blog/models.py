from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'), )

    title = models.CharField(max_length=250)    # title field, CharField --> VARCHAR in database
    slug = models.SlugField(max_length=250, unique_for_date='publish')  # used in build fancy urls for blog posts
    """
    A slug is a short label that contains only letters, numbers, underscores, or hyphens. 
    You will use the slug field to build beautiful, SEO-friendly URLs for your blog posts.
    You have added the unique_for_date parameter to this field 
    so that you can build URLs for posts using their publish date and slug. 
    Django will prevent multiple posts from having the same slug for a given date
    """

    # bidirection link specifies the name of the reverse relationship, from User to Post, with the related_name attribute
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')   

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)    # current datetime in a timezone-aware format
    created = models.DateTimeField(auto_now_add=True)       # the date will be saved automatically when creating an object.
    updated = models.DateTimeField(auto_now=True)           # the date will be updated automatically when saving an object.

    # use a choices parameter, so the value of this field can only be set to one of the given choices defined above
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # The Meta class inside the model contains metadata.
    class Meta:
        ordering = ('-publish',)

    # the default human-readable representation of the object.
    def __str__(self):
        return self.title

