```python
from abc import ABC, abstractmethod
class Forma(ABC):
    def __init__(self, valor):
        self.valor = valor  # usa setter

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, v):
        if v < 0:
            raise ValueError("Valor não pode ser negativo")
        self._valor = v

    @abstractmethod
    def calcular_area(self):
        pass



class Quadrado(Forma):
    def calcular_area(self):
        return self.valor * self.valor



class Circulo(Forma):
    def calcular_area(self):
        return 3.14 * (self.valor ** 2)
        
q = Quadrado(4)
c = Circulo(5)
print(q.calcular_area())  # 16
print(c.calcular_area())  # 78.5
```
