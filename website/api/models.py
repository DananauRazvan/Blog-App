from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
