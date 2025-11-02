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
[X] Adicionar possibilidade de gerar múltiplos CPFs baseada em quantidade definida pelo usuário.
[ ] Adicionar funcionalidade de gerar arquivo para download.
    [ ] TXT (CPFs separados por quebra de linha).
    [ ] CSV (CPFs separados por vírgula).
[ ] Adicionar funcionalidade de gerar um CPF para UF definida pelo usuário.

### Validar CPF
[X] Se a situação do CPF for "inválido", não exibir a UF.
[ ] Adicionar possibilidade de validar múltiplos CPFs inseridos pelo usuário (retirar pontos e hífen) em formato de lista.
[ ] Adicionar funcionalidade de validar múltiplos CPFs via upload de arquivo (retirar pontos e hífen).
    [ ] Arquivo TXT separado por quebra de linha.
    [ ] Arquivo CSV separado por vírgula.
