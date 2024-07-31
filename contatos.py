import os

contatos = []

def id_ajustado(id):
    id_ajustado = id - 1
    return id_ajustado

def adicionar_contato(nome_contato, telefone_contato, email_contato):
    contato = {"nome":nome_contato, "telefone":telefone_contato, "email":email_contato, "favorito":False }
    contatos.append(contato)

def lista_contatos():
    for id, contato in enumerate(contatos, start = 1):
        coracao = "❤︎" if contato["favorito"] else "♡"
        print(f"{id}- {contato["nome"]}, {contato["telefone"]}, {contato["email"]}, {coracao}")
    print("\n")

def editar_contatos(id_contato):
    if id_contato >= 0 and id_contato < len(contatos):
        opcao = (input("Oque voce deseja ajustar: 1- nome, 2- telefone, 3- email? "))
        mudanca = input("Novo: ")
        if opcao == "1":
            contatos[id_contato]["nome"] = mudanca
        elif opcao == "2":
            contatos[id_contato]["telefone"] = mudanca
        elif opcao == "3":
            contatos[id_contato]["email"] = mudanca
        else:
            print("opcao invalida")
    else:
        print("id do contato inexistente")

def alternar_favorito(id_contato):
    if id_contato >= 0 and id_contato < len(contatos):
        contatos[id_contato]["favorito"] = not contatos[id_contato]["favorito"]
    else:
        print("id do contato inexistente")
    
def lista_favoritos():
    for id, contato in enumerate(contatos, start = 1):
        if contato["favorito"]:
            coracao = "❤︎" if contato["favorito"] else "♡"
            print(f"{id}- {contato["nome"]}, {contato["telefone"]},{contato["email"], coracao}")
        else:
            print("nenhum contato favorito")

def apagar_contato(id_contato):
    if id_contato >= 0 and id_contato < len(contatos):
        for id, contato in enumerate(contatos):
            if id_contato == id:
                contatos.remove(contato)
    else:
        print("id do contato inexistente")

while True:
    print("1-Adicionar contato")
    print("2-Visualizar lista de contatos")
    print("3-Editar contato")
    print("4-Marcar/desmacar favorito")
    print("5-Contatos favoritos")
    print("6-Apagar contato")
    print("7-Sair")
    escolha_opcao = input("\nEscolha uma opcao: ")
    os.system("cls")

    if escolha_opcao == "1":
        nome_contato= input("Insira o nome do contato: ")
        numero_contato = input("Insira o numero do contato: ")
        email_contato = input("Insira o email do contato: ")
        adicionar_contato(nome_contato, numero_contato, email_contato)

    elif escolha_opcao == "2":
        lista_contatos()

    elif escolha_opcao == "3":
        lista_contatos()
        id_contato = int(input("Qual o id do contato que deseja editar? "))
        id_contato = id_ajustado(id_contato)
        editar_contatos(id_contato)

    elif escolha_opcao == "4":
        lista_contatos()
        id_contato = int(input("Qual contato voce deja alterar o favorito? "))
        id_contato = id_ajustado(id_contato)
        alternar_favorito(id_contato)

    elif escolha_opcao == "5":
        lista_favoritos()

    elif escolha_opcao == "6":
        lista_contatos()
        id_contato = int(input("Qual o id do contato que desena apagar? "))
        id_contato = id_ajustado(id_contato)
        apagar_contato(id_contato)

    elif escolha_opcao == "7":
        break

    else:
        print("Opçao invalida")


