from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "NBA Polls Admin"
admin.site.site_title = "NBA Polls Admin Area"
admin.site.index_title = "Welcome to the NBA Polls Admin Area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # value on right side in next line is a Tuple. Tuples need a hanging comma after the last parameter.
    fieldsets =[(None, {'fields': ['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

# Makes Question and Choice available in my admin website.
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
