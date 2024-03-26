# Agenda-Django
 Projeto de uma Agenda de contatos em Django, feito em um curso de Python (Luiz Otávio Miranda) porém com mudanças por minha parte.

# Situação Atual:

Projeto Finalizado | Utiliza o POSTGRESQL

# Passo a Passo:

# 1- Ter o Python instalado em sua máquina

# 2- Criar o Ambiente Virtual:
Windows: python -m venv venv
Linux e Mac'os: python3 -m venv venv

# 3- Ativar o Ambiente Virtual:
Windows: .\venv\scripts\activate.ps1
Linux e Mac'os: source venv\bin\activate

# 4- Instalar os requirements.txt:
pip install -r requirements.txt

# 5 - Criar seu Banco de Dados no POSTGRESQL e criar a Conexão)
baixe o Postgres, salve seu usuário e senha, crie um servidor, crie um banco de dados com nome 'agendadb'
após isso vá nos settings.py e troque os dados pelos seus dados. (normalmente só é necessário trocar a senha e user)

<img width="272" alt="20240326193435" src="https://github.com/natan-ayres/Agenda-Django/assets/129100066/873b1df8-54ca-47c2-a2c4-71f36ddb88c8">


# 6- Fazer as migrações:
python manage.py makemigrations

# 7- Migrar as migrações:
python manage.py migrate

# 8- Rodar o programa:
python manage.py runserver

# Como acessar as rotas?

Ao abrir a página inicial, no cabecalho vai ter o LOGIN. 
<img width="1403" alt="20240326175045" src="https://github.com/natan-ayres/Agenda-Django/assets/129100066/22feb5b2-9797-4a21-b4e1-baed6560fbe9">

Ao clicar você vai poder fazer a sua conta de Usuário.
<img width="1409" alt="20240326175107" src="https://github.com/natan-ayres/Agenda-Django/assets/129100066/88f9b933-a9aa-4059-9079-d757b6215be5">

Coloque os dados e se atente aos requisitos de cada campo.
<img width="1395" alt="20240326175138" src="https://github.com/natan-ayres/Agenda-Django/assets/129100066/f474a4a8-9aca-4fd9-8665-540382ccb99c">

Ao voltar a página de Login e fazer o Login, você vai se deparar com seu Perfil, e agora aparecerá Criar Contato.
<img width="1399" alt="20240326175335" src="https://github.com/natan-ayres/Agenda-Django/assets/129100066/c6f395a3-c8c9-4773-aae9-d76f75347b2c">

Coloque os dados e se atente aos requisitos de cada campo.
<img width="1405" alt="20240326175356" src="https://github.com/natan-ayres/Agenda-Django/assets/129100066/8e2f2786-b5c2-4555-a8c5-2126164171cd">

Com o Contato criado, ele aparecerá na página inicial, aonde você pode clicar em seu ID.
<img width="1401" alt="20240326175454" src="https://github.com/natan-ayres/Agenda-Django/assets/129100066/25b3d381-3240-4193-8054-e49b0e111184">

Ao clicar no ID, será Redirecionado para a página do Contato.
<img width="1406" alt="20240326175434" src="https://github.com/natan-ayres/Agenda-Django/assets/129100066/1a53c009-3c24-41f3-8c1f-12022dfb0580">

# Rotas Manuais:

/contact/{id}/ (Rota de informações de um CONTATO específico)
/contact/create/ (Rota para criar CONTATOS)
/contact/{id}/update/ (Rota de atualização de CONTATO)
/contact/{id}/delete/ (Rota de delete de CONTATO)
/user/create/ (Rota de cadastro de USUÁRIOS)
/user/login/ (Rota para fazer o LOGIN)
/user/contact/ (Rota de informações de USUÁRIO)
/user/logout/ (Rota para SAIR da sessão)
/user/userupdate/ (Rota de atualização de USUÁRIO)
/user/userdelete/ (Rota de delete de USUÁRIO)

# Observações:

Contatos com o campo show desmarcado/false, NÃO vão aparecer na pagina inicial, de contato ou na update, somente no banco de dados.
Caso entrar em páginas restritas a usuários logados/contatos existentes, você vai ser redirecionado para outra página, Contatos só podem ser criado por Usuário.
Contatos só podem ser editados ou apagados pelo usuário que fez eles.





