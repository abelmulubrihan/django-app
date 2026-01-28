from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline, AdminSite, ModelAdmin, InlineModelAdmin, BaseModelAdmin
from .models import Course, Lesson, Question, Choice, Submission

class ChoiceInline(TabularInline):
    model = Choice
    extra = 3

class QuestionInline(StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)