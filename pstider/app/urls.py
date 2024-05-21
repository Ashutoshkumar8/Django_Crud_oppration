from django.contrib import admin
from django.urls import path,include
from .views import home, croud, delete_croud
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('croud',views.croud),
    path('delete',views.delete_croud),
    path('updateEmployee',views.updateEmployee),
]