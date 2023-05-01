import json

def lambda_handler(event, context):
    print('Received request:', event)
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps( {'msg': 'Sample response from Lambda!', 'incoming_event': event })
    }
    print('Returning response:' , response)
    return response

