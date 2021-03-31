from django.db import models

class post(models.Model):
    titel=models.CharField(max_length=150)
    desc=models.TextField()
    username=models.CharField(max_length=100,blank=True)
