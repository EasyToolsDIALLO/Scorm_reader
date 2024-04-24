from django.db import models

# Create your models here.


class MyScormModel(models.Model):
    file = models.FileField(upload_to='scorms/')
