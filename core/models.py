from django.db import models


class Summoner(models.Model):

    accountId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
