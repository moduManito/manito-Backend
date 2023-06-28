from django.db import models


class Manito(models.Model):
    class Meta:
        db_table = 'manito'
        verbose_name = 'Manito'

    author = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
    )
