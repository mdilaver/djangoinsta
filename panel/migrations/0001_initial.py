# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alici',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kullanici_id', models.CharField(max_length=50)),
                ('kullanici_adi', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('ad_soyad', models.CharField(max_length=100)),
                ('sifre', models.CharField(max_length=150)),
                ('web_site', models.CharField(max_length=80)),
                ('token_key', models.CharField(max_length=255)),
                ('son_giris', models.DateTimeField()),
                ('ip_adres', models.IPAddressField()),
                ('kayit_tarih', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Satici',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kullanici_id', models.CharField(max_length=50)),
                ('kullanici_adi', models.CharField(max_length=50)),
                ('magaza_adi', models.CharField(max_length=50)),
                ('aciklama', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('ad_soyad', models.CharField(max_length=100)),
                ('sifre', models.CharField(max_length=150)),
                ('web_site', models.CharField(max_length=80)),
                ('token_key', models.CharField(max_length=255)),
                ('son_giris', models.DateTimeField()),
                ('ip_adres', models.IPAddressField()),
                ('kayit_tarih', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
