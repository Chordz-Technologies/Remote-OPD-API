from django.db import models

# Create your models here.
class Medicines(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicines'
