from django.contrib import admin
from .models import User,Event,ExecutiveBody,OperatingBody,Faculty
# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(ExecutiveBody)
admin.site.register(OperatingBody)
admin.site.register(Faculty)

