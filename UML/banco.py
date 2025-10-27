class Pessoa:
  def __init__(self,nome,cpf,rg):
    self.nome = nome
    self.cpf = cpf
    self.rg = rg
  def get_nome(self):
    return self.nome
  def get_cpf(self):
    return self.cpf
  def get_rg (self):
    return self.rg

pessoa1 = Pessoa('Douglas', '094.645.788-89','202205265963-1')
pessoa2 = Pessoa('Maria', '094.621.303-56','2022026147-1')

class Conta:
  def __init__(self,numero,saldo,titular):
    self.numero = numero
    self.saldo = saldo
    self.titular = titular
  def get_numero(self):
    return self.numero
  def get_saldo(self):
    return self.saldo
  def get_titular(self):
    return self.titular

conta1 = Conta('1428',4000,pessoa1)
conta2 = Conta('1429',5000,pessoa2)

class Banco:
  def  __init__(self, online, nome):
    self.online = online
    self.nome = nome
    self.contas = []
  def get_online(self):
    return self.online
  def get_nome(self):
    return self.nome
  def procurar_conta(self,numero):
    for conta in self.contas:
      if conta.numero == numero:
        return conta
    print('Conta não encontrada') 
    return None
  def cadastrar(self,conta):
    self.contas.append(conta)
    print('Conta cadastrada com sucesso')
  def creditar(self,numero,valor):
    conta = self.procurar_conta(numero)
    if conta:
      conta.saldo += valor
      print('Depósito realizado com sucesso')
  def debitar(self,numero,valor):
    conta = self.procurar_conta(numero)
    if conta:
      if conta.saldo >= valor:
        conta.saldo -= valor
        print('Saque realizado com sucesso')
  def saldo(self,numero):
    conta = self.procurar_conta(numero)
    if conta:
      print('Seu saldo é de R$',conta.get_saldo())
  def transferir(self,numero_origem,numero_destino,valor):
    conta_origem = self.procurar_conta(numero_origem)
    conta_destino = self.procurar_conta(numero_destino)
    if conta_origem and conta_destino:
      if conta_origem.saldo >= valor:
        conta_origem.saldo -= valor
        conta_destino.saldo += valor
        print('Transferência realizada com sucesso')

  
    
banco = Banco(True,'Nubank')
if banco.get_online():
  banco.cadastrar(conta1)
  banco.cadastrar(conta2)
  print(f'Informações das contas:')
  for conta in banco.contas:
    print(f'Número: {conta.get_numero()}, Saldo: {conta.get_saldo()}, Titular: {conta.titular.get_nome()},RG: {conta.titular.get_rg()}, CPF:{conta.titular.get_cpf()}')
  conta_procurada = banco.procurar_conta('1428')
  if conta_procurada:
    print(f'Informações da conta procurada:')
    print(f'Número: {conta_procurada.get_numero()}, Saldo: {conta_procurada.get_saldo()}, Titular: {conta_procurada.titular.get_nome()},RG: {conta_procurada.titular.get_rg()}, CPF:{conta_procurada.titular.get_cpf()}')
  print(f'Saldo da conta 1:')
  banco.saldo('1428')
  print(f'Saldo da conta 2:')
  banco.saldo('1429')
  print(f'Realizando depósito na conta 1:')
  banco.creditar('1428',1000)
  print(f'Saldo da conta 1:')
  banco.saldo('1428')
  print(f'Realizando saque na conta 1:')
  banco.debitar('1428',500)
  print(f'Saldo da conta 1:')
  banco.saldo('1428')
  print(f'Realizando transferência da conta 1 para a conta 2:')
  banco.transferir('1428','1429',500)
  print(f'Saldo da conta 1:')
  banco.saldo('1428')
  print(f'Saldo da conta 2:')
  banco.saldo('1429')





