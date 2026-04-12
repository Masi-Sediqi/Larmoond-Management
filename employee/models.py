from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ROLE_CHOICES = [
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('manager', 'Manager'),
        ('qa', 'QA'),
        ('hr', 'HR'),
        ('other', 'Other'),
    ]

    # 🔹 معلومات شخصی
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    # 🔹 معلومات کاری
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='developer')
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    join_date = models.DateField(blank=True, null=True)

    # 🔹 عکس
    image = models.ImageField(upload_to='employees/', blank=True, null=True)

    # 🔹 وضعیت
    is_active = models.BooleanField(default=True)

    # 🔹 timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()