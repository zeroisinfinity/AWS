

import json
import boto3

client = boto3.client('s3')


def lambda_handler(event, context):
    # TODO implement
    #print(event['Records'][0]["object"]["key"])
    response = client.list_objects(Bucket='<your-bucket-name>')['Contents']
    for obj in response:
        filename = obj["Key"]
        print(filename)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
