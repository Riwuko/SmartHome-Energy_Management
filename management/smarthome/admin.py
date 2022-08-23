from django.contrib import admin

from .models import (Building, Device, EnergyDailyMeasurement, ExchangeEnergyStorageRaport, EnergyGenerator, PhotovoltaicsSufficiencyRaport, EnergyMeasurement, EnergySourcesRaport, EnergySurplusRaport, EnergySurplusLossRaport,
                     EnergyReceiver, EnergyStorage, Floor, Room)

admin.site.register(Device)
admin.site.register(Room)
admin.site.register(Floor)
admin.site.register(EnergyDailyMeasurement)
admin.site.register(EnergyMeasurement)
admin.site.register(Building)
admin.site.register(EnergyStorage)
admin.site.register(EnergyReceiver)
admin.site.register(EnergyGenerator)
admin.site.register(EnergySourcesRaport)
admin.site.register(EnergySurplusLossRaport)
admin.site.register(PhotovoltaicsSufficiencyRaport)
admin.site.register(EnergySurplusRaport)
admin.site.register(ExchangeEnergyStorageRaport)

# Register your models here.
