# Agendamento de Atendimento – Assistência Estudantil 

Sistema web para solicitar e organizar agendamentos de atendimento da Assistência Estudantil / Serviço Social do IFRN – Campus SGA.

## Descrição

Este projeto é uma aplicação web feita com Django. Nela, o estudante preenche um formulário online para pedir um horário de atendimento, e a equipe da Assistência Estudantil acompanha e gerencia esses pedidos em um painel administrativo.

O sistema busca resolver a organização dos atendimentos: cada pedido fica registrado em um só lugar e o mesmo horário não pode ser reservado por duas pessoas.

## Objetivos

- Permitir que o estudante solicite um atendimento de forma simples, pela internet.
- Evitar conflitos de horário, impedindo dois agendamentos no mesmo dia e horário.
- Centralizar os pedidos em um painel, para que a equipe consulte, filtre e atualize a situação de cada um.
- Praticar o desenvolvimento web com Django, banco de dados e controle de versão com Git e GitHub.
- Facilitar o atendimento, pois não tem essa opção pelo suap 

## Funcionalidades

### Disponíveis

- **Formulário de agendamento** com nome completo, matrícula, curso e turma, e-mail, telefone/WhatsApp, tipo de atendimento, data, horário e observações.
- **Validação dos dados** no envio:
  - a data deve ser a partir do dia seguinte, de segunda a sexta-feira;
  - o horário não pode já estar reservado para aquele dia;
  - a matrícula deve ter apenas números 
  - o telefone deve ter DDD e número (10 ou 11 dígitos).
- **Liberação de horário:** quando um agendamento é marcado como cancelado, o horário volta a ficar disponível.
- **Página de confirmação** com o número do protocolo e o resumo do agendamento.
- **Painel administrativo** (`/admin`) para a equipe, com listagem dos agendamentos, filtros por situação, tipo e data, busca por nome, matrícula ou e-mail, e alteração da situação (pendente, confirmado, realizado ou cancelado).

Os horários de atendimento (08h–11h e 14h–16h) e os tipos de atendimento podem ser alterados em `tarefas/models.py`.

### Ainda não disponíveis

- Consulta do agendamento pelo próprio estudante.
- Cancelamento do agendamento pelo estudante.
- Envio de confirmação por e-mail ou WhatsApp.
- Login para estudantes.

## Tecnologias utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem de programação |
| Django 6.1 | Framework web (rotas, formulários, administração) |
| SQLite | Banco de dados |
| python-dotenv | Leitura de variáveis de ambiente (arquivo `.env`) |
| HTML e CSS | Páginas e estilo da interface |
| Git e GitHub | Controle de versão e hospedagem do código |
| Visual Studio Code | Editor de código |

As bibliotecas Python e suas versões estão listadas em `requirements.txt`.

## Pré-requisitos

- **Python 3.12 ou superior** (testado com 3.12 e 3.13). Para conferir: `python --version`.
- **Git**, para baixar o projeto.
- Um terminal (PowerShell, Prompt de Comando, Terminal do Linux ou macOS) ou o terminal integrado do VS Code.

## Instalação e execução

Os comandos abaixo são para o **Windows (PowerShell)**. No final há as diferenças para Linux e macOS.

### 1. Baixar o projeto

```bash
git clone https://github.com/<usuario>/Projeto-Django.git
cd Projeto-Django
```

> Troque `<usuario>` pelo nome da conta ou organização dona do repositório no GitHub.

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

Quando estiver ativo, aparece `(venv)` no início da linha do terminal.

> Se o PowerShell bloquear a execução de scripts, rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e tente ativar de novo.

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a chave secreta (recomendado)

Crie o arquivo `setup/.env` com o conteúdo:

```
SECRET_KEY=coloque-aqui-uma-chave-longa-e-aleatoria
```

Para gerar uma chave:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

O arquivo `.env` não é enviado ao GitHub. Se ele não existir, o projeto usa uma chave provisória de desenvolvimento, que **não deve ser usada em produção**.

### 5. Criar as tabelas do banco de dados

```bash
python manage.py migrate
```

### 6. Criar um usuário administrador

```bash
python manage.py createsuperuser
```

O comando pede nome de usuário, e-mail e senha. Esse login dá acesso ao painel da equipe.

### 7. Iniciar o servidor

```bash
python manage.py runserver
```


## Estrutura do projeto

```
Projeto-Django/
├── manage.py            # Comandos do Django (runserver, migrate, ...)
├── requirements.txt     # Dependências do projeto
├── setup/               # Configurações do projeto
│   ├── settings.py      # Configurações gerais
│   ├── urls.py          # Rotas principais
│   └── .env             # Variáveis de ambiente (não vai ao GitHub)
├── tarefas/             # Aplicação de agendamento
│   ├── models.py        # Modelo Agendamento (campos, horários, tipos)
│   ├── forms.py         # Formulário e validações
│   ├── views.py         # Lógica das páginas
│   ├── admin.py         # Configuração do painel administrativo
│   └── migrations/      # Histórico de alterações do banco
└── templates/           # Páginas HTML
    ├── base.html        # Layout e estilo comuns
    ├── agendamento.html # Formulário de agendamento
    └── sucesso.html     # Confirmação do agendamento
```

> O app chama-se `tarefas` porque esse foi o nome dado no início do projeto. Ele contém todo o sistema de agendamento.

## Equipe

| Integrante 
|---|---|
| [ Alice laila] | 
| Marjorie Cecilia | 


**Instituição:** Instituto Federal do Rio Grande do Norte (IFRN) – Campus SGA
