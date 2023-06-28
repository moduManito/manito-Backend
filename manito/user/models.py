from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


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


class User(AbstractBaseUser, PermissionsMixin):
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

    is_superuser = models.BooleanField(
        default=False,
    )

    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.name
