from django.db import models


class Partner(models.Model):
    class Meta:
        db_table = 'partner'
        verbose_name = 'Partner'

    sender = models.ForeignKey(
        'user.User',
        verbose_name="보내는 사람",
        on_delete=models.CASCADE
    )

    receiver = models.ForeignKey(
        'user.User',
        verbose_name="받는 사람",
        on_delete=models.CASCADE
    )
