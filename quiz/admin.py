from django.contrib import admin

from .models import *


class QuestionsModelAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'ans'
    ]
    
    search_fields = [
        'question'
    ]
    

admin.site.register(QuestionsModel, QuestionsModelAdmin)
