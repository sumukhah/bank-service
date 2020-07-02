from django.db import models


class Banks(models.Model):
    name = models.CharField(max_length=49, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True,)

    def __str__(self):
        return self.name

    class Meta:
        # managed = False
        verbose_name = ["bank"]
        verbose_name_plural = "banks"
        db_table = 'banks'


class Branches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank = models.ForeignKey(Banks, models.DO_NOTHING,
                             related_name='banks', blank=True, null=True, )
    branch = models.CharField(max_length=74, blank=True, null=True)
    address = models.CharField(max_length=195, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)

    state = models.CharField(max_length=26, blank=True, null=True)

    def __str__(self):
        return self.branch + ', ' + self.ifsc

    class Meta:
        verbose_name = 'branch'
        verbose_name_plural = "branches"
        # managed = False
        db_table = 'branches'
