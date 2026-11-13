from django.contrib import admin
from django.urls import path

from tarefas.views import agendar, sucesso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', agendar, name='agendar'),
    path('agendado/', sucesso, name='sucesso'),
]
