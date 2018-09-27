from django.db import models


class LdaModel(models.Model):
    filename = models.CharField(unique=True, max_length=1000)
    creation_date = models.DateField(auto_now=True)
    newest = models.BooleanField(default=True, null=False)
    in_use = models.BooleanField(default=False, null=False)


class TrainingStatus(models.Model):
    is_training = models.BooleanField(default=False, null=False)
