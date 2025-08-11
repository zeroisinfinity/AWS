
import json
import boto3

client = boto3.client("s3")
source_bucket = "<your-source-bucket>"
destination_bucket = "<your-destination-bucket>"


def del_objs(bucket, file_key):
    client.delete_object(Bucket=bucket, Key=file_key)
    return True


def ls_obj(bucketname):
    resp = client.list_objects(Bucket=bucketname)

    obj_list = []
    for obj in resp['Contents']:
        obj_list.append(obj['Key'])
    return obj_list


def lambda_handler(event, context):
    print(f"Event is {event['Records'][0]['s3']['object']['key']}")
    objs = ls_obj(source_bucket)
    bucket = source_bucket
    print(objs)
    for file in objs:
        if del_objs(bucket, file):
            objs.remove(file)
        else:
            break
    else:
        print("All are deleted")

    print(
        "###############################################################################################################################")
    print("Checking again")
    print(
        "###############################################################################################################################")
    if objs:
        for file in objs:
            print(
                "###############################################################################################################################")
            print(file, "Yet to delete")
            print(
                "###############################################################################################################################")

    else:
        print("Everything is deleted")
    return True






