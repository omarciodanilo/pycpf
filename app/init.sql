-- Criar usuário cpf-hub
CREATE USER "cpf-hub" WITH PASSWORD 'cpf-hub';

-- Atribuir o usuário cpf-hub como dono do banco de dados cpf-hub-db
ALTER DATABASE "cpf-hub-db" OWNER TO "cpf-hub";

-- Criar esquema para o usuário cpf-hub
CREATE SCHEMA IF NOT EXISTS "cpf-hub" AUTHORIZATION "cpf-hub";

-- Definir o caminho de busca para interações futuras (para não precisar digitar cpf-hub.tabela)
ALTER ROLE "cpf-hub" SET search_path TO "cpf-hub", public;

-- Definir o caminho de busca para o script atual (para não precisar digitar cpf-hub.logs_requisicoes no próximo passo)
SET search_path TO "cpf-hub", public;

-- Criar a tabela logs_requisicoes
CREATE TABLE logs_requisicoes (
    id SERIAL PRIMARY KEY,
    criado_em TIMESTAMPTZ DEFAULT NOW(),
    metodo_http VARCHAR(10),
    interacao BOOLEAN,
    pagina VARCHAR(20),
    status_http INTEGER,
    tempo_execucao REAL
);

-- Garantir que o usuário cpf-hub seja o dono da tabela logs_requisicoes
ALTER TABLE logs_requisicoes OWNER TO "cpf-hub";

-- Criar índice no timestamp
CREATE INDEX IF NOT EXISTS idx_logs_criado_em ON logs_requisicoes (criado_em);

-- Inserir log de sistema (Seed) para marcar que o banco foi inicializado
INSERT INTO logs_requisicoes (metodo_http, interacao, pagina, status_http, tempo_execucao) VALUES ('SYSTEM', True, 'SYSTEM', 0, 0);