from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone

class Staff(AbstractUser):
    # Extending the default User model with additional fields
    age = models.PositiveIntegerField(null=True, blank=True)  # Optional age field
    job_title = models.CharField(max_length=200)  # Job title field
    job_duties = models.TextField(blank=True)  # Optional job duties field
    phone = models.CharField(max_length=20, blank=True, unique=True)  # Optional phone number, must be unique
    home_address = models.CharField(max_length=200, blank=True)  # Optional home address field
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  # Optional photo upload
    hire_date = models.DateTimeField(default=timezone.now, blank=True)  # Hire date with default to now
    
    STAFF_TYPE_CHOICES = [
        ('General', 'General'),
        ('Specialist', 'Specialist'),
    ]
    staff_type = models.CharField(max_length=10, choices=STAFF_TYPE_CHOICES, default='General')  # Staff type choices

    # Adding related_name to avoid clashes with the default User model
    groups = models.ManyToManyField(
        Group,
        related_name='staff_groups',  # Unique related name for groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='staff_user_permissions',  # Unique related name for user permissions
        blank=True
    )

    class Meta:
        db_table = 'staff'  # Set the database table name to 'staff'
        verbose_name = 'Staff'  # Singular name in admin
        verbose_name_plural = 'Staff'  # Plural name in admin

    def __str__(self):
        return self.username  # Returns the username of the user


class Meal(models.Model):
    setup_date = models.DateField(
        default=timezone.now, 
        verbose_name='Meal Date'  # Add this line
    )
    breakfast_menu = models.TextField(blank=True)  # Optional breakfast menu
    lunch_menu = models.TextField(blank=True)  # Optional lunch menu
    teatime_menu = models.TextField(blank=True)  # Optional teatime menu
    dinner_menu = models.TextField(blank=True)  # Optional dinner menu
  
    def __str__(self):
        return f'Meal setup on {self.setup_date}'  # Correct: returns meal setup date and user
