# Generated by Django 4.0.6 on 2022-08-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_roomdetails_complain_hostelblock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='complainResolveDate',
            field=models.DateField(blank=True),
        ),
    ]