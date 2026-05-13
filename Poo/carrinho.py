class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome      # usa setter
        self.preco = preco    # usa setter

    # GETTER nome
    @property
    def nome(self):
        return self._nome

    # SETTER nome
    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode estar vazio")
        self._nome = valor

    # GETTER preco
    @property
    def preco(self):
        return self._preco

    # SETTER preco
    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("Preço não pode ser zero ou negativo")
        self._preco = valor



class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        if not isinstance(produto, Produto):
            raise TypeError("Apenas objetos Produto são permitidos")
        
        self.produtos.append(produto)

    def listar_produtos(self):
        if not self.produtos:
            print("Carrinho vazio")
            return
        
        print("🛒 Carrinho:")
        for produto in self.produtos:
            print(f"- Produto: {produto.nome} | Preço: R${produto.preco}")

    def total(self):
        return sum(produto.preco for produto in self.produtos)

    def produto_mais_caro(self):
        if not self.produtos:
            raise ValueError("Não há produtos no carrinho")
        
        mais_caro = self.produtos[0]

        for produto in self.produtos:
            if produto.preco > mais_caro.preco:
                mais_caro = produto
        
        return mais_caro

 
    def produto_mais_barato(self):
        if not self.produtos:
            raise ValueError("Não há produtos no carrinho")
        
        mais_barato = self.produtos[0]

        for produto in self.produtos:
            if produto.preco < mais_barato.preco:
                mais_barato = produto
        
        return mais_barato



TESTE
p1 = Produto("Mouse", 50)
p2 = Produto("Teclado", 120)
p3 = Produto("Monitor", 900)
carrinho = Carrinho()
carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.adicionar_produto(p3)
carrinho.listar_produtos()
print("Total:", carrinho.total())
print("Mais caro:", carrinho.produto_mais_caro().nome)
print("Mais barato:", carrinho.produto_mais_barato().nome)
