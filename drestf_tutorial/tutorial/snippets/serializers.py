from rest_framework import serializers

from django.contrib.auth.models import User

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

"""
# SnippetSerializer, Serializer, django Form style declaration, v1
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntergerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # create and return a new 'Snippet' instance, given the validated data.
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    # update and return an existing 'Snippet' instance, given the validated data. 
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
"""

# SnippetSerializer, ModelSerializer, django ModelForm style declaration, v2
class SnippetSerializer(serializers.ModelSerializer):

    # The source argument controls which attribute is used to populate a field, 
    # and can point at any attribute on the serialized instance
    # etc, We could have also used CharField(read_only=True) here to replace ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.ModelSerializer):

    #Because 'snippets' is a reverse relationship on the User model, 
    #it will not be included by default when using the ModelSerializer class, 
    #so we needed to add an explicit field for it.
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']



        