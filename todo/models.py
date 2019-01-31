from django.db import models


class TodoItem(models.Model):
    content = models.TextField()


class PogChamp(models.Model):
    name = models.TextField()
    rank = models.IntegerField()
