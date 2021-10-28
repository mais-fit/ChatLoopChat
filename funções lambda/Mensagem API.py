import json

def lambda_handler(event, context):
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
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            'Content-type': 'application/json'
        },
        'body': json.dumps(dados)
    }
