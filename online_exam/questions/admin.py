from django.contrib import admin
from .models import question, student

class QuestionAdmin (admin.ModelAdmin):
    list_display=('lessonName','desineDate',)
    list_filter = ('lessonName','desineDate')
    search_fields = ('lessonName','desineDate')

class studentAdmin(admin.ModelAdmin):
    list_display=('name','family')
    search_fields = ('name','family')
# Register your models here.
admin.site.register(question,QuestionAdmin)
admin.site.register(student)

