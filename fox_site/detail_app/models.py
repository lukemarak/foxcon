# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    CLIENT_NAME = (
        ('','----Select Customer----'),
        ('Foxconn','Foxconn India Pvt. Ltd'),
        ('Rising Stars','Rising Stars Mobile India pvt ltd.'),
    )
    name = models.CharField(max_length=100, choices=CLIENT_NAME)

    PROCESSOR = (
        ('','----Select Processor----'),
        ('i7-6700@3.4','i7-6700@3.40GHz.'),
        ('i7-4790@4.6','i7-4790@4.60GHz.'),
    )
    processor = models.CharField(max_length=100, choices=PROCESSOR)

    ipc_510 = models.CharField(max_length=100)
    aimb_705G2 = models.CharField(max_length=100)
    hdd_1TB = models.CharField(max_length=100)
    ddr4_8GB = models.CharField(max_length=100)
    hdd_BAY = models.CharField(max_length=100)
    win7_KEY = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    date = models.DateField()
    extras = models.TextField()
    ENGINEER = (
		('', '----Select Name-----'),
		('Luke', 'LUKE MARAK'),
		('Mukesh', 'MUKESH GAUTAM'),
		('Gobala', 'A.GOBALAKRISHNAN'),
		('Venkatesh', 'R.VENKATESH'),
		('Tokho', 'TOKHO'),
		('Balaji', 'BALAJI'),
		('Mani', 'MANIKANDAN'),
		('Santosh', 'SANTOSH'),

	)
    assembled_by = models.CharField(max_length=20, choices=ENGINEER)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name','processor','ipc_510','aimb_705G2','hdd_1TB','ddr4_8GB','hdd_BAY','win7_KEY','quantity','date','assembled_by',)
        unique_together = ('ipc_510','aimb_705G2','hdd_1TB','ddr4_8GB','hdd_BAY','win7_KEY',)
