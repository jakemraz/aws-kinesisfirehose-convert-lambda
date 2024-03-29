import base64
import json


def lambda_handler(event, context):
    output = []
    
    for record in event['records']:

        data = json.loads(base64.b64decode(record['data'].encode('utf-8')).decode('utf-8'))
        # transform here
        new = data['event_type']


        out_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(new).encode('utf-8')).decode('utf-8')
        }
        output.append(out_record)
    return {'records': output}
    
