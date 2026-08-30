-- Criar usuário pycpf
CREATE USER pycpf WITH PASSWORD 'pycpf';

-- Atribuir o usuário pycpf como dono do banco de dados pycpfdb
ALTER DATABASE pycpfdb OWNER TO pycpf;

-- Criar esquema para o usuário pycpf
CREATE SCHEMA IF NOT EXISTS pycpf AUTHORIZATION pycpf;

-- Definir o caminho de busca para interações futuras (para não precisar digitar pycpf.tabela)
ALTER ROLE pycpf SET search_path TO pycpf, public;

-- Definir o caminho de busca para o script atual (para não precisar digitar pycpf.logs_requisicoes no próximo passo)
SET search_path TO pycpf, public;

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

-- Garantir que o usuário pycpf seja o dono da tabela logs_requisicoes
ALTER TABLE logs_requisicoes OWNER TO pycpf;

-- Criar índice no timestamp
CREATE INDEX IF NOT EXISTS idx_logs_criado_em ON logs_requisicoes (criado_em);

-- Inserir log de sistema (Seed) para marcar que o banco foi inicializado
INSERT INTO logs_requisicoes (metodo_http, interacao, pagina, status_http, tempo_execucao) VALUES ('SYSTEM', True, 'SYSTEM', 0, 0);
