from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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



class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=100, unique=True)
    # Add other fields as needed

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Add any additional required fields here

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
