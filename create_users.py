#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qpr_project.settings')
django.setup()

from django.contrib.auth.models import User
from qpr_app.models import UserProfile

# Update user 905 to be HOD Gayathri
try:
    user_905 = User.objects.get(username='905')
    user_905.set_password('123456')
    user_905.save()
    
    profile_905 = UserProfile.objects.get(user=user_905)
    profile_905.role = 'hod'
    profile_905.hod_name = 'gayathri'
    profile_905.name = 'Gayathri'
    profile_905.email = 'gayathri@office.gov'
    profile_905.profile_updated = True
    profile_905.save()
    
    print("✓ User 905 updated to HOD Gayathri")
    print(f"  Employee Code: 905")
    print(f"  Password: 123456")
    print(f"  Role: HOD")
except User.DoesNotExist:
    print("User 905 not found")

# Create or update user 654 for Admin
try:
    user_654 = User.objects.get(username='654')
    user_654.set_password('123456')
    user_654.save()
    
    # Check if profile exists
    try:
        profile_654 = UserProfile.objects.get(user=user_654)
        profile_654.employee_code = '654'
        profile_654.role = 'admin'
        profile_654.name = 'Admin Manager'
        profile_654.email = 'admin@office.gov'
        profile_654.profile_updated = True
        profile_654.save()
        print("\n✓ User 654 updated to Admin/Manager")
    except UserProfile.DoesNotExist:
        profile_654 = UserProfile.objects.create(
            user=user_654,
            employee_code='654',
            role='admin',
            name='Admin Manager',
            email='admin@office.gov',
            profile_updated=True
        )
        print("\n✓ User 654 created as Admin/Manager")
    
    print(f"  Employee Code: 654")
    print(f"  Password: 123456")
    print(f"  Role: Admin/Manager")
except User.DoesNotExist:
    # Create new user 654
    user_654 = User.objects.create_user(
        username='654',
        password='123456'
    )
    
    profile_654 = UserProfile.objects.create(
        user=user_654,
        employee_code='654',
        role='admin',
        name='Admin Manager',
        email='admin@office.gov',
        profile_updated=True
    )
    
    print("\n✓ User 654 created as Admin/Manager")
    print(f"  Employee Code: 654")
    print(f"  Password: 123456")
    print(f"  Role: Admin/Manager")

print("\n" + "="*50)
print("USERS CREATED SUCCESSFULLY!")
print("="*50)
