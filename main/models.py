from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone  
from django.db.models import Max


class Staff(AbstractUser):
    # Extending the default User model with additional fields
    age = models.PositiveIntegerField(null=True, blank=True)  # Optional age field
    job_title = models.CharField(max_length=200)  # Job title field
    job_duties = models.TextField(blank=True)  # Optional job duties field
    phone = models.CharField(max_length=20, blank=True)  # Optional phone number, must be unique
    home_address = models.TextField(blank=True)  # Optional home address field
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
    id = models.AutoField(primary_key=True)
    def get_next_day():
        last_day = Meal.objects.aggregate(Max('day_of_month'))['day_of_month__max']
        if last_day is None:
            return 1
        return last_day + 1 if last_day < 31 else 1

    day_of_month = models.IntegerField(
        validators=[
            MinValueValidator(1, message='Day must be at least 1'),
            MaxValueValidator(31, message='Day cannot exceed 31')
        ],
        verbose_name='日號',
        default=get_next_day
    )

    breakfast_menu = models.TextField(blank=True,verbose_name='早餐')
    lunch_menu = models.TextField(blank=True,verbose_name='午餐')
    teatime_menu = models.TextField(blank=True,verbose_name='茶點')
    dinner_menu = models.TextField(blank=True,verbose_name='晚餐')

    def __str__(self):
        return f'Meal for day {self.day_of_month}'

    class Meta:
        ordering = ['day_of_month']


class Price(models.Model):
    PRODUCT_TYPES = [
        ('Bed', '床位'),
        ('Others', '其他')
    ]

    product_type = models.CharField(
        max_length=10,
        choices=PRODUCT_TYPES,
        default='Bed',
        verbose_name='類別'
    )
    description = models.TextField(
        verbose_name='描述'
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='價格'
    )

    def __str__(self):
        return f"{self.get_product_type_display()} - ${self.price}"

 