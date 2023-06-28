from django.db import models
from user.models import User


class Partner(models.Model):
    class Meta:
        db_table = 'partner'
        verbose_name = 'Partner'

    sender = models.ForeignKey(
        User,
        verbose_name="보내는 사람",
        on_delete=models.CASCADE,
        related_name='sender'
    )

    receiver = models.ForeignKey(
        User,
        verbose_name="받는 사람",
        on_delete=models.CASCADE,
        related_name='receiver',
    )
