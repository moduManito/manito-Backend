from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    email = models.CharField(
        verbose_name="이메일",
        max_length=255,
    )

    name = models.CharField(
        verbose_name="이름",
        max_length=255,
    )
