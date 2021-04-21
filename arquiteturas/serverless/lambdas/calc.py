import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    res = { }
    res['resultado'] = "calc está funcionando! Versão 1.0"
    return json.dumps(res)    
    #raise Exception('Something went wrong')

