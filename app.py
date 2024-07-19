# ~/Google Drive/estudos/data science, machine learning, estatistica/Udemy/crie apis rest com python e flask/api
import pandas as pd
from flask import Flask, jsonify

# decorators e rotas -> 
    # a função deve estar atrelada a uma rota; a função será executada quando a rota for a especificada
    # embrulha uma função e altera o comportamento daquela função
    # quando usamos, vamos executar outras coisas antes ou junto com a função
    # Quando você define uma rota em Flask, você associa uma URL a uma função, que processa as requisições e retorna respostas
    # O nome desta função é, por padrão, também usado como o nome do endpoint


# rota GET
    # um endpoint: um endpoint refere-se ao nome de uma função view que é mapeada a uma ou mais rotas URL. Basicamente, é o ponto de extremidade ao qual uma requisição HTTP é enviada para obter um recurso específico, como uma página da web, dados, ou para executar uma ação no servidor
    # 

app = Flask(__name__) # armazena um nome único para esse arquivo; variável setada automaticamente pelo Python
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


# função para retornar os pedidos (lista) (GET)
    # apenas retornar um json
    # verificar a rota no navegador
    #
@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)

# função para retonar os pedidos usando filtro por id (GET)
@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
        
    return jsonify({'message': 'Pedido {} não encontrado'.format(id)})

# endpoint aonde será possível inserir um novo pedido (POST)


# função para obter os itens de pedido especifico


# função para inserir um novo item



# função home para retornar o hello world
@app.route('/')
def home():
    return 'Hello, World!'

app.run(port = 5000)