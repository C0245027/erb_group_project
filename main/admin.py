from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import Staff, Meal

admin.site.register(Meal)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'job_title', 'phone', 'hire_date', 'staff_type')
    search_fields = ('username', 'job_title', 'phone')


 
