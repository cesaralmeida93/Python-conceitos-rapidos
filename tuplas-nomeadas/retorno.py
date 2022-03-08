# pylint: disable-all

def minha_lista():

    return {
        "frutas": ["maçã", "uva", "abacate"],
        "local": "rua das laranjeiras",
        "supermercados": 2,
        "extras": {"doces": "chocolates", "sucos": "Morango"} 
    }

lista = minha_lista()
# processamento

lista["frutas"] = "Qualquer coisa"

print(lista)