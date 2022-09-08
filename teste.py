"""
fazer um programa q determine e mstre os 5 primeiros multiplos de 3 considerando numeor maior q 0
for num in range(3, 16, 3):
    print(num)
    num = num + 1
    ---------------------------
escreva um programa que escreva de 1 a sem, no for, while e do while
for num in range(0, 100, 1):
    print(num + 1 )
------------------------
num = 1
while num < 100:
    if num == 101:
        break
    else:
        print(num)
        num = num + 1
        -----------------------
        fazer um programa de contagem regressiva no while 10 a 1
num = 10
while num > 0:
    if num == 1:
        break
    else:
        print(num)
        num = num - 1
    --------------------------
    peça o usuario para digitar 10 valores e some
    soma = 0
cont = 0
for c in range(1, 11):
    num = int(input(f'Digite o valor {c}:  '))
    soma += num
    cont += 1
print(f'Seus {cont} valores deram {soma}')
---------------------------------
faça um programa que mostre os 20 primeiros numeros e some os pares
soma = 0
cont = 0
for c in range(1, 21):
    num1 = int(input(f"Digite o valor {c}: "))
    if num1 % 2 == 0:
        soma += num1
        cont += 1
print(f"Seus {cont} Valores deram {soma}")
-------------------------------


"""
