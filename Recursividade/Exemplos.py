def contador(final, numero=0):
    print(numero, end=' ')
    if numero < final:
        contador(final, numero + 1)


n = 10
print('===Contando====')

contador(n)

print('')


def soma(a, b):
    if a != b:
        #print(, a, end=' ')
        a += soma(a + 1, b)
    return a


print('===Somando====')
#j=int(input('j: '))
j = 1
#l=int(input('l: '))
l = 5
print('\n' + str(soma(j, l)))


def Maior(a: list):
    if len(a) == 0:
        raise Exception('Array Vazio')
    elif len(a) == 1:
        return a[0]

    return max(Maior(a[1:]), array[0])


print('===Maior====')
array = [1, 2, 34, 4, 54, 5, 56, 66, 7, 66, 76, 7, 65, 435, 67, 6, 7887, 54, 5]
print(Maior(array))