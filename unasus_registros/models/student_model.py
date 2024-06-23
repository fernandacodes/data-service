from django.db import models

class Student(models.Model):
    CPF = models.CharField(max_length=11, unique=True)
    Name = models.CharField(max_length=255)  # Alterado de 'Nome' para 'Name'
    Email = models.CharField(max_length=255, unique=True)
    Phone = models.CharField(max_length=255)  # Alterado de 'Telefone' para 'Phone'
    Municipality = models.CharField(max_length=255)  # Alterado de 'Municipio' para 'Municipality'
    State = models.CharField(max_length=255)  # Alterado de 'UF' para 'State'
    Status = models.CharField(max_length=255)  # Alterado de 'Situacao' para 'Status'
    Cycle = models.CharField(max_length=255)  # Alterado de 'Ciclo' para 'Cycle'
    List = models.CharField(max_length=255)  # Alterado de 'Lista' para 'List'
    DSEI = models.BooleanField(default=False)
    EnrollmentNumber = models.CharField(max_length=255)  # Alterado de 'Matricula' para 'EnrollmentNumber'
    TutorClass = models.CharField(max_length=255)  # Alterado de 'TurmaTutor' para 'TutorClass'
    Date = models.CharField(max_length=255)   # Mantido, mas você pode querer renomear para 'BirthDate' ou similar
    Condition = models.CharField(max_length=255)  # Alterado de 'Condição' para 'Condition'
    RequestChangeDate = models.DateField(null=True, blank=True)  # Alterado de 'DataSolicitacaoMudanca' para 'RequestChangeDate'
    
    def to_dict(self):
        return {
            "CPF": self.CPF,
            "Name": self.Name,
            "Email": self.Email,
            "Phone": self.Phone,
            "Municipality": self.Municipality,
            "State": self.State,
            "Status": self.Status,
            "Cycle": self.Cycle,
            "List": self.List,
            "DSEI": self.DSEI,
            "EnrollmentNumber": self.EnrollmentNumber,
            "TutorClass": self.TutorClass,
            "Date": self.Date,
            "Condition": self.Condition,
            "RequestChangeDate": self.RequestChangeDate,
        }
