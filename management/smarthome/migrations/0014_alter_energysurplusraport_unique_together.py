# Generated by Django 3.2.13 on 2022-06-24 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0013_alter_energysurplusraport_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='energysurplusraport',
            unique_together={('building', 'date_time', 'usage_type')},
        ),
    ]