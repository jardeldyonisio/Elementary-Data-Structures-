class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None # ponteiro para o nó anterior
        self.next = None # ponteiro para o próximo nó

class DoublyLinkedList:
    def __init__(self):
        self.head = None # cabeça da lista (inicialmente vazia)
    
    def add(self, val):
        # cria um novo nó com o valor dado
        new_node = Node(val)
        if self.head is None:
            # se a lista estiver vazia, defina a cabeça da lista como o novo nó
            self.head = new_node
        else:
            # percorre a lista até o último nó
            current = self.head
            while current.next is not None:
                current = current.next
            # insere o novo nó depois do último nó
            current.next = new_node
            new_node.prev = current
    
    def remove(self, val):
        if self.head is None:
            return
        if self.head.data == val:
            # se o valor a ser removido é o valor da cabeça da lista, atualize a cabeça da lista
            self.head = self.head.next
            if self.head is not None:
                # se ainda houver um nó na lista, defina o ponteiro anterior da cabeça como None
                self.head.prev = None
            return
        # percorre a lista até encontrar o nó que contém o valor a ser removido
        current = self.head
        while current.next is not None and current.next.data != val:
            current = current.next
        if current.next is None:
            return
        # remove o nó da lista atualizando os ponteiros dos nós adjacentes
        current.next = current.next.next
        if current.next is not None:
            current.next.prev = current
    
    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# Exemplo de uso
list = DoublyLinkedList()
list.add(1)
list.add(2)
list.add(3)
list.print() # Saída: 1 2 3
list.remove(2)
list.print() # Saída: 1 3
