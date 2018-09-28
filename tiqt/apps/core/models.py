from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    pass


class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Secretaria(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Setor(models.Model):

    class Meta:
        verbose_name_plural = 'Setores'

    nome = models.CharField(max_length=50)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + ' - ' + self.secretaria.sigla


class Ticket(models.Model):
    ABERTO = 0
    EM_ATENDIMENTO = 1
    ENCERRADO = 2
    CANCELADO = 3

    STATUS = (
        (ABERTO, 'Aberto'),
        (EM_ATENDIMENTO, 'Em atendimento'),
        (ENCERRADO, 'Encerrado'),
        (CANCELADO, 'Cancelado')
    )

    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    responsavel = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, related_name='responsavel_por')
    criado_em = models.DateTimeField(auto_now=True)
    iniciado_em = models.DateTimeField(null=True, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    status = models.SmallIntegerField(choices=STATUS, default=ABERTO)
    patrimonio = models.CharField(max_length=5)

    class Meta:
        ordering = ["-criado_em"]

    def iniciar_atendimento(self, user):
        self.responsavel = user
        self.status = self.EM_ATENDIMENTO
        self.iniciado_em = timezone.localtime()
        self.save()

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse("ticket_detail", kwargs={"pk": self.pk})


class Comentario(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)
    texto = models.TextField()
