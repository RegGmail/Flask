
from flask import Flask, jsonify, request

app = Flask (__name__)

lista_tarefas = [
    {'id':'1', 'task':'Comprar material'},
    {'id':'2', 'task':'Aprender Flask'}
]

@app.route ('/lista_tarefas', methods = ['GET'])
def get_lista_tarefas ():
    return jsonify (lista_tarefas)

@app.route ('/lista_tarefas/<int:tarefa_id>', methods = ['GET', 'DELETE'])
def tarefa(tarefa_id):
    print ("tarefa_id", tarefa_id)

    achou = None
    """
    for acao in lista_tarefas:
        print (f"acao['id'] = ", acao['id'])
        print ("acao", acao)
        print ("comparando ", acao['id'], tarefa_id)

        if int(acao['id']) == tarefa_id:
            print ("achou igual ", acao['id'], tarefa_id)
            break # achou
    """
    acao = next((acao for acao in lista_tarefas if int(acao['id']) == tarefa_id), None)
    achou = acao

    print ("acao", acao)
    print ("request", request.method)

    if not achou:
        return jsonify({'error': 'Tarefa nao encontrada'}), 404
    
    if request.method == 'GET':
        return jsonify (acao)
    
    elif request.method == 'DELETE':
        lista_tarefas.remover(acao)
        return jsonify ({'message':'Tarefa deletada'}), 204
    
if __name__ == '__main__':
    app.run (debug=True)

    