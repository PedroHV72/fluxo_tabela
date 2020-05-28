"""
@author: Pedro Vasconcelos
"""

armazenamento = {}
while True:

    print('-=' * 20)
    print('1 - Cadastrar')
    print('2 - Alterar')
    print('3 - Listar')
    print('4 - Excluir')
    print('5 - Finalizar')
    print('-=' * 20)

    usuario = int(input("O que você deseja fazer ? "))


    if usuario == 1 or usuario == 2:

        matricula = int(input("Digite a Matricula: "))

        nome = input("Digite o nome: ")

        idade = int(input("Digite a idade: "))

        telefone = int(input("Digite o telefone: "))

        endereço = input("Digite o endereço: ")

        str1 = "Matrícula: {}, Seu nome: {} , idade: {} , Tel: {} , End: {}".format(matricula, nome, idade, telefone, endereço)

        armazenamento[matricula] = str1

    elif usuario == 3:
        print(armazenamento)

    elif usuario == 4:
        delete = int(input("Digite a matricula que deseja excluir: "))
        armazenamento.pop(delete)

    elif usuario == 5:
        break

    else:
        print("Escolha inválida, tente novamente")