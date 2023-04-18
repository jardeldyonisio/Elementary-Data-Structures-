class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # ponteiro para o próximo nó

class LinkedList:
    def __init__(self):
        self.head = None # cabeça da lista (inicialmente vazia)
    
    def add(self, val):
        # cria um novo nó com o valor dado
        new_node = Node(val)
        if self.head is None:
            # se a lista estiver vazia, defina a cabeça da lista como o novo nó
            self.head = new_node
        else:
            # insere o novo nó no final da lista
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def remove(self, val):
        if self.head is None:
            return
        if self.head.data == val:
            # se o valor a ser removido for o da cabeça da lista, defina a cabeça como o próximo nó
            self.head = self.head.next
            return
        # encontra o nó anterior ao nó que contém o valor a ser removido
        prev = self.head
        while prev.next is not None:
            if prev.next.data == val:
                # remove o nó da lista atualizando o ponteiro do nó anterior
                prev.next = prev.next.next
                return
            prev = prev.next
    
    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

# Exemplo de uso
list = LinkedList()
list.add(1)
list.add(2)
list.add(3)
list.print() # Saída: 1 2 3
list.remove(2)
list.print() # Saída: 1 3
