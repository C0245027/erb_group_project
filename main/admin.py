from django.contrib import admin
# Register your models here. 
from .models import Staff, Meal

admin.site.register(Staff)
admin.site.register(Meal)
