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

@app.route('/', methods=['GET'])
def get_home():
    return "Bem vindo a API de Livros do Michael"

@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def get_livro_id(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)


app.run(port=5000, host='localhost', debug=True)

