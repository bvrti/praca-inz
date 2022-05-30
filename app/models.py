from django.db import models
from datetime import datetime
# Create your models here.

class Setting(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(editable=False)
    description = models.TextField()
    value = models.TextField()
    class Meta:
        #for permissions that don't really relate to a particular model, and I don't want to programmatically create them.
        permissions = [
            ("Operator", "Can report malfunction"),
        ]

class machine(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    description = models.TextField()

class malfunction(models.Model):
    machine_name = models.CharField(max_length=6)
    description = models.TextField()
    status = models.CharField(max_length=20, default="Pending")
    responsible_person = models.CharField(max_length=50, default="")
    date = models.DateTimeField(auto_now_add=True, blank=True)
