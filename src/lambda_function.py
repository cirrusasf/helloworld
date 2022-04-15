def lambda_handler(event, context):

    return {
        'message': 'Hello world, {}'.format(event.get('name'))
    }
