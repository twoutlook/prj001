from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)
# https://docs.djangoproject.com/en/1.10/intro/tutorial07/
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
