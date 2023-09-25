from django.urls import path

from . import views

urlpatterns = [
        path('',views.index, name='manage-index'),
        path('blocked/',views.blocked, name='blocked'),
]
