from rest_framework import serializers

from feedback.models import QuestionType, Choice, Question, Feedback, Answer, DoneFeedback


class QuestionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionType
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class FeedbackCreateSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True, read_only=True)  # Для отображения списка вопросов в json
    # receivers = UserSerializer(many=True,read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackViewSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True, read_only=True)  # Для отображения списка вопросов в json
    # receivers = UserSerializer(many=True,read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    done_feedback = serializers.PrimaryKeyRelatedField(queryset=DoneFeedback.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    choice = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all(), required=False)

    class Meta:
        model = Answer
        fields = ['id', 'done_feedback', 'question', 'choice']


class DoneFeedbackSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    feedback = serializers.PrimaryKeyRelatedField(queryset=Feedback.objects.all())

    class Meta:
        model = DoneFeedback
        fields = '__all__'
