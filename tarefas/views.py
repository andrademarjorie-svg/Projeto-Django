from django.db import IntegrityError
from django.shortcuts import redirect, render

from .forms import AgendamentoForm
from .models import Agendamento


def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            try:
                agendamento = form.save()
            except IntegrityError:
                # Duas pessoas tentaram o mesmo horário ao mesmo tempo.
                form.add_error('horario', 'Este horário acabou de ser reservado. Escolha outro.')
            else:
                # Guarda só o número do agendamento na sessão do próprio aluno.
                request.session['ultimo_agendamento'] = agendamento.pk
                return redirect('sucesso')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento.html', {'form': form})


def sucesso(request):
    pk = request.session.get('ultimo_agendamento')
    agendamento = Agendamento.objects.filter(pk=pk).first() if pk else None
    if agendamento is None:
        return redirect('agendar')
    return render(request, 'sucesso.html', {'agendamento': agendamento})
