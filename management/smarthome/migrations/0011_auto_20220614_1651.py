# Generated by Django 3.2.13 on 2022-06-14 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0010_building_use_exchange_energy'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='energysourcesraport',
            unique_together={('building', 'date_time_from')},
        ),
        migrations.AlterUniqueTogether(
            name='energysurpluslossraport',
            unique_together={('building', 'date_time')},
        ),
        migrations.AlterUniqueTogether(
            name='energysurplusraport',
            unique_together={('building', 'date_time')},
        ),
        migrations.AlterUniqueTogether(
            name='exchangeenergystorageraport',
            unique_together={('building', 'date_time_from')},
        ),
        migrations.AlterUniqueTogether(
            name='photovoltaicssufficiencyraport',
            unique_together={('building', 'date_time')},
        ),
    ]
