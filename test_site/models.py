
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from manager import CustomUserManager


class User(AbstractUser):
    username = None

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    login = models.CharField(verbose_name='Логин', max_length=30, unique=True)
    password = models.CharField(verbose_name='Пароль', null=True)

    first_name = models.CharField(verbose_name='Имя', max_length=30, null=True, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', null=True, blank=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    number_phone = models.CharField(verbose_name='Номер телефона', max_length=11, null=True, blank=True)
    # role = models.CharField(max_length=20, verbose_name='Роль',
    #                           choices=[('student', 'Студент'), ('administration', 'Сотрудник администрации'),
    #                                    ('applicant', 'Абитуриент'),
    #                                    ('struct_division', 'Структурное подразделение'),
    #                                    ('external_expert', 'Внешний эксперт'), ('teacher', 'Преподаватель'),
    #                                    ('employer', 'Работодатель'), ('graduate', 'Выпускник')], default='student')


    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    role = models.ForeignKey('Role',
                             on_delete=models.SET_NULL, null=True, blank=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login


class Role(models.Model):
    title = models.CharField(verbose_name='Название роли', max_length=50)
    class Meta:
        verbose_name='Роль'
        verbose_name_plural='Роли'

    def __str__(self):
        return self.title

class Feedback(models.Model):
    title = models.CharField(verbose_name='Фидбэк', max_length=50)
    description = models.TextField(verbose_name='Описание')
    array_receivers = models.JSONField(default=list, null=True, blank=True)
    user = models.ForeignKey('User',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name='Опрос'
        verbose_name_plural='Опросы'

    def __str__(self):
        return f'Опрос №{self.pk} {self.title}'



class Question(models.Model):
    title = models.CharField(verbose_name='Вопрос', max_length=50)
    value = models.CharField(verbose_name='Ответ', max_length=50,null=True, blank=True)
    feedback = models.ForeignKey('Feedback',
                                 on_delete=models.CASCADE)
    type = models.ForeignKey('QuestionType',
                              on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name='Вопрос'
        verbose_name_plural='Вопросы'

    def __str__(self):
        return f'Вопрос №{self.pk}'

class QuestionType(models.Model):
    title = models.CharField(verbose_name='Название типа', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'Типы вопросов'



