from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:                 # the simplest version needs the Meta class only
        model = Topic           # build a form from the Topic model
        fields = ['text']       # include only the text field
        labels = {'text': ''}   # not to generate a label for the text field

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}     # blank label called 'Entrys:' given
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        """
        A widget is an HTML form element, such as a single-line text box, multi-line text area, or drop-down list.
        By including the widgets attribute, you can override Django’s default widget choices. 
        By telling Django to use a forms.Textarea element, we’re customizing the input widget for the field 'text' 
        so the text area will be 80 columns wide instead of the default 40. 
        """