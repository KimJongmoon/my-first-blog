from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.ImageField()
    filtered_image = models.ImageField();
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)

    def publish(self):
        self.save()
