from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from test_site.models import User, Feedback, Question
from test_site.permissions import IsOwnerOrAdminOnly
from test_site.serializers import UserSerializer, FeedbackSerializer, QuestionSerializer


# Пользователи
# Представление для обновления информации о пользователе
class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

# Представление для удаления пользователя
class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

# Представление для создания нового пользователя
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

# Представление для списка пользователей
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

# Опросы
# Представление для создания опроса
class FeedBackCreateAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (AllowAny, )

#Представление для обновления опроса
class FeedBackUpdateAPIView(generics.UpdateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsOwnerOrAdminOnly, )

# Представление для удаления опроса
class FeedBackDeleteAPIView(generics.DestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsOwnerOrAdminOnly,)

# Представление для просмотра списка опросов
class FeedBackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer



#Представление для просмотра списка опросов определенного пользователя
class FeedBackUserFilterListAPIView(generics.ListAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get('pk')
        return Feedback.objects.filter(user_id = user_pk)



#Вопросы
# Представление для вывода списка вопросов определенного опросника

class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def get_queryset(self):
        feedback_pk = self.kwargs.get('pk')
        return Question.objects.filter(feedback_id = feedback_pk)


class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser, )


