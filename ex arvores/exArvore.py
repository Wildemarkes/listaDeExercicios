# Atividade Final
# Ex. 01:
# Escreva uma TAD de arvore binária de pesquisa ABP
# com as seguintes operações:
# a) Inserir um elemento; ok
# b) Remover um elemento; ok
# c) Caminhamento central a esquerda;
# d) Caminhamento central a direita;
# e) Copiar uma lista com inteiros para a ABP;
# Escreva uma TAD de arvore binária de pesquisa ABP com balanceamento AVL
# a) Inserir na arvore AVL;
# b) Remover da arvore AVL;

# nodos de árvore binaŕia possum um valor chamado de chave
class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s ->%s' % (
            self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)


raiz = NodoArvore(40)  # nó raiz (chave)

raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)

raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)

raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)


def em_ordem(raiz):
    if not raiz:  # se não for o nó raiz
        return

    # visita filho da esquerda
    em_ordem(raiz.esquerda)

    # visita o nodo corrente
    print(raiz.chave)

    # visita filho da direita
    em_ordem(raiz.direita)


em_ordem(raiz)


def insere(raiz, nodo):
    """Insere um nodo em uma árvore binária de pesquisa"""
    # Nodo deve ser inserido na raiz.
    if raiz is None:
        raiz = nodo

    # Nodo deve ser inserido na subárvore direita.
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    # Nodo deve ser inserido na subárvore
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)


print("copiar lista de inteiros para ABP")
# cira uma ABP
raiz = NodoArvore(40)  # insere um nodo base
for chave in [25, 50, 60, 73, 18, 32]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

# mostra o caminhamento em ordem da árvore
em_ordem(raiz)


def busca(raiz, chave):
    """Procura por uma chave em árvore binaŕia de pesquisa"""
    # Trata o caso em que a chave procurada não está presente
    if raiz is None:
        return None

    # A chave procurada está na raiz da árvore
    if raiz.chave == chave:
        return raiz

    # A chave procurada é maior que a da raiz.
    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    # A chave procurada é menor que a da raiz.
    return busca(raiz.esquerda, chave)


print("Buscando a chave")

# Procura por valores na árvore
for chave in [-50, 10, 30, 73, 100]:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))
