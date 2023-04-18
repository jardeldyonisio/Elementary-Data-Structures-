class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # ponteiro para o próximo nó

class CircularLinkedList:
    def __init__(self):
        self.head = None # cabeça da lista (inicialmente vazia)
    
    def add(self, val):
        # cria um novo nó com o valor dado
        new_node = Node(val)
        if self.head is None:
            # se a lista estiver vazia, defina a cabeça da lista como o novo nó e faça a lista circular
            self.head = new_node
            new_node.next = new_node
        else:
            # insere o novo nó depois da cabeça da lista e atualiza os ponteiros
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node
    
    def remove(self, val):
        if self.head is None:
            return
        if self.head.next == self.head and self.head.data == val:
            # se há apenas um nó na lista e contém o valor a ser removido, defina a cabeça da lista como None
            self.head = None
            return    

        # encontra o nó anterior ao nó que contém o valor a ser removido
        prev = self.head
        while prev.next != self.head:
            if prev.next.data == val:
                # remove o nó da lista atualizando o ponteiro do nó anterior
                prev.next = prev.next.next
                return
            prev = prev.next
        if self.head.data == val:
            # atualiza a cabeça da lista e o ponteiro do último nó, se o valor a ser removido for o da cabeça da lista
            prev.next = self.head.next
            self.head = prev.next
    
    def print(self):
        if self.head is None:
            return
        current = self.head.next
        while current != self.head:
            print(current.data, end=" ")
            current = current.next
        print(self.head.data)

# Exemplo de uso
list = CircularLinkedList()
list.add(1)
list.add(2)
list.add(3)
list.print() # Saída: 3 2 1
list.remove(2)
list.print() # Saída: 3 1