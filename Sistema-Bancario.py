menu = """
===============================
Seja bem vindo ao Ximplous Bank
===============================

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [x] - Sair

===============================

==> """

saldo = 0
saque_diario = 0
limite = 500
transacoes = []


while True:
    opcao = input(menu)

    if opcao == "1":
        deposito_sys = float(input("Quanto gostária de depositar? R$:"))
        if deposito_sys > 0:
            saldo += deposito_sys
            transacoes.append(f"Depósito: +R$ {deposito_sys:.2f}")
            print(f"R$:{deposito_sys:.2f} foi depositado à sua conta.")
        else:
            print("Desculpe, o valor informado não pode ser depositado.")

    elif opcao == "2":
        if saque_diario < 3:
            sacar_sys = float(input("Quanto gostaria de sacar? R$:"))
            if saldo < sacar_sys:
                print("Desculpe, saldo insuficiente.")
            elif sacar_sys > 500:
                print("Desculpe, o saque maximo é de R$:500,00")
            else:
                saldo -= sacar_sys
                saque_diario += 1
                transacoes.append(f"Retirada: -R$ {sacar_sys:.2f}")
                print(f"R$:{sacar_sys:.2f} foi retirado de sua conta.")
        else:
            print("Essa conta ja atingiu o limite de saques diários.")
            
    
    elif opcao == "3":
        print("\nExtrato Ximplous Bank")
        print("-------------------------------")

        if not transacoes:
            print("Nenhuma transação até o momento.")
        else:
            for transacao in transacoes:
                print(transacao)
            print("-------------------------------")
            print(f"Seu saldo atual é de: R$:{saldo:.2f}")
            print("-------------------------------")

    elif opcao == "x":
        print("Obrigado pela preferencia!")
        break

    else:
        print("Opção inválida, tente novamente.")
