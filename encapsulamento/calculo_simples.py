class Retangulo:

    def __init__(self, altura, largura):
        self._altura = altura
        self._largura = largura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
        else:
            raise ValueError("Altura não pode ser negativa")

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self._largura = valor
        else:
            raise ValueError("Largura não pode ser negativa")

    @property
    def area(self):
        return self._altura * self._largura
        
r = Retangulo(5,10)


try:
    r.altura = -20
except ValueError as e:
    print(e)

print(r.area)
r.largura = 20
print(r.area)  # 100

r.altura = 2
print(r.area)  # 40
