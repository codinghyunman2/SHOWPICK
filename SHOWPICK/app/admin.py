from django.contrib import admin
from .models import Choice, Question, Vote, Custom_user
# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Vote)
admin.site.register(Custom_user)

