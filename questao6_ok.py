"""
O DBA da empresa criou um script para fazer uma atualização no banco de dados MongoDB:

    var sku = ""        // a pessoa informa o sku aqui
    var estoque = 0     // valor a ser informado do novo estoque
    db.produto.update({sku: sku}, {$inc: estoque})

O problema é que esse script está em JavaScript do MongoDB.
Logo, escreva para nós uma função Python ajustar_estoque()
com o seus devidos parâmetros, para que realize a atualização
na coleção produto conforme o script que o DBA passou para nós.
"""

from pymongo.collection import Collection

def ajustar_estoque(sku:str, estoque:int, collection:Collection) -> None:
    collection.find_one_and_update({"sku": sku},
                                   {"$inc": {"estoque": estoque}})