import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'message': 'Hello world {}'.format(event['name']), 
        'body': json.dumps('Hello from Lambda!')
    }
