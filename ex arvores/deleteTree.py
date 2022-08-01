# Exclusão de nó em árvore binária

class Node:

    # construtor da classe
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # função para o BST


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Função para inserir um novo Nodo
def insert(node, key):
    if node is None:  # se a árvore estiver vazia retorna um novo nó
        return Node(key)
    # senão, busca na árvore
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# encontra o menor valor (Nodo)
def minValueNone(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def deleteNode(root, key):
    if root is None:
        return root

    # Se a chave a ser excluída é menor que o Nó Raiz
    if key < root.key:
        root.left = deleteNode(root.left, key)
    # se for maior, está na direita
    elif key > root.key:
        root.right = deleteNode(root.right, key)

    else:
        # Quando o nó possui um filho ou nenhum
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # quando possuir dós nó, obtem o sucessor na pré-ordem
        temp = minValueNone(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)
    return root


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Árvore em Ordem")
inorder(root)

print("\nApagando o 20")
root = deleteNode(root, 20)
print("Imprimindo árvore em ordem após exclusão do 20")
inorder(root)
