from django.db import models

# Create your models here.

class recordOfInvention(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)
    name_of_invention = models.CharField(max_length=20, default="")
    problem_it_solves = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name_of_invention