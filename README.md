## Descrição

Aplicação que gera um CPF válido ou valida um CPF inserido pelo usuário.

For non-brazilians readers:
- Python application that generates a valid CPF or validates an inserted CPF by the user.
- [CPF is a document that identifies a taxpayer at the Federal Internal Revenue Department, and carries registration information supplied by the individual and by the Federal Internal Revenue Department database.](https://thebrazilbusiness.com/qa/what-is-cpf)

### Aviso importante: esta aplicação deve ser utilizada para fins de teste de software.

## Configuração do ambiente

### Banco de Dados

- Versão testada: 18
- Comandos para configuração do PostgreSQL:

  - Instalar postgresql-common

  `sudo apt install -y postgresql-common`

  - Adicionar repositório do PostgreSQL

  `sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh`

  - Atualizar lista de repositórios do Ubuntu

  `sudo apt update`

  - Instalar PostgreSQL 18

  `sudo apt install -y postgresql-18`

  - Logar como usuário postgres

  `sudo -u postgres psql`

  - Criar senha para o usuário postgres

  `\password postgres`

- Comando para configuração do banco de dados (dentro do repositório pycpf clonado):

  `psql -U postgres -f init.sql`

### Python

- Versão testada: 3.10.12
- Comandos para configuração (dentro do repositório pycpf clonado):
  
  `python3 -m venv .venv`
  
  `python3 -m pip install -r requirements.txt`

### App

- Comando para inicialização permitindo acesso local:

  `flask --app app/main.py run`

- Comando para inicialização permitindo acesso externo:

  `flask --app app/main.py run --host 0.0.0.0`
