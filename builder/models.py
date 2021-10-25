from django.db import models



class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(default='user')
    #TODO: typo
    experience_level = models.IntegerField(default=0)
    is_trainer = models.BooleanField(default=True)
    class Meta:
        ordering = ['created']

class Plan(models.Model):
    #TODO: change to models.DateTimeField()
    time = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(default='Basic_Full_Body')
    description = models.TextField(default='lorem ipsum')
    #TODO: implement google maps API
    place = models.TextField()
    class Meta:
        ordering = ['created']

