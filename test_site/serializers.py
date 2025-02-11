from rest_framework import serializers
from test_site.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        field = '__all__'




class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set',many=True, read_only=True)
    class Meta:
        model = Feedback
        fields = '__all__'



