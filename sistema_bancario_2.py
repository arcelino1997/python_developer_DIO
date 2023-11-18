def menu():
  print("""
    [ d  ] - Depositar
    [ s  ] - Sacar
    [ e  ] - Ver Extrato
    [ nu ] - Novo Usuário
    [ cc ] - Criar Conta
    [ lc ] - Listar Contas
    [ q  ] - Sair
  """)
  return "Escolha uma opção: "


def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo = saldo + valor
    extrato.append(f"Deposito: {valor}")
    print("Depósito feito com sucesso!")
  else:
    print(
        "Ocorreu um erro na operação. Por favor tente novamente em instantes")

  return saldo, valor, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  if valor > saldo:
    print("Saldo insuficiente.")
  elif valor > 500:
    print("Limite de saque excedido.")
  elif valor > 0 and limite_saques > numero_saques:
    saldo = saldo - valor
    extrato.append(f"Saque: {valor:.2f}")
    numero_saques = numero_saques + 1
    print("Saque realizado com sucesso")
  else:
    print("Operação inválida")
  return saldo, extrato, numero_saques


def show_extrato(saldo, /, *, extrato):
  for item in extrato:
    print(item)
  print(saldo)


def cadastrar_usuario(lista_usuarios):
  dictUser = dict.fromkeys(["nome", "dataNasc", "endereço", "cpf"], "vazio")
  dictUser["cpf"] = input("Digite somente os números de seu cpf: ")
  if buscar_cpf(lista_usuarios, dictUser["cpf"]):
    return print("Usuário já cadastrado")
  else:
    dictUser["nome"] = input("Nome: ")
    dictUser["dataNasc"] = input("Data de nascimento: ")
    logradouro = input("Rua: ")
    numero = input("N°: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    sigla = input("Sigla do Estado: ")
    dictUser[
        "endereço"] = f"{logradouro}, {numero} - {bairro} - {cidade}/{sigla}"
    lista_usuarios.append(dictUser.copy())
    return lista_usuarios


def criar_conta(agencia, contas, usuario):
  num_conta = str(len(contas) + 1)
  cpfUser = input("Digite somente o numero do cpf do usuario: ")

  if (buscar_cpf(usuario, cpfUser)):
    dictContas = dict.fromkeys({"Agencia", "Numero da Conta", "Usuario"},
                               "Vazio")
    dictContas["Agencia"] = agencia
    dictContas["Numero da Conta"] = num_conta
    dictContas["Usuario"] = cpfUser
    contas.append(dictContas.copy())
    print("Conta criada com sucesso.")
    return contas
  else:
    print("Usuario não cadastrado. Por favor, tente novamente em instantes")


def buscar_cpf(lista_usuarios, cpf):
  for item in lista_usuarios:
    if item["cpf"] == cpf:
      return True


def listar_contas(contas):
  for item in contas:
    print(item)


##################   INICIO DO PROGRAMA ######################
saldo = 0.0  #SALDO EM CONTA
extrato = []  #MOVIMENTAÇÕES NA CONTA
AGENCIA = "0001"
limite = 500
numero_saques = 0
limite_saques = 3
valor = 0.0
usuarios = []
contas = []

while True:
  opcao = input(f"{menu()}")
  if opcao == "d" or opcao == "Depositar":

    valor = float(input("Qual valor do depósito? "))  # SAQUE E DEPOSITO
    saldo, valor, extrato = depositar(saldo, valor, extrato)

  elif opcao == "s" or opcao == "Sacar":
    if numero_saques < limite_saques:
      valor = float(input("Qual valor do saque? "))  # SAQUE E DEPOSITO
      saldo, extrato, numero_saques = sacar(saldo=saldo,
                                            valor=valor,
                                            extrato=extrato,
                                            limite=limite,
                                            numero_saques=numero_saques,
                                            limite_saques=limite_saques)

    else:
      print("Limite de saques excedido")

  elif opcao == "e" or opcao == "Extrato":

    show_extrato(saldo, extrato=extrato)

  elif opcao == "nu" or opcao == "Novo Usuario":
    usuarios = cadastrar_usuario(usuarios)

  elif opcao == "cc" or opcao == "Criar Conta":
    contas = criar_conta(AGENCIA, contas=contas, usuario=usuarios)

  elif opcao == "lc" or opcao == "Listar Contas":
    listar_contas(contas)

  elif opcao == "q" or opcao == "Sair":
    print("""
      Obrigado por usar nossos sistemas. 
      Até logo... 
    """)
    break
