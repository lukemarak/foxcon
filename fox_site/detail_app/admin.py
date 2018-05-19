# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','processor','ipc_510','aimb_705G2','hdd_1TB','ddr4_8GB','hdd_BAY','win7_KEY','quantity','date','assembled_by']
    search_fields = ['name', 'ipc_510', 'aimb_705G2']
    list_filter = ['name', 'date', 'assembled_by']
admin.site.register(Customer, CustomerAdmin)
