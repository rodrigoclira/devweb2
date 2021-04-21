import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    op1 = event['queryStringParameters']['op1']
    op2 = event['queryStringParameters']['op2']
    res = { }
    res['resultado'] = float(op1) + float(op2)
    return json.dumps(res)  # Echo back the first key value
    #raise Exception('Something went wrong')

