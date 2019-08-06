from django.db import models
from django.utils import timezone


# Create your models here.
class MduUser(models.Model):
    name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    news_preference = models.CharField(max_length=50)
    stock_preference = models.CharField(max_length=50)
    favorite_team = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)
