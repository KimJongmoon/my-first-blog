from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.ImageField(null = True)
    filtered_image = models.ImageField(null = True)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True, null = True)

    def publish(self):
        self.save()
