# Classe que representa uma fila (Queue)
class Queue:
    def __init__(self, c): #Construtor da fila
        # Inicializa a fila com capacidade 'c'
        # Definindo variáveis
        self.queue = []      # Lista que armazenará os elementos da fila, isto é, recebe uma lista vazia.
        self.front = 0       # Ponteiro para o início da fila (não utilizado ativamente aqui), aponta para posição 0
        self.back = 0        # Ponteiro para o final da fila (quantidade de elementos inseridos), aponta para a posição 0
        self.capacity = c    # Capacidade máxima da fila

    def enqueue(self, data): # Função responsável por inserir um elemento no final da fila
        if self.capacity == self.back: # Verificando capacidade da fila
            print("A lista está cheia, o elemento", data, "não pode ser adicionado à fila")
        else:
            self.queue.append(data)  # Adiciona o elemento no final da lista
            self.back += 1           # Incrementa o contador de elementos
            print("O elemento", data, "foi adicionado à fila")

    def dequeue(self):
        # Remove um elemento do início da fila
        if self.back == 0:
            print("A fila está vazia, não é possível desenfileirar")
        else:
            print("O elemento", self.queue[0], "foi removido")
            self.queue.pop(0)   # Remove o primeiro elemento da fila
            self.back -= 1      # Decrementa o contador de elementos

    def peek(self):
        # Exibe o elemento que está no início da fila (sem removê-lo)
        if self.back == 0:
            print("A fila está vazia")
        else:
            print("O primeiro elemento da fila é:", self.queue[0])

    def display(self):
        # Exibe todos os elementos da fila
        if self.back == 0:
            print("A fila está vazia")
        else:
            print("Fila atual:", self.queue)


# Exemplo de uso da fila
q = Queue(10)        # Cria uma fila com capacidade 10
q.enqueue(5)
q.enqueue(15)
q.enqueue(25)
q.enqueue(35)
q.enqueue(45)
q.enqueue(50)
q.enqueue(55)
q.enqueue(60)
q.enqueue(65)
q.enqueue(70)

# Tentativa de incluir mais do que a capacidade máxima

q.enqueue(75)
q.enqueue(80)
q.enqueue(85)
q.enqueue(90)
q.enqueue(95)

# Removendo os elementos da fila.

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

# Tentativa de remover de uma fila já vazia

q.dequeue()  
q.dequeue()