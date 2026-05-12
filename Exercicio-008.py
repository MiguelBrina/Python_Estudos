```python
class Item:
    def __init__(self, nome: str, preco: float):
        self.nome = nome 
        self.preco = preco
        
    @property
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome(self, n):
        if not n.strip():
            raise ValueError("nome não pode estar vazio")
        self._nome = n
        
    @property
    def preco(self):
        return self._preco
        
    @preco.setter
    def preco(self, n):
        if n <= 0:
            raise ValueError("preço não pode ser negativo ou igual a zero")
        self._preco = n



class Pedido:
    def __init__(self):
        self.itens = []
        
    def adicionar_item(self, item: Item):
        if not isinstance(item, Item):
            raise TypeError("Apenas objetos do tipo Item podem ser adicionados")
        
        self.itens.append(item)
        
    def listar_itens(self):
        if not self.itens:
            print("Pedido vazio")
            return
        
        print("\n📦 Lista de itens:")
        for item in self.itens:
            print(f"- {item.nome} | R${item.preco:.2f}")
            
    def total(self):
        return sum(item.preco for item in self.itens)



===== TESTE =====
p1 = Pedido()
i1 = Item("Mochila Tática 50L", 145.26)
i2 = Item("Capa de Chuva Mochila", 69.00)
i3 = Item("Conjunto Capa de Chuva", 126.90)
i4 = Item("Bomba de Ar", 72.99)
i5 = Item("Manopla Silicone", 16.56)
i6 = Item("Saco Estanque 10L", 38.74)
p1.adicionar_item(i1)
p1.adicionar_item(i2)
p1.adicionar_item(i3)
p1.adicionar_item(i4)
p1.adicionar_item(i5)
p1.adicionar_item(i6)
p1.listar_itens()
print(f"\n💰 Total do pedido: R${p1.total():.2f}")
```
