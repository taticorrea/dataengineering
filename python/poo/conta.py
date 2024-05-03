class Conta:
    
    def __init__(self,numero, agencia, titular, saldo, limite) -> None:
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__agencia = agencia
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
    
    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        print("chamando getter do saldo()")
        return self.__saldo

    @property
    def numero(self):
        print("fazendo um getter do numero()")
        return self.__numero

    @property
    def titular(self):
        print("fazendo um getter do titular")
        return self.__titular

    @property
    def limite(self):
        print("chamando getter limite()")
        return self.__limite

    @limite.setter
    def limite(self,limite):
        print("chamando setter limite()")
        self.__limite = limite        
    
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB":"001",
                "CAIXA":"104",
                "Bradesco":"237"}
    
    def extrato(self):
        print("Titular: {} \nConta: {} \nAgencia: {} \nSaldo: R$ {} ,00 \nLimite: R$ {} ,00".format(self.__titular,self.__numero,self.__agencia,self.__saldo,self.__limite))