from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import Staff, Meal, Price

admin.site.register(Meal)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'job_title', 'phone', 'hire_date', 'staff_type')
    search_fields = ('username', 'job_title', 'phone')


class PriceAdmin(admin.ModelAdmin):
    list_display = ['product_type', 'description', 'price']
    list_filter = ['product_type']
    search_fields = ['description']
    list_per_page = 20
    ordering = ['product_type', 'price']
    
    fieldsets = (
        ('基本資料', {
            'fields': ('product_type', 'description', 'price')
        }),
    )

admin.site.register(Price, PriceAdmin)


 
