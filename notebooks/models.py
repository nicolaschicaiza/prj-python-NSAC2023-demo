from django.utils import timezone
from django.db import models

# Create your models here.


class Notebook(models.Model):
    name = models.CharField(max_length=50, null=False, default="name")
    code = models.CharField(max_length=50, null=False, default="code")
    path = models.CharField(max_length=255, null=False, default="path/of/file")
    create_at = models.DateField(null=False, default=timezone.now)

    def __str__(self):
        return self.name
