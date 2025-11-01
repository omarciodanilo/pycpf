def limpa_tela():
    """Limpa tela com base no Sistema Operacional utilizado."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
