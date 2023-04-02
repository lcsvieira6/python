menu = """
### BEM VINDO ###

[d] Depositar
[s] Sacar
[e] Extrato
[a] Saldo
[q] Sair

==> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    print()

    if opcao == "d":
        valor = float(input("Informe o Valor do Depósito: "))
        print()
               
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {saldo:.2f}\n"            
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso !")

        else:
            print("Depósito não realizado. O valor informado é inválido. ")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        print()

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente. ")
        
        elif excedeu_limite:
            print("Operação falhou. O valor do saque excede o limite diário. ")

        elif excedeu_saques:
            print("Operação falhou. Numero de saques excedidos.\n Tente novamente amanhã, ou procure a agência mais próxima. ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso! ")
        else:
            print("Operação falhou. O valor informado é inválido")

    elif opcao == "e":
        print("################## EXTRATO ##################")
        print("Não foram realizadas nenhuma movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("#############################################")

    elif opcao == "a":
        print("################ SALDO #############")
        print(f"O saldo disponível é de R$ {saldo:.2f}")
        print("####################################")
    
    elif opcao == "q":
        print("Operação Finalizada. ")
        print()
        print("Volte Sempre!")
        print()
        break

    else:
        print("Opção inválida!\nTente novamente. ")
    



    

