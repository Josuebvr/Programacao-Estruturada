from collections import deque

pilha = deque()

pilha.append("a")
pilha.append("b")
pilha.append("c")

print("Elementos da pilha: ")
print(pilha)

print("\nElemento removido: ")
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())

print("\nElementos da pilha: ", pilha)
print(pilha)