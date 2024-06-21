from django.db import models

from..models.student_model import Student

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term_accepted = models.BooleanField(default=False)
    guardian_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    rg_number = models.CharField(max_length=20)
    rg_issuer = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    university = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    total_score = models.CharField(max_length=10)
    partial_score = models.CharField(max_length=10, null=True, blank=True)
    document = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.student.Name}"

    