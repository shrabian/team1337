from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Break(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    break_start = models.TimeField().auto_now_add
    bio = models.CharField(max_length = 200, default = "", primary_key = True)