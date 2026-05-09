lista_frutas = ["Banana", "maçã", "Morango"]

print(lista_frutas[1])
#lista_frutas[0] = Banana
#lista_frutas[1] = Maçã
#lista_frutas[2] = Morango

lista_frutas.append("uva")
print(lista_frutas[-1])

tamanho = len(lista_frutas)
print(tamanho)
print()

for i in range(tamanho):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)

