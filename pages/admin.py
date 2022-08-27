from django.contrib import admin

# Register your models here.
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('name','MU','csv')

admin.site.register(Data,DataAdmin)