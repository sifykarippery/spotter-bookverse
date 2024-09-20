from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        db_table = "authors"

    def __str__(self):
        return self.name
