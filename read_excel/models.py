from django.db import models
# from django.contrib.auth.models import User


class Iap(models.Model):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    order_id = models.IntegerField(max_length=100, null=False)
    purchase_id = models.IntegerField(max_length=100, null=False)
    csm_name = models.CharField(max_length=100, null=False)
    serial = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=False)
    macaddr = models.CharField(max_length=100, null=False)
    

    def __str__(self):
        return self.site_name
