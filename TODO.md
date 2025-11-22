### Geral
- [X] Migrar funções do arquivo gera_e_valida_cpf.py para novos locais:
	- [X] Função main para o arquivo app/main.py.
	- [X] Demais funções para arquivos individuais, dentro do diretório pycpf (arquivos cpf.py e utils.py).
		- [X] verifica_cpf
		- [X] calcula_dv
		- [X] compara_dv
		- [X] converte_cpf
		- [X] verifica_uf
		- [X] gera_cpf
		- [X] limpa_tela
- [X] Configurar Flask para migrar o app para Web.
- [X] Adicionar ao arquivo requirements.txt os pacotes necessários para configurar o app.
- [ ] Empacotar app no Docker.

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
