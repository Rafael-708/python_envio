# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
from pagamentoController import pagamentoDTO

app = Flask(__name__) #Flask atribue_name da aplicação.
app.register_blueprint(pagamentoDTO) #Isto serve para fazer o registro de pagamentos.

if __name__ == '__main__': #if é uma estrutura de decisão que basicamente define e garante que __name__ existe para ser executado."
    app.run()

