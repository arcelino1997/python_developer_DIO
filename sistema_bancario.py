menu = '''
[d] - Depositar
[s] - Sacar
[e] - Estrato
[q] - Sair
'''
saldo = 0.0
saque = 0.0
qtd_saques = 1
LIMITE_SAQUE = 3
estrato = []

while True:
  print(menu)
  opcao = input("Digite a opção: ")

  if (opcao == 'd'):
    deposito = float(input("Digite o valor do deposito: "))
    if (deposito > 0.0):
      saldo = saldo + deposito
      estrato.append('Deposito: R$ ' + str(deposito))

  elif (opcao == 's'):
    print("São permitidos até 3 saques diários de até R$ 500.00")
    saque = float(input("Valor a ser sacado: "))
    if (saldo > 0.0 and saque <= saldo):
      if (qtd_saques <= LIMITE_SAQUE):
        if (saque <= 500):
          qtd_saques = qtd_saques + 1
          saldo = saldo - saque
          estrato.append('Saque: R$ ' + str(saque))
        else:
          print(
              "Sque máximo disponível de R$ 500.00. Por favor, tente novamente em instantes."
          )
      else:
        print(
            "Limite de saques diários atingido. Por favor tente novamente mais tarde!"
        )
    else:
      print("Saldo insuficiente.")

  elif (opcao == 'e'):
    print("##############################")
    if (len(estrato) == 0):
      print("Nenhuma movimentação ocorreu")
    else:
      for i in range(0, len(estrato), 1):
        print(estrato[i])
    print(f"Saldo: {saldo:.2f}")
    print("##############################")
  elif (opcao == 'q'):
    print("Saindo do Sistema")
    break
  else:
    print("Opção inválida. Tente novamente")
