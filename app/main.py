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
        qtd = 1
        dict_cpf = {}
        item = 0
        if escolha == "1":
            print("1 - GERAR CPF\n")
            qtd = int(input("Insira a quantidade de CPFs para gerar: "))

            for item in range(qtd):
                cpf = gera_cpf()
                while cpf.count(cpf[0]) == 11:
                    cpf = gera_cpf()
                situacao = "válido"
                uf = verifica_uf(cpf[8])
                dict_cpf[item] = [cpf,situacao,uf]
        else:
            print("2 - VALIDAR CPF\n")
            cpf = input("Insira o CPF para validação (apenas números): ")
            print()

            if verifica_cpf(cpf):
                primeiro_dv = calcula_dv(cpf, 10)
                segundo_dv = calcula_dv(cpf, 11)
                situacao = compara_dv(cpf, primeiro_dv, segundo_dv)
                if situacao == "válido":
                    uf = verifica_uf(cpf[8])
                else:
                    uf = "não se aplica"
            else:
                situacao = "inválido"
                uf = "não se aplica"
            dict_cpf[item] = [cpf,situacao,uf]

        print()
        for i in range(qtd):
            print(f"CPF      : { converte_cpf(dict_cpf[item][0]) }")
            print(f"SITUAÇÂO : { dict_cpf[item][1] }")
            print(f"UF       : { dict_cpf[item][2] }\n")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
