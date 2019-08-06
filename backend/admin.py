from django.contrib import admin
from .models import MduUser


class MduUserList(admin.ModelAdmin):
    list_display = ('id', 'name', 'zip_code', 'email', 'news_preference', 'stock_preference', 'favorite_team')
    list_filter = ('id', 'name', 'zip_code', 'email', 'news_preference', 'stock_preference', 'favorite_team')
    search_fields = ('id', 'name', 'zip_code', 'email', 'news_preference', 'stock_preference', 'favorite_team')
    ordering = ['id']


admin.site.register(MduUser, MduUserList)
