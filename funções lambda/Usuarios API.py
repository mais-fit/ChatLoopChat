import json

def lambda_handler(event, context):
    dados = {"usuarios":[
    {
        "login": "KauanAmorim",
        "password": "estudo123",
    },
    
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