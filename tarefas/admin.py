from django.contrib import admin

from .models import Agendamento


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'nome', 'matricula', 'tipo', 'telefone', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'tipo', 'data')
    search_fields = ('nome', 'matricula', 'email')
    date_hierarchy = 'data'
