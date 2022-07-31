from django.contrib import admin

from .models import *


@admin.action(description='Mostrar todas as perguntas')
def mostrar_todos(modeladmin, requeust, queryset):
    queryset.update(mostrar=True)

@admin.action(description='Não mostrar todas as perguntas')
def nao_mostrar_todos(modeladmin, requeust, queryset):
    queryset.update(mostrar=False)

class QuestionsModelAdmin(admin.ModelAdmin):
    list_display = [
        'q_number',
        'question',
        'ans',
        'mostrar'
    ]
    
    search_fields = [
        'question',   
    ]
    
    list_editable = [
        'mostrar'
    ]
    
    list_filter = [
        'mostrar'
    ]
    
    actions = [
        mostrar_todos,
        nao_mostrar_todos
    ]
    

admin.site.register(QuestionsModel, QuestionsModelAdmin)
