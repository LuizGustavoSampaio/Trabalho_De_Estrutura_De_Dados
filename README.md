# Trabalho_De_Estrutura_De_Dados

# Queue em Python

Este projeto implementa uma **fila (Queue)** em Python usando uma classe simples.

## O que é uma fila?

Uma fila segue o conceito **FIFO**:

**First In, First Out**  
Ou seja, o primeiro elemento que entra é o primeiro que sai.

Exemplo:
- entra: `A`, `B`, `C`
- sai: `A`, depois `B`, depois `C`

## Funcionalidades

A classe `Queue` possui os seguintes métodos:

- `enqueue(item)` → adiciona um item no final da fila
- `dequeue()` → remove e retorna o primeiro item
- `peek()` → mostra o primeiro item sem remover
- `is_empty()` → verifica se a fila está vazia
- `is_full()` → verifica se a fila está cheia
- `size()` → retorna a quantidade de itens
- `clear()` → limpa toda a fila

## Como funciona

A fila guarda os dados em uma lista interna e permite:

- adicionar elementos no final
- remover elementos do começo
- controlar tamanho máximo, se for definido

## Exemplo de uso

```python
fila = Queue()
fila.enqueue("Cliente 1")
fila.enqueue("Cliente 2")
fila.enqueue("Cliente 3")

print(fila)
print(fila.dequeue())
print(fila.peek())