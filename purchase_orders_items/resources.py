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

class PurchaseOrdersItems(Resource): # recurso

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
    parser.add_argument( # define-se os parâmetros da requisição desejados
        'price',  # alterado para 'descricao' para manter consistência
        type = float,
        required = True,
        help = 'Informe um preço' # mensagem caso o parâmetro esteja incorreto
    ) 

    def get(self, id):

        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['items'])
    
        return jsonify({'message': 'Id {} de pedido não encontrado'.format(id)})
    
    def post(self, id):

        req_data = PurchaseOrdersItems.parser.parse_args() # pega o json que chega na requisição

        for po in purchase_orders:
            if po['id'] == id:
                po['items'].append(
                    {
                        'id': req_data['id'],
                        'description': req_data['description'],
                        'price': req_data['price']
                    }
                )

                return jsonify(po)
            
        return jsonify({'message': 'Id {} de pedido não encontrado'.format(id)})