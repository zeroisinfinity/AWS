
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
    print(resp)
    obj_list = []
    for obj in resp['Contents']:
        obj_list.append(obj['Key'])
    return obj_list

def copy_objs(src_bucket,dest_bucket,key):
    client.copy_object(
                        Bucket = dest_bucket , 
                        CopySource = "/{}/{}".format(src_bucket,key),
                        Key = key
                        )
    return True
    
def lambda_handler(event, context):
    
    
    objs = ls_obj(source_bucket)

    print(objs)
    
    for file in objs:
        
        if copy_objs(source_bucket,destination_bucket,file):
            del_objs(source_bucket,file)
        else:
            print("Problem occurred in copying.")
    else:
        print("Moving successfull")
    
        
    return True
def main():
    lambda_handler(event, context)
    return True
if __name__ == "__main__":
    main()
        
        






