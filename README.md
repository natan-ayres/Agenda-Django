# Agenda-Django
 Projeto de uma Agenda de contatos em Django, feito em um curso de Python (Luiz Otávio Miranda) porém com mudanças por minha parte.

# Situação Atual:

Projeto Funcionando com Login e Autenticação, porém ainda falta adcionar algumas coisas, Banco de Dados ainda o padrão de Django

# Como acessar as rotas?

No topo do página, tem o Criar Contato, ao clicar vai ser redirecionado para a página de criação, após criar seu contato(pode-se criar vários) será redirecionado a página principal, aonde lá aparece o seu contato criado, ao clicar no seu ID, entrará em uma página com as informações do contato e opção de ATUALIZAR e DELETAR, aonde o ATUALIZAR levará a uma página para atualização.

No topo terá a opção de LOGIN, aonde redirecionará para uma página que caso você ainda não tenha uma conta, você poderá clicar em Cadastrar Usuário, nisso após cadastrado você terá que fazer o Login, após isso, ao olhar para o cabeçalho da página, verá que visitante se tornou o seu nome de usuário, aonde ao clicar você vai entrar em uma página com suas informações, opção de ATUALIZAR os dados e de DELETAR a conta, ao olhar para o cabeçario novamente também verá que LOGIN se tornou LOGOUT, aonde ao clicar você vai sair da sessão.

# Rotas Manuais:

/contact/{id}/ (Rota de informações de um CONTATO específico)
/contact/create/ (Rota para criar CONTATOS)
/contact/{id}/update/ (Rota de atualização de CONTATO)
/contact/{id}/delete/ (Rota de delete de CONTATO)
/user/create/ (Rota de cadastro de USUÁRIOS)
/user/login/ (Rota para fazer o LOGIN)
/user/contact/ (Rota de informações de USUÁRIO)
/user/logout/ (Rota para SAIR da sessão)

# Observações:

Contatos com o campo show desmarcado/false, NÃO vão aparecer na pagina inicial, de contato ou na update, somente no banco de dados.
Caso entrar em páginas restritas a usuários logados/contatos existentes, você vai ser redirecionado para outra página.

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



