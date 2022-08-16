"""
faça um programa que possua um vetor A que amazene 6 numeros inteiros. passo:
a- atribua os sguintes valores a esse vetor 1, 0, 5, -3, -5, 7.
a = [1, 0, 5, -2, -5, 7]
print(a[0], a[1], a[5])
a[4] = 100
for x in a:
    print(x)
    -----------------------------
Crie um pograma que le 6 valores inteiros e em seguida exiba os 6 na tela


valor = [1, 4, 6, 77, 45, 88]

i = 0
while i < len(valor):
    print(valor[i])
    i = i + 1

3- LER UM VETOR DE 10 POSIÇOES. CONTAR E ESCREVER QUANTOS VALORES PARES ELE POSSUI
v = [11, 22, 54, 67, 88, 82, 90, 102, 43, 14]

for num in v:
    if num % 2 == 0:
        print(num)
4- faça um programa q leia um vetor de 8 pociçoes e em seguida leia um valor X e Y e some os valores e mostre


vetor = [33, 55, 89, 90, 76, 2, 6, 8]
x = vetor[3]
y = vetor[2]
num = (x + y)
print(vetor)

print('-' * 30)

print(f' O valor é X {x} e o valor Y é {y}')

print('-' * 30)

print(f'A Soma de X e Y é  {num} ...')

5 - faça um programa q receba do usuario 10 vetores e q mostre o maior e menos numero
num = []
valor = 0
for c in range(1, 11):
    valor = int(input(f'Digite o {c}° Numero : '))
    num.append(valor)
    print(f' Os Valores {num}')
print('o valor minimo é', min(num))
print('o valor maximo e', max(num))

5- gere 10 vetores inteiros, e imprima o valor max e sua posiçao

num = [10, 44, 5, 3, 2, 90, 77, 65, 32, 84]
n_max = max(num)
n_pos = num.index(n_max)
print(f'A posiçao é {n_pos}')

print(f'O maior Numero é {n_max} :')

6- crie um programa q le 6 numero int pares e inverta a ordem
#lista de valores
val = [2, 8, 12, 14, 18, 20]

val.reverse()
print(f'Os valores sao {val}')

7 - leia a nota de 15  alunos e mostre a note media geral

nota = [6, 8, 7, 8, 9, 5]

media = (nota[1] + nota[3]) / 2

print(f'A nota media é {media}')

8 - Fazer um programa para ler 5 valores e em seguida mostrar max, min, e med

lista = [50, 30, 10, 67, 194]
med = 0
m = max(lista)
n = min(lista)

# fazer a media da lista
for num in lista:
    med += num / 2

print(f' o Valor maximo é {m}  e o Minimo {n}')
print(f"Media dos valores -> {med}")

9 - fazer um programa pra ler 5 valores e em seguida, mostarr a posiçao onde s encotra o maior e menor valor

lista = [60, 20, 30, 40, 55]
print(f' O Menor Valor se encontra na posiçao {lista.index(min(lista))}')
print('-_-' * 15)
print(f' O Maior Valor se encontra na posiçao {lista.index(max(lista))}')

10 -> Crie um Programa que le 5 radios e mostre a porcentagem da bateria
lista = []
radio = ''

for c in range(1, 6):
     print('Digite o numero do radio ')
     radio = input()
     lista.append(radio)
     print(f'Temos {lista} de Radios')
11 - leia um vetor de 20 numeros inteiros, escreva elementos do vetor eliminando os repetidos
numero = {10, 10, 20, 45, 15, 15, 67, 85, 34,
          23, 56, 65, 65, 78, 93, 94, 123, 34, 34, 55}
print(numero)

12 - faça um vetor que leia 5 posiçoes paa cada numero
 """

lista = [22, 33, 45, 56, 67]
i = [1]

while lista < i:
    print('Numero invalido')
    break