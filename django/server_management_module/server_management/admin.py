from django.contrib import admin

from .models import Log

class LogAdmin(admin.ModelAdmin):

    list_display = ('user_id', 'time_logged' )
    list_filter = ['time_logged']
    order_by = ['time_logged']

admin.site.register(Log, LogAdmin)
