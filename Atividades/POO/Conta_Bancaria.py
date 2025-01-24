class Conta_Bancaria:
    def __init__(self, nome, cpf, senha, saldo: float):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido")
    
    def sacar(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")
    
    def transferencia(self, outra_conta: "Conta_Bancaria", valor):
        if valor <= self.saldo:
            self.sacar(valor)
            outra_conta.depositar(valor)

    def __str__(self) -> str :
        return f"Conta de {self.nome}, tem saldo de R$ {self.saldo}"



        
minha_Conta = Conta_Bancaria("marcos", "22143554643", "1234", 35.99)
print(minha_Conta)

# Sub-classe

class Conta_Poupanca(Conta_Bancaria):
    def __init__(self, nome, cpf, senha, saldo):
        super().__init__(nome, cpf, senha, saldo)

