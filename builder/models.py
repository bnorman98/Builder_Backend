from django.db import models
from users.models import CustomUser

class Plan(models.Model):
    time = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner')
    title = models.TextField(default='Basic_Full_Body')
    description = models.TextField(default='Causes migrate')
    location = models.TextField()
    subscribers = models.ManyToManyField(CustomUser)
    experience_level = models.IntegerField(default=0)
    class Meta:
        ordering = ['created']