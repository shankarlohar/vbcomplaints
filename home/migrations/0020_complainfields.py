# Generated by Django 4.0.6 on 2022-08-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_complain_complainresolvedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='complainFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complainFields', models.CharField(max_length=122)),
            ],
        ),
    ]