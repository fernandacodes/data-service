from django.core.exceptions import ValidationError
from django.db import models
from ..models.student_model import Student

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    term_accepted = models.BooleanField(default=False)
    
    # Form fields in English
    birthplace = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField()
    marital_status = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=10)
    rh_factor = models.CharField(max_length=5)
    ethnicity = models.CharField(max_length=50, null=True, blank=True)
    physical_disability = models.BooleanField(default=False)
    disability_details = models.CharField(max_length=100, null=True, blank=True)
    disability_degree = models.CharField(max_length=50, null=True, blank=True)
    psychological_disorder = models.CharField(max_length=100, null=True, blank=True)
    street_address = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=100, null=True, blank=True)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=10)
    rg = models.CharField(max_length=20)
    birth_city = models.CharField(max_length=100)
    birth_state = models.CharField(max_length=2)
    high_school_graduation_year = models.CharField(max_length=4)
    university_name = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=4)
    graduation_course = models.CharField(max_length=100)
    current_ubs_name = models.CharField(max_length=100)
    ubs_type = models.CharField(max_length=50)
    
    # Fields for PDF documents stored in MongoDB
    rg_cpf_copy = models.FileField(upload_to='documents/rg_cpf/', null=True, blank=True)
    reservista_cert_copy = models.FileField(upload_to='documents/reservista_cert/', null=True, blank=True)
    diploma_copy = models.FileField(upload_to='documents/diploma/', null=True, blank=True)
    marriage_certificate_copy = models.FileField(upload_to='documents/marriage_certificate/', null=True, blank=True)
    address_proof_copy = models.FileField(upload_to='documents/address_proof/', null=True, blank=True)
    residence_internet_copy = models.FileField(upload_to='documents/residence_internet/', null=True, blank=True)
    ubs_internet_copy = models.FileField(upload_to='documents/ubs_internet/', null=True, blank=True)
    
    # Additional fields for internet and energy
    internet_speed = models.CharField(max_length=10, null=True, blank=True)
    internet_availability = models.CharField(max_length=50, null=True, blank=True)
    energy_availability = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Submission by {self.student.full_name}"

    def clean(self):
        # Check if there is already a submission for the student
        if Submission.objects.filter(student=self.student).exists():
            raise ValidationError('Student has already submitted')

    def save(self, *args, **kwargs):
        # Call the clean method before saving
        self.clean()
        super().save(*args, **kwargs)
