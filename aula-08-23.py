from math import sqrt

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if a != 0:
    delta = b * b - 4 * a * c

    if delta < 0:
        print('/nDelta e negativo, logo nao ha solucao real!')
    else:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print('')
        print('O valor de x1 e:', x1)
        print('O valor de x2 e:', x2)

else: 
    print('/nO valor de "A" deve ser diferentes de zero')

print('Fim do Calculo')