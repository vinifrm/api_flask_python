# é uma boa prática deixar os recursos e/ou rotas em um arquivo separado
# também é uma boa prática inicializar a pasta como um módulo, com um arquivo __init__.py

from flask import jsonify
from flask_restful import Resource, reqparse # definir e resgatar conteudo do corpo de uma requisição

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

    parser = reqparse.RequestParser()
    parser.add_argument( # define-se os parâmetros da requisição desejados
        'id',
        type = int,
        required = True,
        help = 'Informe um id' # mensagem caso o parâmetro esteja incorreto
    ) 
    parser.add_argument( # define-se os parâmetros da requisição desejados
        'description',  # alterado para 'descricao' para manter consistência
        type = str,
        required = True,
        help = 'Informe uma descrição' # mensagem caso o parâmetro esteja incorreto
    ) 

    # já temos as funções get e post para serem sobrescritas
    # deve retornar um json em memória
    def get(self):
        return jsonify(purchase_orders)

    def post(self):
        purchase_data = PurchaseOrders.parser.parse_args() # pegando os parâmetros inseridos no corpo da requisição
        purchase_order = {
            'id': purchase_data['id'],
            'description': purchase_data['description'],  # alterado para 'descricao' para manter consistência
            'items': []
        }

        purchase_orders.append(purchase_order)

        return jsonify(purchase_order)
