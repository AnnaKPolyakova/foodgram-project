from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import Follow


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)
    search_fields = ('user', 'author',)
    empty_value_display = '-пусто-'


# admin.site.unregister(Group)
admin.site.register(Follow, FollowAdmin)