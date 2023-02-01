from django.contrib import admin
from . import models


admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.TypeOfWork)
admin.site.register(models.Loyalty)
admin.site.register(models.StatusOrder)

