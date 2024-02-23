from django.db import models
import os

# Create your models here.


class Userregister(models.Model):
    user_name = models.CharField(null=True, max_length=50)
    user_email = models.EmailField(null=True)
    user_contact = models.CharField(null=True, max_length=10)
    user_address = models.CharField(null=True, max_length=100)
    user_password = models.CharField(null=True, max_length=50)
    registered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(null=True, max_length=20, default="pending")

    class Meta:
        db_table = "Userregister"


class Uploadfiles(models.Model):
    user_email = models.CharField(max_length=50, null=True)
    inputfilename = models.CharField(max_length=50, null=True)
    filename = models.CharField(max_length=50, null=True)
    uploadeddate = models.DateTimeField(auto_now_add=True)
    hashcodeone = models.TextField(null=True)
    hashcodetwo = models.TextField(null=True)
    hashcodethree = models.TextField(null=True)
    hashcodefour = models.TextField(null=True)
    keyone = models.TextField(null=True)
    keytwo = models.TextField(null=True)
    keythree = models.TextField(null=True)
    keyfour = models.TextField(null=True)

    class Meta:
        db_table = "Uploadfiles"


class Auditrequest(models.Model):
    useremail = models.EmailField(null=True)
    fileid = models.CharField(max_length=20, null=True)
    filename = models.CharField(max_length=20, null=True)
    requested_date = models.DateTimeField(auto_now_add=True)
    proofcheck = models.CharField(null=True, max_length=20, default="waiting")
    status = models.CharField(null=True, max_length=20, default="waiting")

    class Meta:
        db_table = "Auditrequest"
