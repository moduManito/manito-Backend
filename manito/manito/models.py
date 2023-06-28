from django.db import models
from user.models import User


class Manito(models.Model):
    class Meta:
        db_table = 'manito'
        verbose_name = 'Manito'

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
