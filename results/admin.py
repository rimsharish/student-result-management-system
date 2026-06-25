from django.contrib import admin

# Register your models here.

from .models import Student,Subject,Result

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll_number','batch']
    search_fields = ['name','roll_number']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name','code','max_marks']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks_obtained']
    list_filter = ['subject','student__batch']