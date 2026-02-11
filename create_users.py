#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qpr_project.settings')
django.setup()

from django.contrib.auth.models import User
from qpr_app.models import UserProfile

# Create or update user 905 to be HOD Gayathri
user_905, created_905 = User.objects.get_or_create(
    username='905',
    defaults={'first_name': 'Gayathri', 'last_name': 'HOD'}
)
user_905.set_password('123456')
user_905.save()

profile_905, created_profile_905 = UserProfile.objects.get_or_create(
    user=user_905,
    defaults={
        'role': 'hod',
        'hod_name': 'gayathri',
        'name': 'Gayathri',
        'email': 'gayathri@office.gov',
        'employee_code': '905',
        'profile_updated': True
    }
)
if not created_profile_905:
    profile_905.role = 'hod'
    profile_905.hod_name = 'gayathri'
    profile_905.name = 'Gayathri'
    profile_905.email = 'gayathri@office.gov'
    profile_905.employee_code = '905'
    profile_905.profile_updated = True
    profile_905.save()

status_905 = "created" if created_905 else "updated"
print(f"✓ User 905 {status_905} - HOD Gayathri")
print(f"  Employee Code: 905")
print(f"  Password: 123456")
print(f"  Role: HOD")

# Create or update user 654 for Admin
user_654, created_654 = User.objects.get_or_create(
    username='654',
    defaults={'first_name': 'Admin', 'last_name': 'Manager'}
)
user_654.set_password('123456')
user_654.save()

profile_654, created_profile_654 = UserProfile.objects.get_or_create(
    user=user_654,
    defaults={
        'role': 'admin',
        'name': 'Admin Manager',
        'email': 'admin@office.gov',
        'employee_code': '654',
        'profile_updated': True
    }
)
if not created_profile_654:
    profile_654.role = 'admin'
    profile_654.name = 'Admin Manager'
    profile_654.email = 'admin@office.gov'
    profile_654.employee_code = '654'
    profile_654.profile_updated = True
    profile_654.save()

status_654 = "created" if created_654 else "updated"
print(f"\n✓ User 654 {status_654} - Admin/Manager")
print(f"  Employee Code: 654")
print(f"  Password: 123456")
print(f"  Role: Admin/Manager")

print("\n" + "="*50)
print("USERS CREATED/UPDATED SUCCESSFULLY!")
print("="*50)

print("\n" + "="*50)
print("USERS CREATED SUCCESSFULLY!")
print("="*50)
