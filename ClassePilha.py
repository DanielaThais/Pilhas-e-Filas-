class Stack:
    def __init__(self, capacity = None): # Construtor da classe
        # Inicializa a pilha.
        self.items = []
        self.capacity = capacity
       

    def push(self, data):
      # Adiciona um elemento ao topo da pilha.
        if self.capacity is not None and len(self.items) >= self.capacity:
            print("Erro: Capacidade máxima atingida. Não é possível adicionar", data)
        else:
            self.items.append(data)
            print("O item", data, "foi inserido na pilha.")

    def isEmpty(self):
        # Retorna True se a pilha estiver vazia.
        return len(self.items) == 0

    def pop(self):
        # Remove e retorna o elemento do topo da pilha.
        if self.isEmpty():
            print("Erro: A pilha já está vazia.")
            return None
        else:
            item = self.items.pop()
            print("O item", item, "foi removido da pilha.")
            return item

    def peek(self):
        # Retorna o elemento no topo da pilha sem removê-lo.
        if self.isEmpty():
            print("A pilha está vazia.")
            return None
        else:
            print("Topo da pilha:", self.items[-1])
            return self.items[-1]

    def show(self):
        # Exibe a pilha do topo até a base.
        if self.isEmpty():
            print("A pilha está vazia.")
        else:
            print("\nEstado atual da pilha:")
            for i, item in enumerate(reversed(self.items)):
                if i == 0:
                    print(item, "<----- Topo")
                else:
                    print(item)

    def size(self):
        # Retorna o número de elementos na pilha.
        return len(self.items)


# Exemplo de uso:
pilha = Stack(capacity=5)  # Pilha com capacidade máxima de 5 elementos

pilha.push(10)
pilha.push(20)
pilha.push(30)
pilha.push(40)
pilha.push(50)

# Tentativa de incluir mais do que a capacidade permite
pilha.push(60)  

pilha.show()
pilha.peek()

pilha.pop()
pilha.show()

pilha.pop()
pilha.pop()
pilha.pop()
pilha.pop()

# Tentativa de remover de pilha vazia

pilha.pop()  
