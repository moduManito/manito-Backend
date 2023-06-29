from django.contrib import admin

from manito.models import Manito


@admin.register(Manito)
class ManitoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'type',
        'created_at',
        'end_at',
    )
