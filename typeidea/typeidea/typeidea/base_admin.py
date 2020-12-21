from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1. save_model():    automatically fill the field 'owner' using request.user in all models
    2. get_queryset():  filter queryset to display only current user's data 
    """

    exclude = ('owner', )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        return super(BaseOwnerAdmin, self).get_queryset(request).filter(owner=request.user)

    