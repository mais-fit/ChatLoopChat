from flask import Flask , jsonify, request
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)
    
@app.route("/") 
def hello(): 
    return "Hello World?? reload!"

dados = {"mensagem":[
    {
        "usuario": "Lucas",
        "texto": "Oi",
        "id": "1"
    },
    {
        "usuario": "Karol",
        "texto": "Oi xD",
        "id": "2"
    },
    {
        "usuario": "Lucas",
        "texto": "Tudo bem?",
        "id": "3"
    },
    {
        "usuario": "Karol",
        "texto": "Tudo sim! E você?",
        "id": "4"
    },
    {
        "usuario": "Lucas",
        "texto": "Estou bem :D",
        "id": "5"
    }
]}
#criar uma url para atender um pedido na 
# /alunos com o verbo get

@app.route("/mensagem", methods=['GET']) #espeficiquei o verbo. Como era GET nao precisava, mas eu quis
def get_alunos():
    #return dados["alunos"] #esse return dá problema. O flask basicamente espera uma string ou um dict
    return jsonify(dados["mensagem"]) 


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)