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

#Aqui o "var" e o "copia" apontam para o mesmo endereço de memória (Em pythom se eu copiar uma lista ele vai apontar para o endereço da lista original)
var = ['abcd',1,2,3]
copia = var
var.append("fghi")
print(var)
print(copia)

#Com a função copy() a variavel "copia" cria um novo endereço de memoria, e não aponta para o endereço da variavel ao qual foi copiado
var = ['abcd',1,2,3]
copia = var.copy()
var.append("fghi")
print(var)
print(copia)