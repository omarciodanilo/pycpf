> # Nota
> Esta aplicação deve ser utilizada para fins de teste.

# Descrição

- Aplicação que gera um CPF válido ou valida um CPF inserido pelo usuário.

# Configurar ambiente

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

  `flask run`

- Acesso local e externo

  `flask run --host 0.0.0.0`

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

### Comandos úteis

#### Python/Flask

- Executar container Python ([link de apoio](https://images.chainguard.dev/directory/image/python/overview))

  ```docker container run -it -d \
  --env-file .env \
  --publish 5000:5000 \
  --network cpf-hub-network \
  --mount type=bind,source=$(pwd),target=/app \
  --user root \
  --entrypoint /bin/bash \
  --name cpf-hub-flask \
  cgr.dev/chainguard/python:latest-dev```

- Comando para criar imagem

  `docker image build -f Dockerfile-Flask -t cpf-hub-flask .`

- Comando para executar container após criação de imagem

  ```docker container run -it -d \
  --env-file .env \
  --publish 5000:5000 \
  --network cpf-hub-network \
  --name cpf-hub-flask \
  cpf-hub-flask```

#### PostgreSQL

- Comando para executar container PostgreSQL ([link de apoio](https://images.chainguard.dev/directory/image/postgres/overview))

  ```docker container run -it -d \
  --env-file .env \
  --network cpf-hub-network \
  --mount type=volume,source=cpf-hub-volume,target=/var/lib/postgresql/data \
  --name cpf-hub-postgresql \
  cgr.dev/chainguard/postgres:latest-dev```

- Comando para criar imagem

  `docker image build -f Dockerfile-PostgreSQL -t cpf-hub-postgresql .`

- Comando para executar container PostgreSQL após criação de imagem

  ```docker container run -it -d \
  --publish 5432:5432 \
  --env-file .env \
  --network cpf-hub-network \
  --mount type=volume,source=cpf-hub-volume,target=/var/lib/postgresql/data \
  --name cpf-hub-postgresql \
  cpf-hub-postgresql```