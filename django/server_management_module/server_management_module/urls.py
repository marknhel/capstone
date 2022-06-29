from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('server-management/', include('server_management.urls')),
    path('register/', include('register.urls')),
    path('admin/', admin.site.urls),
    path('django-sb-admin/', include('django_sb_admin.urls')),
    path('<int:user_id>/log/', views.log, name='log'),
]
