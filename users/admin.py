from django.contrib import admin
from users.models import Claim, Main, Preauthorisation

# Register your models here.


admin.site.register(Main)
admin.site.register(Claim)
admin.site.register(Preauthorisation)