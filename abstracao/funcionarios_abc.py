
from abc import ABC, abstractmethod
class Funcionario(ABC):
def init(self, nome):
self.nome = nome
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, v):
        if len(v) < 1:
            raise ValueError("nome não pode ficar vazio")
        self._nome = v
        
    @abstractmethod
    def calcular_salario(self):
        pass



class FuncionarioCLT(Funcionario):
def init(self, nome, salario):
super().init(nome)
self.salario = salario
    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, v):
        if v < 0:
            raise ValueError("Salário não pode ser negativo")
        self._salario = v

    def calcular_salario(self):
        return self.salario



class FuncionarioPJ(Funcionario):
def init(self, nome, horas, v_horas):
super().init(nome)
self.horas = horas
self.v_horas = v_horas
    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, v):
        if v < 0:
            raise ValueError("Horas não podem ser negativas")
        self._horas = v
    
    @property
    def v_horas(self):
        return self._v_horas

    @v_horas.setter
    def v_horas(self, v):
        if v < 0:
            raise ValueError("Valor por hora não pode ser negativo")
        self._v_horas = v
        
    def calcular_salario(self):
        return self.horas * self.v_horas



funcs = [
FuncionarioCLT("Miguel", 3000),
FuncionarioPJ("mig-rico", 50, 100)
]

for f in funcs:
print(f.nome,":",f.calcular_salario()) #Miguel : 3000 mig-rico : 5000
