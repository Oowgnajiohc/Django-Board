from django.db import models

class Post(models.Model):
    nickname = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nickname} - {self.created_at.strftime("%Y-%m-%d")}'