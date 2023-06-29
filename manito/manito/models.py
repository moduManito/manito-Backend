from django.db import models
from user.models import User


class Manito(models.Model):
    MANITO_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
    )

    class Meta:
        db_table = 'manito'
        verbose_name = 'Manito'

    title = models.CharField(
        verbose_name="제목",
        max_length=255,
    )

    author = models.ForeignKey(
        User,
        verbose_name="마니또 만든 이",
        on_delete=models.CASCADE,
    )

    type = models.CharField(
        verbose_name="마니또 타입",
        choices=MANITO_CHOICES,
        max_length=255,
    )

    content = models.TextField(
        verbose_name="메일에 넣을 내용",
    )

    price = models.PositiveIntegerField(
        verbose_name="선물 금액",
    )

    mail_data = models.TextField(
        verbose_name="참가자 메일",
    )

    name_data = models.TextField(
        verbose_name="참가자 이름",
    )

    created_at = models.DateTimeField(
        verbose_name="생성날",
        auto_now_add=True,
    )

    end_at = models.DateTimeField(
        verbose_name="마감날",
        null=True,
    )

    def __str__(self):
        return self.title
