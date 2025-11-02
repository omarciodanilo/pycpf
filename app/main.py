# imports do Python
import sys

# import dos módulos do projeto
from pycpf import limpa_tela, converte_cpf, gera_cpf, verifica_cpf, calcula_dv, compara_dv, verifica_uf

def main():

    """Solicita informações ao usuário e retorna saída na tela."""

    limpa_tela()
    
    print("GERADOR E VALIDADOR DE CPF")
    print("\nO que você deseja:\n  1. Gerar um CPF válido\n  2. Validar um CPF\n  OBS: para sair, pressione qualquer outra tecla")
    escolha = input("\nEscolha: ")

    if escolha in ("1", "2"):
        limpa_tela()
        if escolha == "1":
            cpf = gera_cpf()

            while cpf.count(cpf[0]) == 11:
                cpf = gera_cpf()

            print("1 - GERAR CPF\n")
            situacao = "válido"
            uf = verifica_uf(str(cpf[8]))
        else:
            print("2 - VALIDAR CPF\n")
            cpf = input("Insira o CPF para validação (apenas números): ")

            print()
            if verifica_cpf(cpf):
                primeiro_dv = calcula_dv(cpf, 10)
                segundo_dv = calcula_dv(cpf, 11)
                situacao = compara_dv(cpf, primeiro_dv, segundo_dv)
                uf = verifica_uf(str(cpf[8]))
            else:
                situacao = uf = "inválido"

        print(f"CPF      : { converte_cpf(cpf) }")
        print(f"SITUAÇÃO : { situacao }")
        print(f"UF       : { uf }")
        print()
    else:
        sys.exit()

if __name__ == "__main__":
    main()
