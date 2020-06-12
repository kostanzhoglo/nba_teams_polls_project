from django.contrib import admin

from .models import Question, Choice



# Makes Question and Choice available in my admin website.
admin.site.register(Question)
admin.site.register(Choice)
