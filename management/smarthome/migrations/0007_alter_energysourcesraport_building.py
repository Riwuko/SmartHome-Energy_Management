# Generated by Django 3.2.13 on 2022-05-31 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0006_auto_20220527_2334_squashed_0009_auto_20220528_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energysourcesraport',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_energy_sources_raports', to='smarthome.building'),
        ),
    ]