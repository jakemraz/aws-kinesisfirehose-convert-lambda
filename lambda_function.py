import base64
import json


def lambda_handler(event, context):
    # TODO implement
    output = []
    test_data = {
        'name': 'jakemraz',
        'age': 13
    }
    for record in event['records']:

        # transform here

        out_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(test_data).encode('utf-8')).decode('utf-8')
        }
        output.append(out_record)
    return {'records': output}
    
