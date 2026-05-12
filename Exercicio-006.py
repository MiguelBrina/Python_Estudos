```python
class Veiculo:
    def __init__(self, nome, modelo, marca):
        self.nome = nome
        self.modelo = modelo
        self.marca = marca
        
class Motor:
def ligar(self):
print("motor ligado") #função de ligar o motor
    def desligar(self):
        print("motor desligado") #função de desligar o motor

class Carro(Veiculo):
    def __init__(self, nome, modelo, marca, motor):
        super().__init__(nome, modelo, marca)
        self.motor = motor
        
    def ligar_carro(self):
        self.motor.ligar()
        
    def desligar_carro(self):
        self.motor.desligar()

m = Motor()
c = Carro("miguel", "onix", "chevrolet", m)
c.ligar_carro()
c.desligar_carro()
```
