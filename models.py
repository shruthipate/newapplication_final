from django.db import models

class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def get_short_description(self):
        return self.title[:50] + "..." if len(self.title) > 50 else self.title

    def get_absolute_url(self):
        return self.url
