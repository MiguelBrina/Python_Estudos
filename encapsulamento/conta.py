class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo
     
    @property   
    def saldo(self):
        return self.__saldo
        
    @saldo.setter
    def saldo(self, valor):
       if valor < 0:
         raise ValueError("Saldo não pode ser Negativo")
       
       else:
           self.__saldo = valor
           
c = Conta(100)

print(c.saldo)

c.saldo = 200
print(c.saldo)

print(c.__saldo)  # deve dar erro
       
