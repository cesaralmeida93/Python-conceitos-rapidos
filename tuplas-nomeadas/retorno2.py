# pylint: disable-all

from collections import namedtuple

MyList = namedtuple("Compra", "frutas local supermercados extras")


def minha_lista():
    return MyList(
        frutas=["maçã", "uva", "abacate"],
        local="rua das laranjeiras",
        supermercados=2,
        extras={"doces": "chocolates", "sucos": "Morango"} 
    )

def minha_lista2():
    return MyList(
        frutas=["Pera", "Banana"],
        local="rua das oliveiras",
        supermercados=1,
        extras={"doces": "chocolates"} 
    )

lista = minha_lista()
lista2 = minha_lista2()
print(lista)
print(lista2)