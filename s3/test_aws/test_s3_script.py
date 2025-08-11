# Initialize an S3 client
import boto3

# Set up the S3 client with the new user's credentials
s3 = boto3.client(
    's3',
    aws_access_key_id='<your-aws-access-key-id>',
    aws_secret_access_key='<your-aws-secret-access-key>',
    region_name='ap-south-1'  # or the region your resources are in
)


# Define your bucket name
bucket_name = '<your-bucket-name>'

# List all objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        print(f"Found object: {obj['Key']}")

# Read an object from the bucket
object_key = 'Details.csv'  # Specify the object key
response = s3.get_object(Bucket=bucket_name, Key=object_key)
data = response['Body'].read()  # Get the object content as bytes

# Print or process the data
print(data.decode('utf-8'))  # Decode as per your data's encoding