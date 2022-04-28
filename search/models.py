from tabnanny import verbose
from django.db import models


class Candidate(models.Model):
    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'My Candidates'

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=15)
    job = models.CharField(max_length=200)

    def __str__(self):
        return self.name
