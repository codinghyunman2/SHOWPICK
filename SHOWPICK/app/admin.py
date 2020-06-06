from django.contrib import admin
from .models import Choice, Question, Vote, ConventionBigVote, ConventionSmallVote, ConventionTitleVote
# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Vote)
admin.site.register(ConventionBigVote)
admin.site.register(ConventionSmallVote)
admin.site.register(ConventionTitleVote)