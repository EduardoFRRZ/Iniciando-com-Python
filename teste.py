people = 29
cats = 10
dogs = 15

print (people)
print (people - cats)

#If em Python
if people > cats:
	print("Pessoas = 29")

#Lista
lista = [1,2,3,4,5, 'Eduardo']

#for percorendo a lista
for item in lista:
	print(item)

for posicao in range(0,6):
	print(lista[posicao])
	print(posicao)

for posicao in range(0,len(lista)):
	print(lista[posicao])
	print(posicao)
	print("Elemento %d : %s" %(posicao, lista[posicao]))

#Função
def funcao():
	print("Minha funcao")
funcao() #Chamada da função

def funcao2(x):
	print("Minha funcao 2 -> x =", x)

x = 10
funcao2(x)


