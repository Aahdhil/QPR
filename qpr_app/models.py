from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Extended user profile for storing additional information"""
    ROLE_CHOICES = [
        ('user', 'User'),
        ('hod', 'HOD'),
        ('admin', 'Admin/Manager'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    employee_code = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    hod_name = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    office_name = models.CharField(max_length=255, blank=True, null=True)
    office_code = models.CharField(max_length=50, blank=True, null=True)
    profile_updated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.employee_code} - {self.role}"
    
    class Meta:
        ordering = ['-id']


class ManagerRequest(models.Model):
    """Stores requests from HOD to Manager for profile/QPR updates"""
    REQUEST_TYPE_CHOICES = [
        ('profile', 'Profile Update'),
        ('qpr', 'QPR Update'),
        ('both', 'Both Profile and QPR'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    hod = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_requests_sent')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_requests_received')
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.hod.profile.employee_code} -> {self.user.profile.employee_code}"
    
    class Meta:
        ordering = ['-created_at']


class QPRRecord(models.Model):
    """Main QPR Record - stores header information"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qpr_records', null=True, blank=True)
    officeName = models.CharField(max_length=255)
    officeCode = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    quarter = models.CharField(max_length=50)
    year = models.CharField(max_length=20, default='2025-2026', null=True, blank=True)  # Fiscal year (e.g., 2025-2026)
    status = models.CharField(max_length=50, default='Draft')
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_submitted = models.BooleanField(default=False)  # To freeze after submission
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.officeName} - {self.quarter}"

    class Meta:
        ordering = ['-id']


class Section1FilesData(models.Model):
    """Section 1: Details of Files Sent To The Minister"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section1')
    total_files = models.IntegerField(null=True, blank=True)
    hindi_files = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 1 - {self.qpr_record}"


class Section2MeetingsData(models.Model):
    """Section 2: Secretary/Equivalent level meetings and files"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section2')
    meetings_count = models.IntegerField(null=True, blank=True)
    hindi_minutes = models.IntegerField(null=True, blank=True)
    total_papers = models.IntegerField(null=True, blank=True)
    hindi_papers = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 2 - {self.qpr_record}"


class Section3OfficialLanguagesData(models.Model):
    """Section 3: Documents under Official Languages Act 1963 Section 3(3)"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section3')
    total_documents = models.IntegerField(null=True, blank=True)
    bilingual_documents = models.IntegerField(null=True, blank=True)
    english_only_documents = models.IntegerField(null=True, blank=True)
    hindi_only_documents = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 3 - {self.qpr_record}"


class Section4HindiLettersData(models.Model):
    """Section 4: Letters received in Hindi (Official Language Rule-5)"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section4')
    total_letters = models.IntegerField(null=True, blank=True)
    no_reply_letters = models.IntegerField(null=True, blank=True)
    replied_hindi_letters = models.IntegerField(null=True, blank=True)
    replied_english_letters = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 4 - {self.qpr_record}"


class Section5EnglishRepliedHindiData(models.Model):
    """Section 5: English letters replied in Hindi (Region A & B)"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section5')
    # Region A data
    region_a_english_letters = models.IntegerField(null=True, blank=True)
    region_a_replied_hindi = models.IntegerField(null=True, blank=True)
    region_a_replied_english = models.IntegerField(null=True, blank=True)
    region_a_no_reply = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 5 - {self.qpr_record}"


class Section6IssuedLettersData(models.Model):
    """Section 6: Details of letters issued to different regions"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section6')
    # Region A
    region_a_hindi_bilingual = models.IntegerField(null=True, blank=True)
    region_a_english_only = models.IntegerField(null=True, blank=True)
    region_a_total = models.IntegerField(null=True, blank=True)
    # Region B
    region_b_hindi_bilingual = models.IntegerField(null=True, blank=True)
    region_b_english_only = models.IntegerField(null=True, blank=True)
    region_b_total = models.IntegerField(null=True, blank=True)
    # Region C
    region_c_hindi_bilingual = models.IntegerField(null=True, blank=True)
    region_c_english_only = models.IntegerField(null=True, blank=True)
    region_c_total = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 6 - {self.qpr_record}"


class Section7NotingsData(models.Model):
    """Section 7: Details of notings on files/documents during quarter"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section7')
    hindi_pages = models.IntegerField(null=True, blank=True)
    english_pages = models.IntegerField(null=True, blank=True)
    total_pages = models.IntegerField(null=True, blank=True)
    eoffice_notings = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 7 - {self.qpr_record}"


class Section8WorkshopsData(models.Model):
    """Section 8: Hindi workshops conducted in the quarter"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section8')
    full_day_workshops = models.IntegerField(null=True, blank=True)
    officers_trained = models.IntegerField(null=True, blank=True)
    employees_trained = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 8 - {self.qpr_record}"


class Section9ImplementationCommitteeData(models.Model):
    """Section 9: Official Language Implementation Committee meeting"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section9')
    meeting_date = models.DateField(null=True, blank=True)
    sub_committees_count = models.IntegerField(null=True, blank=True)
    meetings_organized = models.IntegerField(null=True, blank=True)
    agenda_hindi = models.CharField(max_length=10, null=True, blank=True)  # Yes/No
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 9 - {self.qpr_record}"


class Section10HindiAdvisoryData(models.Model):
    """Section 10: Hindi Advisory Committee meeting date"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section10')
    meeting_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 10 - {self.qpr_record}"


class Section11SpecificAchievementsData(models.Model):
    """Section 11: Specific achievements during the quarter"""
    qpr_record = models.OneToOneField(QPRRecord, on_delete=models.CASCADE, related_name='section11')
    innovative_work = models.TextField(blank=True, null=True)
    special_events = models.TextField(blank=True, null=True)
    hindi_medium_works = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Section 11 - {self.qpr_record}"