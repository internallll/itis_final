from django.contrib import admin

from feedback.models import Feedback, Question, QuestionType, Answer, DoneFeedback, Choice
from test_site.models import User, Role

# Register your models here.
admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(Role)
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Answer)
admin.site.register(DoneFeedback)
admin.site.register(Choice)
