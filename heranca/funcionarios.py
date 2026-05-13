class Funcionário:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_pagamento(self):
        return self.salario + self.bonus


class Freelancer(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor hora:
        super().__init__(nome, 0)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
        
    def calcular_pagamento(self):
        return self.horas_trabalhadas  self.valor_hora


# criar os objetos
g1 = Gerente(Carlos, 5000, 2000)
f1 = Freelancer(Ana, 40, 50)
f2 = Freelancer(Pedro, 30, 60)

# lista de funcionarios
funcionarios = [g1, f1, f2]

for f in funcionarios
    print(f.nome)
    print(Pagamento, f.calcular_pagamento())
    print()
