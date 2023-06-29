from django.contrib import admin

from user.models import User

from django.contrib import admin

from partner.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
    )
