from rest_framework import serializers
from .models import MduUser


class MduUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MduUser
        fields = ('id', 'name', 'zip_code', 'email', 'news_preference', 'stock_preference')
