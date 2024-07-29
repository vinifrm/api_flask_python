# é uma boa prática deixar os recursos e/ou rotas em um arquivo separado
# também é uma boa prática inicializar a pasta como um módulo, com um arquivo __init__.py

from flask import jsonify
from flask_restful import Resource

purchase_orders = [
    { # dicionário que vai conter os pedidos de compra, com os itens pedidos
    'id': 1,
    'descricao': 'Pedido de compra',
    'items': [
        {
            'id': 1,
            'descricao': 'Item do pedido 1',
            'preco': 20.99
        }
            ]
    } 
]

# para criar um recurso, vamos criar uma classe
# deve herdar da classe Resource

class PurchaseOrders(Resource):

    # já temos as funções get e post para serem sobrescritas
    # deve retornar um json em memória
    def get(self):

        return jsonify(purchase_orders)

# utilizar o flask restful para expor/configurar o endpoint que será relacionado ao recurso
# usar a função add resource
