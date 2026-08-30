> # Nota
> Esta aplicação deve ser utilizada para fins de teste.

# Descrição

- Aplicação que gera um CPF válido ou valida um CPF inserido pelo usuário.

# Configurar ambiente

## Versões testadas

- Sistemas Operacionais: `Ubuntu 22.04 LTS`, `Ubuntu 24.04 LTS`
- PostgreSQL: `18`
- Python: `3.10.12`
- Flask: `XYZ`
- Docker: `XYZ`

## Ambiente sem Docker

### PostgreSQL

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

  `\password <senha>`

- Configurar o banco de dados (dentro do repositório cpf-hub clonado):

  `psql -U postgres -f init.sql`

  > OBS: será solicitada a senha do usuário postgres

### Python/Flask

- Iniciar ambiente virtual Python (dentro do repositório cpf-hub clonado):
  
  `python3 -m venv .venv`

- Ativar ambiente virtual

  `source .venv/bin/activate`

- Instalar pré-requisitos
  
  `python3 -m pip install -r requirements.txt`

### Variáveis de ambiente

- Copiar o arquivo `.env.template` e editar no `.env` a variável `DB_HOST` para `localhost`

  `cp .env.template .env`

### Executar aplicação

- Apenas acesso local

  `flask --app app/main.py run`

- Acesso local e externo

  `flask --app app/main.py run --host 0.0.0.0`

- Encerrar aplicação

  `Ctrl + C`

## Ambiente com Docker

### Docker

- Instalar o Docker Engine

  - [Ambiente de testes](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)
  - [Ambiente de produção](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

### Variáveis de ambiente

- Copiar o arquivo `.env.template`

  `cp .env.template .env`

### Executar aplicação

- Subir os contêineres (API Flask + PostgreSQL)

  `docker compose up -d --build`

- Encerrar aplicação

  `docker compose down`