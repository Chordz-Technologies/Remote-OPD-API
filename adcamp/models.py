from django.db import models


class ADCamp(models.Model):
    srno = models.AutoField(db_column='SrNo', primary_key=True)  # Field name made lowercase.
    village = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=60, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    standard = models.CharField(max_length=45, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    hb = models.DecimalField(db_column='HB', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    villagename = models.CharField(db_column='villageName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hbreadings = models.CharField(db_column='HBReadings', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bmi = models.DecimalField(db_column='BMI', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bmireadings = models.CharField(db_column='BMIReadings', max_length=100, blank=True, null=True)  # Field name made lowercase.
    client_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adcamp'
