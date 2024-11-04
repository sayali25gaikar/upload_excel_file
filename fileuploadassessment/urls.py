"""fileuploadassessment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from file_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', index, name='index'),
    path('view-files/', view_uploaded_files, name='view_all_files'),
    path('view-id-data/<int:file_id>/', view_file_data_with_id, name='view_file_data'),
    path('dashboard/', dashboard, name='dashboard')
]
