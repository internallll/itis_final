

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from test_site.manager import CustomUserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False,
        default='example@google.com'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(verbose_name='Пароль')
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    number_phone = models.CharField(verbose_name='Номер телефона', max_length=11)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    role = models.ForeignKey('Role',
                             on_delete=models.SET_NULL, null=True, blank=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.pk} {self.email}'


class Role(models.Model):
    title = models.CharField(verbose_name='Название роли', max_length=50)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title


class Feedback(models.Model):
    title = models.CharField(verbose_name='Фидбэк', max_length=50)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    receivers = models.ManyToManyField(User, related_name='received_feedbacks')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, related_name='feedbacks')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return f'Опрос №{self.pk} {self.title}'


class Question(models.Model):
    title = models.CharField(verbose_name='Вопрос', max_length=50)

    feedback = models.ForeignKey('Feedback',
                                 on_delete=models.CASCADE)
    type = models.ForeignKey('QuestionType', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title


class QuestionType(models.Model):
    title = models.CharField(verbose_name='Название типа', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'Типы вопросов'


class Choice(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        return self.value


class DoneFeedback(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    feedback = models.ForeignKey(Feedback,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f"Опрос: '{self.feedback.title}' заполнен пользователем {self.user.email}"


class Answer(models.Model):
    done_feedback = models.ForeignKey(DoneFeedback,
                                      on_delete=models.CASCADE)
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,
                               on_delete=models.CASCADE,
                               blank=True, null=True)

    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ответ на вопрос {self.question.title} в опросе {self.doneFeedback.feedback.title}"
