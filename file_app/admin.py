from django.contrib import admin
from .models import UserData, FileUpload
# Register your models here.
admin.site.register(UserData)
admin.site.register(FileUpload)