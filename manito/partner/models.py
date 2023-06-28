from django.db import models

from manito.models import Manito
from user.models import User


class Partner(models.Model):
    class Meta:
        db_table = 'partner'
        verbose_name = 'Partner'

    manito = models.ForeignKey(
        Manito,
        verbose_name="마니또",
        on_delete=models.CASCADE,
    )

    manito_sender = models.ForeignKey(
        User,
        verbose_name="보내는 사람",
        on_delete=models.CASCADE,
        related_name='sender'
    )

    manito_receiver = models.ForeignKey(
        User,
        verbose_name="받는 사람",
        on_delete=models.CASCADE,
        related_name='receiver',
    )
