# ~/Google Drive/estudos/data science, machine learning, estatistica/Udemy/crie apis rest com python e flask/api
import pandas as pd
from flask import Flask
from flask_restful import Api
from purchase_orders.resources import PurchaseOrders

app = Flask(__name__) # armazena um nome único para esse arquivo; variável setada automaticamente pelo Python
api = Api(app)

# utilizar o flask restful para expor/configurar o endpoint que será relacionado ao recurso
# usar a função add resource
api.add_resource(PurchaseOrders, '/purchase_orders')
# api.add_resource(PurchaseOrders, '/purchase_orders')

app.run(port = 5000)