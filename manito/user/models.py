from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, email, name, password):
        user = self.model(
            email=email,
            name=name,
        )
        user.set_password(password)
        user.save()

    def create_superuser(self, email, name, password):
        user = self.model(
            email=email,
            name=name,
        )
        user.set_password(password)
        user.is_superuser = True
        user.save()


class User(AbstractBaseUser):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'email'

    email = models.CharField(
        verbose_name="이메일",
        unique=True,
        max_length=255,
    )

    name = models.CharField(
        verbose_name="이름",
        max_length=255,
    )

    REQUIRED_FIELDS = ['name']

    objects = UserManager()
