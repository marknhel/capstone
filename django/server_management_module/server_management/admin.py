from django.contrib import admin

from .models import Log, Server

class LogAdmin(admin.ModelAdmin):

    list_display = ('user_id', 'time_logged', 'server' )
    list_filter = ['time_logged']
    order_by = ['time_logged']

class ServerAdmin(admin.ModelAdmin):

    list_display = ('server_name', 'ip' )
    order_by = ['server_name']
admin.site.register(Log, LogAdmin)
admin.site.register(Server, ServerAdmin)
