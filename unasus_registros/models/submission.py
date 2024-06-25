from django.core.exceptions import ValidationError
from django.db import models
from ..models.student_model import Student

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    term_accepted = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3)
    rh_factor = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    race = models.CharField(max_length=20)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    birth_city = models.CharField(max_length=50)
    birth_state = models.CharField(max_length=2)
    birth_country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    marital_status = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    rg_number = models.CharField(max_length=20)
    rg_issuer = models.CharField(max_length=50)
    rg_state = models.CharField(max_length=2)
    document = models.FileField(upload_to='documents/')
    high_school_graduation_year = models.CharField(max_length=4)
    university_name = models.CharField(max_length=100)
    work_city = models.CharField(max_length=50)
    work_state = models.CharField(max_length=2)
    address = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=100)
    address_complement = models.CharField(max_length=255, null=True, blank=True)
    address_city = models.CharField(max_length=50)
    address_state = models.CharField(max_length=2)
    address_zip_code = models.CharField(max_length=10)
    indigenous_ethnicity = models.CharField(max_length=50, null=True, blank=True)
    disability = models.BooleanField(default=False)
    disability_degree = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.student.Name}"

    def clean(self):
        # Verifica se já existe uma submissão para o estudante
        if Submission.objects.filter(student=self.student).exists():
            raise ValidationError('Student has already submitted')

    def save(self, *args, **kwargs):
        # Chama o método clean antes de salvar
        self.clean()
        super().save(*args, **kwargs)
