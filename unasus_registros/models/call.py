from django.db import models
from unasus_registros.models.ubs import Ubs

class Call(models.Model):
    CALL_STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled'),
    ]
    
    ubs = models.ForeignKey(Ubs, on_delete=models.CASCADE, related_name='calls', null=True, blank=True)  # Relacionamento com UBS
    subject = models.CharField(max_length=255)  # Assunto do chamado
    description = models.TextField()  # Descrição detalhada
    status = models.CharField(max_length=50, choices=CALL_STATUS_CHOICES, default='open')  # Status do chamado
    priority = models.CharField(max_length=50)  # Prioridade do chamado
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do chamado
    updated_at = models.DateTimeField(auto_now=True)  # Data de atualização do chamado
    resolved_at = models.DateTimeField(null=True, blank=True)  # Data de resolução do chamado
    reporter_name = models.CharField(max_length=255)  # Nome da pessoa que reportou
    reporter_email = models.EmailField()  # E-mail de quem reportou

    def __str__(self):
        return f"Call {self.id} - {self.subject} ({self.status})"

    def to_dict(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "resolved_at": self.resolved_at.isoformat() if self.resolved_at else None,
            "reporter_name": self.reporter_name,
            "reporter_email": self.reporter_email,
            "ubs": self.ubs.id if self.ubs else None  # Inclui apenas o ID da UBS associada
        }
