# -*- coding: utf-8 -*-
"""aula5e6_programaçao_em_python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H_3xlHKPMA0o2P8cT-pOgVNxO-kVkbgy
"""

text = 'Olá Mundo'
lista = list(text)
print(lista)

numero = [1,2,5,4,2,8]
soma = sum(numero)
print (soma)

n = range(1,10)
print (n)
for n in range (1,10):
  print (n)

Loop for
serve para evitar retrabalhos, evita digitar muitas vezes um algoritmo

print ('Olá mundo')
print ('Olá mundo')
print ('Olá mundo')
print ('Olá mundo')
print ('Olá mundo')
print ('..........')
for i in range (1,6):
  print ('Ola Mundo' ,i)

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

lista = [1,3,6,89,78,15,56]
for n in lista:
  print (n)

for n in range(1,201):
  print(n)

menino = {
    'nome' : 'Carlos',
    'idade' : '17',
    'endereco': 'rua 10'
}

for key, value in menino.items():
  print (value)

for linha in matriz:
    for elemento in linha:
        print(elemento)

for i in range (1,11,3):
   print(i)

Exercício 1: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

for pares in range (2,22,2):
  print(pares)

Exercício 2: Escreva um programa que use a função range() para gerar os múltiplos de 5 em 5 a 50 e, em seguida.
for n in range (5,55,5):


  print (n)
  print (sum(range(5,55,5)))

  Exercício 3: Escreva um programa que use a função type() para verificar o tipo de uma variável.

number = 100
tipo = type(number)
print(tipo)

words = 'hello words'
r = type(words)
print (r)



Exercício 4: Escreva um programa que use a função print() para imprimir uma mensagem de saudação personalizada, incluindo o nome do usuário.

name = input('digite seu nome')
print ('Bem Vinda ', name)

name = input ('Digite seu nome')
hello = ('Hello')
print(hello+ ' ', name)


**Exercício 5:** Escreva um programa que use a função `range()` para gerar os números ímpares de 1 a 10 .

for i in range (1,11,2):
  print (i)


soma = sum(range(1,11,2))
print (soma)

Listas:

n= [2,3,6,89,45]
index_one = n[4]
print(index_one)



n= [2,3,6,89,45]
add = n.append(10)
add2 = n.append(5)
remove = n.pop()

remove2 = n.remove(3)
del n[0]
print(n)



n= [2,3,6,89,45]
comprimento = len (n)
print (comprimento)

Exercício 1: Crie uma lista chamada numeros que contenha os números inteiros de 1 a 5 e imprima-a na tela.

numero = list[1,2,3,4,5]
print (numero)


Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.

terceiro_elemento = list[4]
print (terceiro_elemento)


**Exercício 3:** Adicione o número 6 à lista `numeros` e imprima a lista atualizada.

numero = [1,2,3,4,5]
add = numero.append(6)
print (numero)


Exercício 4: Remova o número 3 da lista numeros e imprima a lista resultante.
numero = [1,2,3,4,5]
remove = numero.remove(3)
print (numero)


Exercício 5: Crie uma lista chamada frutas contendo três nomes de frutas diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.

numero = [1,2,3,4,5]
frutas = ['Banana', 'Maça', 'Morango']
juntar = frutas,numero
print (juntar)

Exercício 6: Use um loop for para percorrer e imprimir todos os elementos da lista frutas.


frutas = ['Banana', 'Maça', 'Morango']
for i in frutas:
     print(i)