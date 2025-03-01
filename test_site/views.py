from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.views import APIView

from test_site.permissions import IsOwnerOrAdminOnly, IsSelfOrAdmin, IsFeedbackOwner
from test_site.serializers import *

logger = logging.getLogger('main')

# Пользователи
# Представление для обновления информации о пользователе
class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSelfOrAdmin,)

# Представление для удаления пользователя
class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSelfOrAdmin,)

    def perform_delete(self, serializer):
        user = serializer.save()
        logger.info('User %s deleted', user.pk)

# Представление для создания нового пользователя
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    logger.info('User created')


# Представление для списка пользователей
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    logger.info('Open user list')

# Опросы
# Представление для создания опроса
class FeedBackCreateAPIView(generics.CreateAPIView):
    try:
        queryset = Feedback.objects.all()
        serializer_class = FeedbackCreateSerializer
        permission_classes = (IsAuthenticated, )
    except Exception as e:
        logger.error('Произошло исключение: %s', e)


    logger.info('Feedback create')


#Представление для обновления опроса
class FeedBackUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackViewSerializer
    permission_classes = (IsOwnerOrAdminOnly, )

    # Функция для возможности в логе указывать айди
    def perform_update(self, serializer):
        feedback = serializer.save()
        logger.info("Feedback %s updated", feedback.pk)


# Представление для удаления опроса
class FeedBackDeleteAPIView(generics.DestroyAPIView):
    try:
        queryset = Feedback.objects.all()
        serializer_class = FeedbackViewSerializer
        permission_classes = (IsOwnerOrAdminOnly,)
    except Exception as e:
        logger.error("Ошибка при попытке удаления Feedback %s", e)


    # Функция для возможности в логе указывать айди
    def perform_delete(self, serializer):
        feedback = serializer.save()
        logger.info("Feedback %s deleted", feedback.pk)

# Представление для просмотра списка опросов
class FeedBackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackViewSerializer
    permission_classes = (IsAdminUser,)

    logger.info("Open Feedback list")




#Представление для просмотра списка опросов, которые пользователь создал
class FeedBackUserFilterListAPIView(generics.ListAPIView):
    serializer_class = FeedbackViewSerializer
    permission_classes = (IsFeedbackOwner, )
    def get_queryset(self):
        try:

            user_pk = self.kwargs.get('pk')

            return Feedback.objects.filter(user_id = user_pk)
        except Exception as e:
            logger.error("Ошибка при попытке обращения к user_pk %s", e)



#Вопросы
# Представление для вывода списка вопросов определенного опросника

class QuestionListFilterAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser, )
    try:
        def get_queryset(self):
            feedback_pk = self.kwargs.get('pk')
            return Question.objects.filter(feedback_id = feedback_pk)
    except Exception as e:
        logger.error("Ошибка при сопоставлении вопроса и фидбэка")

#Представление для просмотра всех вопросов
class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser, )

#Представление для обновления/удаления вопроса
class QuestionUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsOwnerOrAdminOnly, )


class QuestionCreate(generics.CreateAPIView):
    try:
        queryset = Question.objects.all()
        serializer_class = QuestionSerializer
        permission_classes = (IsAuthenticated, )
    except Exception as e:
        logger.error("Ошибка при попытке создания вопроса %s", e)



#Представление для просмотра фидбеков у определенного юзера
class FeedbackReceiversListAPIView(generics.ListAPIView):
    serializer_class = (FeedbackViewSerializer)
    permission_classes = (IsSelfOrAdmin, )

    try:
        def get_queryset(self):
            user_pk = self.kwargs.get('pk')
            return Feedback.objects.filter(receivers__pk=user_pk)
    except Exception as e:
        logger.error("Ошибка при попытке обращения к user_pk %s", e)



#Работа с заполненными фидбеками

class DoneFeedbackListAPIView(generics.ListAPIView):
    queryset = DoneFeedback.objects.all()
    serializer_class = (DoneFeedbackSerializer)
    permission_classes = (IsAdminUser, )

class DoneFeedbackCreateAPIView(generics.CreateAPIView):
    queryset = DoneFeedback.objects.all()
    serializer_class = (DoneFeedbackSerializer)
    permission_classes = (IsAuthenticated, )

class DoneFeedbackUpdateDeleteAPIView(generics.RetrieveUpdateAPIView):
    queryset = DoneFeedback.objects.all()
    serializer_class = (DoneFeedbackSerializer)
    permission_classes = (IsOwnerOrAdminOnly, )


class AnswerView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsSelfOrAdmin, )

class AnswerUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsOwnerOrAdminOnly, )

class ChoicesView(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer
    permission_classes = (IsSelfOrAdmin, )

class ChoicesUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer
    permission_classes = (IsSelfOrAdmin, )