from django.db import models
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