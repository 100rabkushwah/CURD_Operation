"""CRUD_Operation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',view.student),
    path('create_row/',view.creat_row),
    path('show_data/',view.show_data),
    path('show_data/delete_row/',view.delete_row),
    path('create_row/delete_row/', view.delete_row),
    path('show_data/eidt_row', view.edit_row),
    path('update_row/',view.update_row)

]
