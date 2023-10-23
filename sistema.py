menu = """
[D] Depósito
[S] Sacar
[E] Extrato
[Q] Sair
"""
saldo = 0
limite = 500
extrato = ""
saques_diarios = 0
SAQUES_REALIZADOS = 3

while True:
    options = input(menu)
    
    if options == "D":
        try:
            valor = float(input("Qual valor você deseja depositar: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                extrato += f"Saldo: R$ {saldo:.2f}\n"
            else:
                print("Não foi possível seguir com a operação, o valor informado é inválido, digite outro valor.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido.")

    elif options == "S":
        try:
            valor = float(input("Qual o valor deseja sacar: "))
            saldo_excedido = valor > saldo
            limite_excedido = valor > limite
            saques_excedidos = saques_diarios >= SAQUES_REALIZADOS

            if saldo_excedido:
                print("Não foi possível realizar a operação!!! Saldo insuficiente.")
            elif limite_excedido:
                print("Não foi possível realizar a operação!!! Não possui limite o suficiente.")
            elif saques_excedidos:
                print("Não foi possível realizar a operação!!! Número de Saques Diários esgotados.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                extrato += f"Saldo: R$ {saldo:.2f}\n"
                saques_diarios += 1
            else:
                print("Não foi possível completar a operação. O valor informado não é válido.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido.")

    elif options == "E":
        print("\n============ Extrato ============")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=================================")

    elif options == "Q":
        break

    else:
        print("Operação inválida, por favor selecionar um dos itens mostrados na tela.")
