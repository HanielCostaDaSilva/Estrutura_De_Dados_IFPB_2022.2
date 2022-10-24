from No import No

def preordem(no_inicial):
    if no_inicial is None:
        return
    print(f'{no_inicial.carga}', end=' ')
    preordem(no_inicial.esq)
    preordem(no_inicial.dir)


def emordem(no_inicial):
    if no_inicial is None:
        return
    emordem(no_inicial.esq)
    print(f'{no_inicial.carga}', end=' ')
    emordem(no_inicial.dir)


def posordem(no_inicial):
    if no_inicial is None:
        return
    posordem(no_inicial.esq)
    posordem(no_inicial.dir)
    print(f'{no_inicial.carga}', end=' ')


def busca(chave, no_inicial)->bool:
    if no_inicial is None:
        return False
    if no_inicial.carga == chave:
        return True
    if ( busca(chave, no_inicial.esq)):
        return True
    else:
        return busca(chave, no_inicial.dir)

raiz = No(10)
raiz.esq = No(32)
raiz.dir = No(23)
cursor = raiz.esq # cursor desce para o nó 32
cursor.esq = No(12)
cursor.dir = No(40)
cursor = cursor.esq
cursor.esq = No(5)
cursor = raiz.dir # cursor desce para o nó 23, a partir do raiz
cursor.dir = No(30)
cursor = cursor.dir # cursor desce para o nó 30
cursor.esq = No(60)
cursor = cursor.esq # cursor desce par ao nó 60
cursor.dir = No(22)

preordem(raiz)
print()
emordem(raiz)
print()
posordem(raiz)



