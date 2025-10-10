# === CAIXA ELETRÔNICO COM FUNÇÕES ===

def exibir_menu():
    print("\n=== MENU DO CAIXA ELETRÔNICO ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Ver histórico de transações")
    print("5 - Sair")

def depositar(saldo, historico):
    valor = float(input("Digite o valor do depósito: R$"))
    if valor > 0:
        saldo += valor
        historico.append(f"Depósito de R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! O depósito deve ser maior que zero.")
    return saldo

def sacar(saldo, historico):
    valor = float(input("Digite o valor do saque: R$"))
    if valor > 0:
        if valor <= saldo:
            saldo -= valor
            historico.append(f"Saque de R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Valor inválido! O saque deve ser maior que zero.")
    return saldo

def ver_saldo(saldo):
    print(f"Seu saldo atual é de R${saldo:.2f}")

def ver_historico(historico):
    print("\n=== HISTÓRICO DE TRANSAÇÕES ===")
    if len(historico) == 0:
        print("Nenhuma transação registrada.")
    else:
        for transacao in historico:
            print(transacao)

def main():
    saldo = 1000.00
    historico = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo = depositar(saldo, historico)
        elif opcao == "2":
            saldo = sacar(saldo, historico)
        elif opcao == "3":
            ver_saldo(saldo)
        elif opcao == "4":
            ver_historico(historico)
        elif opcao == "5":
            print("Obrigado por usar o caixa eletrônico. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
main()