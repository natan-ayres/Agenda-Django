# Agenda-Django
 Projeto de uma Agenda de contatos em Django, feito em um curso de Python (Luiz Otávio Miranda) porém com mudanças por minha parte.

# Situação Atual:

Projeto Finalizado | Utiliza o DB do Django

# Como acessar as rotas?

Ao abrir a página inicial, no cabecalho vai ter o LOGIN, aonde ao clicar você vai poder fazer a sua conta de Usuário, após criar, vai ter a opção de entrar no seu perfil e ATUALIZAR ou DELETAR sua conta se necessário, também se olhar no cabecalho terá a opção de criar contato, aonde poderá fazer contatos, após isso aparecerá na sua página principal o novo contato cadastrado, se clicar no ID dele, vai entrar na página de informações do contato, aonde poderá ATUALIZAR e DELETAR o contato se necessário, também pode ver que no cabeçalho invês do LOGIN agora terá LOGOUT e se clicar na AGENDA volta para a página inicial.

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

