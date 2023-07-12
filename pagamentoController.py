from flask import Blueprint, jsonify, request  # Importação de funcionalidades.
import uuid

pagamentoDTO = Blueprint('pagamento', __name__)  # Registro de um blueprint para pagamento e criação de rotas.

pagamentos = {}  # É uma lista de registro de pagamentos vazia.
global contadorId


@pagamentoDTO.route('/pagamentos/salvar',
                    methods=['POST'])  # POST é um comando que permite fazer publicação de comandos/atributos.
def salvar_pagamento():
    dto = request.get_json()
    print(dto)

    id = str(
        uuid.uuid4())  # uuid é uma estratégia de geração de caracteres aleatórios de forma que lese não se repitam.
    pagamentos[id] = dto
    response = {'message': 'Pagamento Salvo com sucesso!'}
    return jsonify(response), 200


@pagamentoDTO.route('/pagamentos/listar', methods=['GET'])
def listar_pagamentos():  # def é uma maneira de definir métodos.
    response = pagamentos
    return jsonify(response), 200


@pagamentoDTO.route('/pagamentos/deletar', methods=['DELETE'])
def deletar_pagamentos(dto=None):
    id_remocao = request.args.get('id')
    if pagamentos.get(id_remocao, None) != None:
        x = pagamentos.pop(id_remocao)
        print(x)
        response = {'message': 'id ' + id_remocao + ' deletado'}
        return jsonify(response), 200
    else:
        response = {'message': 'id' + id_remocao + ' não encontrado!'}
        return jsonify(response), 200



@pagamentoDTO.route('/pagamentos/id', methods=['GET'])
def get_id():
    id_identificacao = request.args.get('id')

    response = pagamentos.get(id_identificacao)
    return jsonify(response), 200


# Percorrer dicionário, identificar o id e removê-lo(retornar mensagem com sucesso ao remover ou não encontrado).
