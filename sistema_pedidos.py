class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @nome.setter
    def nome(self, n):

        if not isinstance(n, str):
            raise TypeError("nome deve ser uma string")

        if not n.strip():
            raise ValueError("nome não pode estar vazio")

        self._nome = n

    @preco.setter
    def preco(self, p):

        if not isinstance(p, (float, int)):
            raise TypeError("preco deve ser um numero")

        if p < 0:
            raise ValueError("preço deve ser maior ou igual a zero")

        self._preco = p


class Pedido:

    # ID automático
    contador_id = 1

    def __init__(self):

        self.id = Pedido.contador_id
        Pedido.contador_id += 1

        self.fechado = False
        self.itens = []

    # adicionar item
    def adicionar_item(self, item):

        if not isinstance(item, Item):
            raise TypeError("o item deve ser do tipo Item")

        if self.fechado:
            raise Exception("Pedido fechado!")

        self.itens.append(item)

    # listar itens
    def listar_itens(self):

        if not self.itens:
            print("Nenhum item no pedido.")
            return

        print(f"\n📦 PEDIDO ID: {self.id}")
        print("📦 ITENS:")

        for i, item in enumerate(self.itens):
            print(f"{i+1} - {item.nome} | R$ {item.preco:.2f}")

    # calcular total
    def calcular_total(self):

        total = 0

        for item in self.itens:
            total += item.preco

        return total

    # fechar pedido
    def fechar_pedido(self):

        if self.fechado:
            print("Pedido já foi fechado.")
            return

        if not self.itens:
            raise ValueError("pedido vazio")

        self.fechado = True

        print("\nPedido fechado com sucesso!")
        print(f"Total: R$ {self.calcular_total():.2f}")

    # buscar item
    def buscar_item(self, nome):

        for item in self.itens:

            if nome.lower() == item.nome.lower():
                return item

        return None

    # remover item
    def remover_item(self, nome):

        if self.fechado:
            print("pedido fechado!")
            return

        resultado = self.buscar_item(nome)

        if resultado is None:
            raise ValueError("item inexistente")

        self.itens.remove(resultado)

    # item mais caro
    def item_mais_caro(self):

        if not self.itens:
            return None

        mais_caro = self.itens[0]

        for item in self.itens:

            if item.preco > mais_caro.preco:
                mais_caro = item

        return mais_caro

    # item mais barato
    def item_mais_barato(self):

        if not self.itens:
            return None

        mais_barato = self.itens[0]

        for item in self.itens:

            if item.preco < mais_barato.preco:
                mais_barato = item

        return mais_barato

    # quantidade de itens
    def quantidade_itens(self):

        return len(self.itens)

    # desconto em um item
    def aplicar_desconto_item(self, nome, porcentagem):

        if self.fechado:
            print("pedido fechado!")
            return

        item = self.buscar_item(nome)

        if item is None:
            raise ValueError("item não encontrado")

        desconto = item.preco * (porcentagem / 100)

        item.preco -= desconto

        print(f"Desconto de {porcentagem}% aplicado em {item.nome}")

    # desconto em todos os itens
    def aplicar_desconto_total(self, porcentagem):

        if self.fechado:
            print("pedido fechado!")
            return

        for item in self.itens:

            desconto = item.preco * (porcentagem / 100)

            item.preco -= desconto

        print(f"Desconto de {porcentagem}% aplicado em todos os itens")

    # desconto personalizado
    def aplicar_descontos_personalizados(self, descontos):

        if self.fechado:
            print("pedido fechado!")
            return

        for nome, porcentagem in descontos.items():

            item = self.buscar_item(nome)

            if item:

                desconto = item.preco * (porcentagem / 100)

                item.preco -= desconto

                print(f"{porcentagem}% aplicado em {item.nome}")

            else:
                print(f"{nome} não encontrado")


# =========================
# TESTES
# =========================

p1 = Pedido()

i1 = Item("Mochila Tática 50L", 145.26)
i2 = Item("Capa de Chuva Mochila", 69.00)
i3 = Item("Conjunto Capa de Chuva", 126.90)
i4 = Item("Bomba de Ar", 72.99)
i5 = Item("Manopla Silicone", 16.56)
i6 = Item("Saco Estanque 10L", 38.74)
i7 = Item("teste", 20)
i8 = Item("TESTE", 40)

# adicionando itens
p1.adicionar_item(i1)
p1.adicionar_item(i2)
p1.adicionar_item(i3)
p1.adicionar_item(i4)
p1.adicionar_item(i5)
p1.adicionar_item(i6)
p1.adicionar_item(i8)

# listagem inicial
p1.listar_itens()

# remover item
print("\n--- REMOVENDO ITEM ---")
p1.remover_item("TESTE")

p1.listar_itens()

# desconto em item específico
print("\n--- DESCONTO ITEM ---")
p1.aplicar_desconto_item("Bomba de Ar", 10)

# desconto em todos
print("\n--- DESCONTO TOTAL ---")
p1.aplicar_desconto_total(5)

# descontos personalizados
print("\n--- DESCONTOS PERSONALIZADOS ---")

descontos = {
    "Mochila Tática 50L": 20,
    "Manopla Silicone": 50,
    "Saco Estanque 10L": 15
}

p1.aplicar_descontos_personalizados(descontos)

# listagem após descontos
print("\n--- LISTA FINAL ---")
p1.listar_itens()

# total
print(f"\nTotal: R$ {p1.calcular_total():.2f}\n")

# item mais caro
print("\t|MAIS CARO|")
print(
    f"nome: {p1.item_mais_caro().nome} | "
    f"preço: {p1.item_mais_caro().preco:.2f}\n"
)

# item mais barato
print("\t|MAIS BARATO|")
print(
    f"nome: {p1.item_mais_barato().nome} | "
    f"preço: {p1.item_mais_barato().preco:.2f}\n"
)

# quantidade
print(f"Quantidade: {p1.quantidade_itens()}\n")

# fechar pedido
p1.fechar_pedido()

# testar erro ao adicionar item em pedido fechado
try:
    p1.adicionar_item(i8)

except Exception as erro:
    print(erro)

# buscar item
item = p1.buscar_item("mochila Tática 50L")

if item:
    print(f"\nItem encontrado: {item.nome}")
