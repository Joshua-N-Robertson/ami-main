from django.db import models

# Create your models here.


class Main(models.Model):
    relationship = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    mobilephone = models.CharField(max_length=50)
    employer = models.CharField(max_length=100)
    plans = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    membernumber = models.CharField(max_length=50, primary_key=True, default=None)
    dateprinted = models.DateField()
    exiteddate = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.membernumber
    

    class Meta:
        db_table = 'main'



class Claim(models.Model):
    systemclaimno = models.CharField(max_length=50)
    membernumber = models.CharField(max_length=50, primary_key=True, default=None) #using primary key to prevent id error
    description = models.TextField()
    type = models.CharField(max_length=50)
    amt = models.DecimalField(max_digits=10, decimal_places=2)
    rejected = models.CharField(max_length=5)
    reason = models.CharField(max_length=100)
    time = models.TimeField()    
    hsp = models.CharField(max_length=100)
    ailment = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    batchno = models.CharField(max_length=50)

    def __str__(self):
        return self.systemclaimno
    
    class Meta:
        db_table = 'claim'


class Inpatient_limit(models.Model):
    membernumber = models.CharField(max_length=50, primary_key=True, default=None)
    startdate = models.DateField()
    status = models.CharField(max_length=50)
    mobilephone = models.CharField(max_length=50)
    employer = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    plans = models.CharField(max_length=100)
    total_claims = models.CharField(max_length=100)
    type_of_visit = models.CharField(max_length=100)
    amt = models.DecimalField(max_digits=10, decimal_places=2)
    per_usage = models.IntegerField()

    def __str__(self):
        return self.type_of_visit
    
    class Meta:
        db_table = 'Inpatient limit'

class Outpatient_limit(models.Model):
    membernumber = models.CharField(max_length=50, primary_key=True, default=None)
    startdate = models.DateField()
    status = models.CharField(max_length=50)
    mobilephone = models.CharField(max_length=50)
    employer = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    plans = models.CharField(max_length=100)
    total_claims = models.CharField(max_length=100)
    type_of_visit = models.CharField(max_length=100)
    amt = models.DecimalField(max_digits=10, decimal_places=2)
    per_usage = models.IntegerField()

    def __str__(self):
        return self.type_of_visit
    
    class Meta:
        db_table = 'Outpatient limit'

class Preauthorisation(models.Model):
    acode = models.CharField(max_length=12)
    adate = models.DateField()
    membernumber = models.CharField(max_length=50, primary_key=True, default=None)
    chistory = models.CharField(max_length=50)
    ptype = models.CharField(max_length=50)
    amt = models.DecimalField(max_digits=10, decimal_places=2)
    hsp = models.CharField(max_length=100)
    auser = models.CharField(max_length=50)

    class Meta:
        db_table ='preauthorisation'


class Caps_benefits(models.Model):
    caps = models.CharField(max_length=15)
    amt = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    iplan = models.CharField(max_length=33)
    comp = models.CharField(max_length=33, primary_key=True, default=None)
    sdate = models.DateField()
    prem = models.IntegerField()
    status = models.CharField(max_length=50)
    byear = models.CharField(max_length=4)
    updatecomp = models.CharField(max_length=33)

    class Meta:
        db_table ='caps_benefits'