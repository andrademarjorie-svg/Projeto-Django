from django.db import models
from django.db.models import Q


class Agendamento(models.Model):
    TIPOS = [
        ('auxilio', 'Auxílios e programas da Assistência Estudantil'),
        ('social', 'Atendimento / orientação do Serviço Social'),
        ('acompanhamento', 'Acompanhamento socioeconômico'),
        ('documentos', 'Entrega ou dúvidas sobre documentação'),
        ('outro', 'Outro assunto'),
    ]

    # Horários de atendimento. Para mudar, é só editar esta lista.
    HORARIOS = [
        ('08:00', '08h00'),
        ('09:00', '09h00'),
        ('10:00', '10h00'),
        ('11:00', '11h00'),
        ('14:00', '14h00'),
        ('15:00', '15h00'),
        ('16:00', '16h00'),
    ]

    STATUS = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    ]

    nome = models.CharField('Nome completo', max_length=150)
    matricula = models.CharField('Matrícula', max_length=14)
    curso = models.CharField('Curso e turma', max_length=100)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone / WhatsApp', max_length=15)
    tipo = models.CharField('Tipo de atendimento', max_length=20, choices=TIPOS)
    data = models.DateField('Data desejada')
    horario = models.CharField('Horário', max_length=5, choices=HORARIOS)
    observacoes = models.TextField('Observações (opcional)', blank=True)
    status = models.CharField(max_length=12, choices=STATUS, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data', 'horario']
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        constraints = [
            # Impede dois agendamentos (não cancelados) no mesmo dia e horário.
            models.UniqueConstraint(
                fields=['data', 'horario'],
                condition=~Q(status='cancelado'),
                name='horario_unico_por_dia',
            ),
        ]

    def __str__(self):
        return f'{self.nome} - {self.data:%d/%m/%Y} {self.horario}'

    @property
    def protocolo(self):
        return f'{self.pk:05d}'
