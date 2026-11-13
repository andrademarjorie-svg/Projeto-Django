import datetime

from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone

from .models import Agendamento


class AgendamentoForm(forms.ModelForm):
    matricula = forms.CharField(
        label='Matrícula',
        max_length=14,
        validators=[RegexValidator(r'^\d{10,14}$', 'Digite apenas números (de 10 a 14 dígitos).')],
        widget=forms.TextInput(attrs={'inputmode': 'numeric', 'placeholder': 'Somente números'}),
    )
    telefone = forms.CharField(
        label='Telefone / WhatsApp',
        max_length=15,
        validators=[RegexValidator(r'^\d{10,11}$', 'Digite DDD + número, só números. Ex.: 84999998888')],
        widget=forms.TextInput(attrs={'inputmode': 'tel', 'placeholder': 'DDD + número'}),
    )

    class Meta:
        model = Agendamento
        fields = [
            'nome', 'matricula', 'curso', 'email', 'telefone',
            'tipo', 'data', 'horario', 'observacoes',
        ]
        widgets = {
            'curso': forms.TextInput(attrs={'placeholder': 'Ex.: Técnico em Informática - 3º ano'}),
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        amanha = timezone.localdate() + datetime.timedelta(days=1)
        self.fields['data'].widget.attrs['min'] = amanha.isoformat()
        self.fields['tipo'].choices = [('', 'Selecione...')] + list(Agendamento.TIPOS)
        self.fields['horario'].choices = [('', 'Selecione...')] + list(Agendamento.HORARIOS)

    def clean_data(self):
        data = self.cleaned_data['data']
        if data <= timezone.localdate():
            raise forms.ValidationError('Escolha uma data a partir de amanhã.')
        if data.weekday() >= 5:
            raise forms.ValidationError('O atendimento é de segunda a sexta-feira.')
        return data

    def clean(self):
        cleaned = super().clean()
        data = cleaned.get('data')
        horario = cleaned.get('horario')
        if data and horario:
            ocupado = (
                Agendamento.objects
                .filter(data=data, horario=horario)
                .exclude(status='cancelado')
                .exists()
            )
            if ocupado:
                self.add_error('horario', 'Este horário já está reservado. Escolha outro horário ou outra data.')
        return cleaned
