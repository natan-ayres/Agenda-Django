# Agenda-Django
 Projeto de uma Agenda de contatos em Django, feito em um curso de Python (Luiz Otávio Miranda) porém com mudanças por minha parte.

# Situação Atual:

Utilizando SQLite, sem login e sem auth.

# Como acessar as rotas?

No topo do página, tem o Criar Usuário, ao clicar vai ser redirecionado para a página de criação, após criar seu úsuario(pode-se criar vários) será redirecionado para a página de atualização aonde poderá atualizar o úsuario recem criado, ao clicar em AGENDA, será redirecionado para a página principal, aonde com o contato já criado, poderá ao clicar no seu ID, entrar em uma página com as informações do usuário.

# Rotas Manuais:

/contact/{id} (Rota de informações de um usuário específico)
/contact/create (Rota para criar usuários)
/contact/{id}/update (Rota de atualização de usuário)

# Observações:

Usuários com o campo show desmarcado/false, NÃO vão aparecer na pagina inicial, de usuário ou na update.

# Passo a Passo para testes:

# 1- Ter o Python instalado em sua máquina

# 2- Criar o Ambiente Virtual:
Windows: python -m venv venv
Linux e Mac'os: python3 -m venv venv

# 3- Ativar o Ambiente Virtual:
Windows: .\venv\scripts\activate.ps1
Linux e Mac'os: source venv\bin\activate

# 4- Instalar os requirements.txt:
pip install -r requirements.txt

# 5- Fazer as migrações:
python manage.py makemigrations

# 6- Migrar as migrações:
python manage.py migrate

# 7- Rodar o programa:
python manage.py runserver



