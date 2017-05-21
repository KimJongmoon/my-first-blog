from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.ImageField(null = True, upload_to = 'photos/%Y/%m/%d/origin')
    filtered_image = models.ImageField(null = True, upload_to = 'photos/%Y/%m/%d/filtered')
    text = models.TextField(null = True, blank = True)
    published_date = models.DateTimeField(auto_now_add = True, null = True)

    def publish(self):
        self.save()

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Post, self).delete(*args, **kwargs)
