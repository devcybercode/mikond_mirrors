from django.contrib import admin
from .models import (
    UserModel, 
    SocialContact,
    mirrors,
    Contact
)
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.html import format_html

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']
    
@admin.register(SocialContact)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['id', 'instagram', 'telegram']
    list_display_links = ['id', 'instagram', 'telegram']
    search_fields = ['instagram', 'telegram']
       
    
@admin.register(mirrors)
class MirrorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    search_fields = ('name', 'phone')