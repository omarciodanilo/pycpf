### Geral
[X] Migrar funções do arquivo gera_e_valida_cpf.py para novos locais:
    [X] Função main para o arquivo app/main.py.
    [X] Demais funções para arquivos individuais, dentro do diretório pycpf (arquivos cpf.py e utils.py).
        [X] verifica_cpf
	[X] calcula_dv
	[X] compara_dv
	[X] converte_cpf
	[X] verifica_uf
	[X] gera_cpf
	[X] limpa_tela
[ ] Empacotar app no Docker.
[ ] Configurar Flask para migrar o app para Web.
[ ] Adicionar ao arquivo requirements.txt os pacotes necessários para configurar o app.

### Gerar CPF
[ ] Adicionar funcionalidade de gerar múltiplos CPFs baseada em quantidade definida pelo usuário.
[ ] Adicionar funcionalidade de gerar um CPF para UF definida pelo usuário.

### Validar CPF
[ ] Ao inserir um CPF inválido, não exibir a linha UF. Exibir apenas as linhas CPF e Situação.
