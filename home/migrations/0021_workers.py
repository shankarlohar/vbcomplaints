# Generated by Django 4.0.6 on 2022-08-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_complainfields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerName', models.CharField(max_length=100)),
                ('workerField', models.CharField(max_length=100)),
            ],
        ),
    ]
