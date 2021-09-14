from django.db import models

# Create your models here.
class Target(models.Model):
    target = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.target

class Issue(models.Model):
    issue = models.CharField(max_length=200, null=True,)

    def __str__(self):
        return self.issue
    


class Start(models.Model):
    start = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.start

    