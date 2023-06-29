from django.contrib import admin

from partner.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'manito',
        'manito_sender',
        'manito_receiver'
    )
