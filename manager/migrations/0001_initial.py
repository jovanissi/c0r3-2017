# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-03 12:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank_accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=70)),
                ('account_number', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=70)),
                ('date_of_opening', models.DateField(default=datetime.datetime.now)),
                ('proof_of_creation', models.FileField(default='null', upload_to='uploads/Accounts_proofs')),
            ],
        ),
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('account_name', models.CharField(blank=True, max_length=30)),
                ('account_number', models.CharField(blank=True, max_length=30)),
                ('trans_type', models.CharField(blank=True, choices=[('out_trans', 'out_trans'), ('in_trans', 'in_trans')], max_length=20)),
                ('depositor_type', models.CharField(blank=True, choices=[('other', 'other'), ('shareholder', 'shareholder')], max_length=30)),
                ('depositor_name', models.CharField(blank=True, max_length=50)),
                ('contribution_months', models.CharField(blank=True, max_length=200)),
                ('reference', models.IntegerField(blank=True, default=0)),
                ('categories', models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Unapproved', 'Unapproved')], default='Pending', max_length=30)),
                ('classifications', models.CharField(blank=True, choices=[('Cheque', 'Cheque'), ('Cash', 'Cash')], default='Cash', max_length=30)),
                ('cheque_number', models.CharField(blank=True, default='null', max_length=50)),
                ('cheque_bank', models.CharField(blank=True, default='null', max_length=80)),
                ('slip_number', models.CharField(blank=True, default='null', max_length=50)),
                ('trans_comment', models.TextField(blank=True)),
                ('money_in', models.IntegerField(blank=True, default=0)),
                ('money_out', models.IntegerField(blank=True, default=0)),
                ('transaction_proof', models.FileField(blank=True, default='null', upload_to='uploads/transaction proofs')),
            ],
        ),
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Surname', models.CharField(max_length=50)),
                ('Occupied_post', models.CharField(max_length=20)),
                ('Birth_date', models.DateField()),
                ('National_ID', models.CharField(max_length=50)),
                ('E_mail', models.CharField(blank=True, max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=100)),
                ('User_picture', models.FileField(upload_to='uploads/User_profile_pictures')),
            ],
        ),
    ]
