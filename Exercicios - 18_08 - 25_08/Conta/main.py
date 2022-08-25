from conta import ContaCorrente
import os
from time import sleep
if __name__ == "__main__":
    print('Bem Vindo!')
    sleep(1)
    print("Vamos começar fazendo o cadastro de 10 pessoas :)")
    sleep(1)
    lista_contas = []
    for i in range(10):
        numero = int(input(f'Digite o número da conta {i+1}: '))
        saldo = float(input(f'Digite o saldo da conta {i+1}: '))
        nome = input(f'Digite o nome da conta {i+1}: ')
        conta = ContaCorrente(numero, saldo, nome)
        lista_contas.append(conta)
        os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("""Opções
[1] - Depositar
[2] - Sacar
[3] - Saldo
[4] - Sair""")
        escolha = int(input('Digite sua opção: '))
        while escolha < 1 or escolha > 4:
            escolha = int(input('Tente Novamente. Digite sua escolha: '))
        s = ''
        for i in range(len(lista_contas)):
            s += str(lista_contas[i].numero) + ' '
        
        if escolha == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(s)
            conta = int(input('Para qual conta você deseja depósitar? [1-10] '))
            while conta < 1 or conta > 10:
                conta = int(input('Tente Novamente. Para qual conta você deseja depósitar? [1-10] '))
            conta -= 1
            deposito = float(input('Digite o valor do seu depósito: '))
            lista_contas[conta].depositar(deposito)

        elif escolha == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(s)
            conta = int(input('Você deseja sacar de qual conta? [1-10] '))
            while conta < 1 or conta > 10:
                conta = int(input('Tente Novamente. Você deseja sacar de qual conta? [1-10] '))
            conta -= 1
            saque = float(input('Quanto você deseja sacar? '))
            if lista_contas[conta].sacar(saque) == False:
                print("ERRO: Valor acima do seu saldo.\033[m")
            else:
                print('Saque Concluído!')

        elif escolha == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(s)
            conta = int(input('Você deseja ver o saldo de qual conta? [1-10] '))
            while conta < 1 or conta > 10:
                conta = int(input('Tente Novamente. Você deseja ver o saldo de qual conta? [1-10] '))
            conta -= 1
            print(lista_contas[conta].saldo)

        else:
            print('Obrigado por usar nosso serviço :)')
            break
