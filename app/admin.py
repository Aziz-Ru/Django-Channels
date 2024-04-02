from django.contrib import admin
from .models import *

@admin.register(Chats)
class ChatModelAdmin(admin.ModelAdmin):
    list_display=['id','content','timestamp','group']
