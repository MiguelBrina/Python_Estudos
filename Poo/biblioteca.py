
class Book:
def init(self, name: str, price: float):
# validações básicas
if not name:
raise ValueError("O nome do livro não pode ser vazio")
if price < 0:
raise ValueError("O preço não pode ser negativo")
        self.name = name
        self.price = price



class Library:
def init(self):
# lista que armazena objetos Book
self.books = []
    def add_book(self, book: Book):
        # garante que só livros sejam adicionados
        if not isinstance(book, Book):
            raise TypeError("Apenas objetos do tipo Book podem ser adicionados")
        
        self.books.append(book)
        
    def list_books(self):
        # se não tiver livros, evita print vazio
        if not self.books:
            print("Nenhum livro na biblioteca.")
            return
        
        print("📚 Lista de livros:")
        for book in self.books:
            print(f"- Nome: {book.name} | Preço: R${book.price}")
    
    def total(self):
        # soma total dos preços
        return sum(book.price for book in self.books)



===== TESTE =====
l1 = Book("Dom Casmurro", 22)
l2 = Book("Malala", 67)
ze_library = Library()
ze_library.add_book(l1)
ze_library.add_book(l2)
ze_library.list_books()
print(f"\n💰 Total da biblioteca: R${ze_library.total()}")
