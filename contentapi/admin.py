from django.contrib import admin
from .models import UserModel, ContentModel
# Register both models 
admin.site.register(UserModel)
admin.site.register(ContentModel)