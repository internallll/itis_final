import logging

from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.db import models


logger = logging.getLogger('main')


# Менеджер для создания пользователя/суперпользователя
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        try:
            if not email:
                raise ValueError("Email обязателен")
            if not full_name:
                raise ValueError("Полное имя обязательно")

            email = self.normalize_email(email)
            user = self.model(
                email=email,
                full_name=full_name,
                **extra_fields
            )
            user.set_password(password)
            user.save(using=self._db)
        except Exception as e:
            logger.error("Произошла ошибка %s", e)
        logger.info('Create user N %s. %s - %s', user.id, user.email, user.full_name)
        return user

    def create_superuser(self, email, full_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, full_name, password, **extra_fields)


class User(AbstractUser):
    username_validator = None
    username = None
    full_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Поле для записи даты и времени создания пользователя
    # Есть еще возможность переопределить save метод
    Cuser = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    Uuser = models.DateTimeField(verbose_name="Время обновления", auto_now=True, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email


class Role(models.Model):
    title = models.CharField(verbose_name='Название роли', max_length=50)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title
