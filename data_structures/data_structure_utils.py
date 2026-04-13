"""Modulo con strutture dati di base"""

import numpy as np


class PilaListBased:

    def __init__(self):
        self.__pila = []

    def push(self, dato):
        self.__pila.append(dato)

    def pop(self):
        if self.is_empty():
            raise Exception("La pila è vuota")
        return self.__pila.pop()

    def top(self):
        if self.is_empty():
            raise Exception("La pila è vuota")
        return self.__pila[-1]

    def is_empty(self):
        return len(self.__pila) == 0

    def size(self):
        return len(self.__pila)

    def clear(self):
        self.__pila.clear()

    def __str__(self):
        return str(self.__pila)


class PilaArrayBased:

    def __init__(self, capacity=10):
        self.__pila = np.empty(capacity, dtype=object)
        self.__top = -1
        self.__capacity = capacity

    def push(self, dato):
        if self.__top + 1 >= self.__capacity:
            raise Exception("La pila è piena")
        self.__top += 1
        self.__pila[self.__top] = dato

    def pop(self):
        if self.is_empty():
            raise Exception("La pila è vuota")
        dato = self.__pila[self.__top]
        self.__pila[self.__top] = None  # Pulire il riferimento
        self.__top -= 1
        return dato

    def top(self):
        if self.is_empty():
            raise Exception("La pila è vuota")
        return self.__pila[self.__top]

    def is_empty(self):
        return self.__top == -1

    def size(self):
        return self.__top + 1

    def clear(self):
        self.__pila.fill(None)
        self.__top = -1

    def __str__(self):
        return str(self.__pila[: self.__top + 1])


class PilaLinkedListBased:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, dato):
        new_node = self.Node(dato)
        new_node.next = self.__top
        self.__top = new_node
        self.__size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("La pila è vuota")
        dato = self.__top.data
        self.__top = self.__top.next
        self.__size -= 1
        return dato

    def top(self):
        if self.is_empty():
            raise Exception("La pila è vuota")
        return self.__top.data

    def is_empty(self):
        return self.__size == 0

    def size(self):
        return self.__size

    def clear(self):
        self.__top = None
        self.__size = 0

    def __str__(self):
        result = []
        current = self.__top
        while current is not None:
            result.append(current.data)
            current = current.next
        result.reverse()
        return str(result)


class QueueListBased:

    def __init__(self):
        self.__queue = []

    def push(self, elemento: int):
        self.__queue.append(elemento)

    def pop(self):
        if len(self.__queue) == 0:
            raise Exception("La coda è vuota")
        return self.__queue.pop(0)

    def top(self):
        if len(self.__queue) == 0:
            raise Exception("La coda è vuota")
        return self.__queue[0]

    def size(self):
        return len(self.__queue)

    def is_empty(self):
        return len(self.__queue) == 0

    def __str__(self):
        return f"{self.__queue}"

    def get_lunghezza(self):
        return len(self.__queue)


class QueueArrayBased:

    def __init__(self, grandezza: int = 10):
        self.__grandezza = grandezza
        self.__coda = np.empty(shape=grandezza)
        self.__lunghezza = -1

    def push(self, elemento: int):
        if self.__lunghezza + 1 >= self.__grandezza:
            raise Exception("Coda piena")
        self.__lunghezza += 1
        self.__coda[self.__lunghezza] = elemento

    def pop(self):
        if self.__lunghezza < 0:
            raise Exception("Coda vuota")
        testa = self.__coda[0]
        for i in range(self.__lunghezza):
            self.__coda[i] = self.__coda[i + 1]
        self.__lunghezza -= 1
        return testa

    def __str__(self):
        return f"{[round(el, 2) for el in self.__coda]}"

    def get_lunghezza(self):
        return self.__lunghezza + 1


class QueueLinkedList:
    class Node:
        def __init__(self, elemento):
            self.valore = elemento
            self.successivo = None

    def __init__(self):
        self.__testa = None
        self.__coda = None
        self.__lunghezza = 0

    def push(self, elemento: int):
        nuovo_nodo = self.Node(elemento)
        if self.__lunghezza == 0:
            self.__testa = nuovo_nodo
            self.__coda = nuovo_nodo
        else:
            self.__coda.successivo = nuovo_nodo
            self.__coda = nuovo_nodo
        self.__lunghezza += 1

    def pop(self):
        if self.__lunghezza == 0:
            raise Exception("La coda è vuota")
        el = self.__testa.valore
        self.__testa = self.__testa.successivo
        if self.__testa == None:
            self.__coda = None
        self.__lunghezza -= 1
        return el

    def __str__(self):
        a = self.__testa
        if a == None:
            return "Coda vuota"
        l = [a.valore]
        while a.successivo != None:
            a = a.successivo
            l.append(a.valore)
        return f"{l}"

    def get_lunghezza(self):
        return self.__lunghezza


class Nodo:

    def __init__(self, v: int, p=None, l=0):
        self.__valore = v
        self.__padre = p
        self.__level = l

    def get_valore(self):
        return self.__valore

    def get_padre(self):
        return self.__padre

    def get_level(self):
        return self.__level

    def child(self, v: int):
        return Nodo(v, self, self.__level + 1)

    def __str__(self):
        return f"Valore Nodo: {self.__valore}\nLevel: {self.__level}"
