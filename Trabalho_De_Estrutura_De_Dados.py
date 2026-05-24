from typing import Any, List


class Queue:
    # Cria uma fila vazia e, opcionalmente, define um tamanho máximo.
    def __init__(self, max_size=None) -> None:
        self.__data: List[Any] = []
        self.__max_size = max_size

    # Representação textual da fila para facilitar o print.
    def __repr__(self) -> str:
        return str(self.__data)

    # Adiciona um item ao final da fila.
    def enqueue(self, item: Any) -> None:
        if self.is_full():
            raise OverflowError(f"Fila cheia (limite: {self.__max_size})")
        self.__data.append(item)

    # Remove e retorna o primeiro item da fila.
    def dequeue(self) -> Any:
        if not self.__data:
            raise IndexError("Fila vazia")
        return self.__data.pop(0)

    # Retorna o primeiro item da fila sem removê-lo.
    def peek(self) -> Any:
        if not self.__data:
            raise IndexError("Fila vazia")
        return self.__data[0]

    # Verifica se a fila está vazia.
    def is_empty(self) -> bool:
        return len(self.__data) == 0

    # Verifica se a fila atingiu o tamanho máximo.
    def is_full(self) -> bool:
        if self.__max_size is None:
            return False
        return len(self.__data) >= self.__max_size

    # Retorna a quantidade de itens na fila.
    def size(self) -> int:
        return len(self.__data)

    # Limpa todos os itens da fila.
    def clear(self) -> None:
        self.__data = []


# Testa se a fila começa vazia.
def teste_fila_vazia():
    fila = Queue()
    if fila.is_empty() and fila.size() == 0:
        print("Teste 1 passou - fila começa vazia")
    else:
        print("Teste 1 falhou")


# Testa se a ordem FIFO está correta.
def teste_ordem_fifo():
    fila = Queue()
    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")
    if fila.dequeue() == "A" and fila.dequeue() == "B":
        print("Teste 2 passou - ordem FIFO correta")
    else:
        print("Teste 2 falhou")


# Testa se o peek retorna o primeiro item sem remover.
def teste_peek():
    fila = Queue()
    fila.enqueue(10)
    if fila.peek() == 10 and fila.size() == 1:
        print("Teste 3 passou - peek não remove")
    else:
        print("Teste 3 falhou")


# Testa se o clear realmente esvazia a fila.
def teste_clear():
    fila = Queue()
    fila.enqueue(1)
    fila.enqueue(2)
    fila.clear()
    if fila.is_empty():
        print("Teste 4 passou - clear funcionou")
    else:
        print("Teste 4 falhou")


# Testa se dequeue em fila vazia lança IndexError.
def teste_dequeue_vazia():
    fila = Queue()
    try:
        fila.dequeue()
        print("Teste 5 falhou")
    except IndexError:
        print("Teste 5 passou - IndexError lançado corretamente")


# Testa se a fila respeita o tamanho máximo.
def teste_max_size():
    fila = Queue(max_size=2)
    fila.enqueue(1)
    fila.enqueue(2)
    try:
        fila.enqueue(3)
        print("Teste 6 falhou")
    except OverflowError:
        print("Teste 6 passou - OverflowError lançado corretamente")


if __name__ == "__main__":
    fila = Queue()
    fila.enqueue("Cliente 1")
    fila.enqueue("Cliente 2")
    fila.enqueue("Cliente 3")

    print(fila)
    print(fila.dequeue())
    print(fila)
    print(fila.peek())

    fila_limitada = Queue(max_size=2)
    fila_limitada.enqueue("A")
    fila_limitada.enqueue("B")
    print(fila_limitada.is_full())

    teste_fila_vazia()
    teste_ordem_fifo()
    teste_peek()
    teste_clear()
    teste_dequeue_vazia()
    teste_max_size()