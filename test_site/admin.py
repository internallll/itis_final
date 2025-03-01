from django.contrib import admin

from test_site.models import User, Feedback, Role, Question, QuestionType, Answer, DoneFeedback, Choice

# Register your models here.
admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(Role)
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Answer)
admin.site.register(DoneFeedback)
admin.site.register(Choice)