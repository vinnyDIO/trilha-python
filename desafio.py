# O objetivo é criar uma lógica Bancária - sistema de banco, onde tem saldo, depósito, retirada, limite
# implementar operações
# Terei um menu com escolha

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def new_func():
    opcao = input('informe a opcao desejada:\n d)Deposito \n s)Saque \n e)Extrato \n q)Sair ')
    return opcao

while True:
    opcao = new_func()

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do deposito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("O valor informado é inválido.")
        print("Deposito: ",valor_deposito)
        print("Saldo: ",saldo)
    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Informe o valor do Saque: "))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques =  numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! VocÊ não tem saldo suficiente")
        
        elif excedeu_limite:
            print("Operacao falhou! o valor do saque excede o limite.")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques +=1
        else:
            print("Operação falhou! o valor informado é invalido")
       
    elif opcao == "e":
        print("\n==================Extrato==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")

