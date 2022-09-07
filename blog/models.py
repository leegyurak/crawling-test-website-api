from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=127, db_index=True)
    text = models.TextField(max_length=1023, db_index=True)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title