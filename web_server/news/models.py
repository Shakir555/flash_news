from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    url = models.URLField()
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
