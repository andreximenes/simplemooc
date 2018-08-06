from django.contrib import admin
from simplemooc.courses.models import *


# Classe usada para customiazar opções e visualizações da tela no admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'create_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Course, CourseAdmin)