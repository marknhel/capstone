from django.contrib import admin

from .models import Profile, User

class ProfileAdmin(admin.ModelAdmin):

    fieldsets = [
            ( 'Name',               { 'fields': ['first_name']}),
#            ( None,                 { 'fields': ['middle_name']}),
            ( None,                 { 'fields': ['last_name']}),
            ( 'Academic Infomation', { 'fields': ['college']}),
#            ( None,                 { 'fields': ['department']}),
            ( None,                 { 'fields': ['course']}),
            ]

    list_display = ('last_name', 'first_name', 'college', 'course')
    list_filter = ['last_name']
    order_by = ['last_name']

class UserAdmin(admin.ModelAdmin):

    list_display = ('profile_id','mac_address', 'usertype', 'blocked')
    list_filter = ['mac_address']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)
