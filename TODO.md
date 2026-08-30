### Docker
- [X] Ler documentação da Chainguard sobre utilização das imagens Python e PostgreSQL para adequar a execução dos contêineres.
- [X] Criar Dockerfiles para o app e para o banco de dados.
- [X] Testar aplicação com os Dockerfiles do app e do banco de dados.
- [X] Empacotar app e banco de dados utilizando Docker Compose.
- [RX Testar aplicação com o Docker Compose.
- [ ] Definir forma segura para não precisar passar senha do PostgreSQL no Dockerfile
- [ ] Verificar forma mais correta de utilizar variáveis de comunicação entre o Flask e o PostgreSQL (arquivo .env)
- [ ] Adicionar healthcheck para validar comunicação entre Flask e PostgreSQL
- [ ] Adicionar tag _YY.MM.VERSION_ nas imagens, baseada na sugestão _ENVIRONMENT:YY.MM.VERSION_ de [Bhanu Teja](https://decodeops.substack.com/p/latest-tag-will-kill-your-weekend). Assim, a imagem gerada será identificada, por exemplo, como _omarciodanilo/pycpf-flask:26.1.0_
- [ ] Criar um pipeline no GitHub Actions para, a cada modificação no código, gerar como artefato as imagens Docker do Flask e PostgreSQL e enviá-las para meu Docker Hub

### GitHub Actions
- [ ] Criar pipeline para, a cada modificação no código:
  - [ ] Validar código (lint, etc.)
  - [ ] Gerar app.tar.gz
  - [ ] Subir containers
  - [ ] Validar comunicação entre containers
  - [ ] Gerar imagens dos containers
  - [ ] Verificar segurança das imagens com Trivy
  - [ ] Assinar imagens com Cosign
  - [ ] Enviar imagens para meu Docker Hub

### Código Python
- [ ] Adicionar rota health para realizar healthcheck (comunicação entre Flask e PostgreSQL)
- [ ] Usar blocos try/except: em caso de erro, logar o erro e tratar (seguir tentando ou exibir mensagem).
- [ ] Verificar motivo de não conseguir executar flask run sem o --host=0.0.0.0.

### Gerar CPF
- [X] Adicionar possibilidade de gerar múltiplos CPFs baseada em quantidade definida pelo usuário (apenas via Terminal).
- [ ] Adicionar funcionalidade de gerar arquivo para download.
    - [ ] TXT (CPFs separados por quebra de linha).
    - [ ] CSV (CPFs separados por vírgula).

### Validar CPF
- [X] Se a situação do CPF for "incorreto", exibir a UF em branco.
- [ ] Adicionar possibilidade de validar múltiplos CPFs inseridos pelo usuário, retirando pontos e hífen (apenas via Terminal).
    - [ ] Formato de lista.
    - [ ] Via upload de arquivo.
        - [ ] Arquivo TXT separado por quebra de linha.
        - [ ] Arquivo CSV separado por vírgula.
