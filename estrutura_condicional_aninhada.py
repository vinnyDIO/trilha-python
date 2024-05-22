#Esse arquivo visa mostrar a utilização das estruturas: if, elif e else
#utilização do input e int

conta_normal = 1
conta_universitaria = 2
conta_especial = 3

saldo = 2000
saque = int(input("Informe o valor do saque: "))
conta = int(input("Escolha sua conta: 1-Conta Normal, 2-Conta Universitária, 3-Conta Especial "))

cheque_especial = 450

if conta_normal==conta:
    print("Conta normal selecionada!")
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria==conta:
    print("Conta universitária selecionada!")
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial==conta:
    print("Conta especial selecionada!")
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")