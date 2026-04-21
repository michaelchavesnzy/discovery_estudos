from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id" : 1,
        "titulo": "O senhor dos Anéis",
        "autor": "J.R.R. Tolkien"
    },
    {
        "id" : 2,
        "titulo": "Entendendo Algortimos",
        "autor": "Adytia"
    },
    {
        "id" : 3,
        "titulo": "Fundamentos da Engenahria de Dados",
        "autor": "Matt"
    } 
]

#home da API
@app.route('/', methods=['GET'])
def get_home():
    return "Bem vindo a API de Livros do Michael"

#obter os livros
@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros)

#obter 1 livro id específico
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro_id(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
        
#atualizar info de um livro
@app.route('/livros/<int:id>', methods=['PUT'])     
def editar_livro_por_id(id):
    #requisicao do usuário
    livro_alterado = request.get_json()

    for indice, livro in enumerate(livros):
        if livro['id'] == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar novo livro
@app.route('/livros', methods=['POST'])      
def criar_novo_livro():

    livro_novo = request.get_json()
    livros.append(livro_novo)

    return f'titulo {livro_novo['titulo']} inserido com sucesso!'

#deletar um livro
@app.route('/livros/<int:id>', methods = ['DELETE'])
def excluir_livro(id):

    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)

