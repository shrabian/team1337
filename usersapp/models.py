from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
num_messages_displayed = 10

user = get_user_model()

class Text(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(user, related_name = 'author', on_delete =  models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.author.username

    def last_x_messages(self):
        return Text.objects.order_by('-timestamp').all()[:num_messages_displayed]
