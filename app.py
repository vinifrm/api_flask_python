# ~/Google Drive/estudos/data science, machine learning, estatistica/Udemy/crie apis rest com python e flask/api
# código refatorando usando a técnica de TDD
import pandas as pd
from flask import Flask
from flask_restful import Api

def create_app():
    
    app = Flask(__name__) # armazena um nome único para esse arquivo; variável setada automaticamente pelo Python
    api = Api(app)

    app.run(port = 5000)

    return app

# exportar variáveis:
    # export FLASK_APP=app.py (qual é o aplicativo que inicializa o Flask)
    # export FLASK_ENV=development (ambiente aonde o Flask está sendo executado. No caso, está sendo executado no ambiente de testes)
# agora é possível rodar o projeto usando o comando "flask run"