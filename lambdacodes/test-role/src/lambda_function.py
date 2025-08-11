import json

def user_split(ee):
    return ee.split(".")[-1]
def lambda_handler(event, context):
    # TODO implement
    e = "sahil2011@gmail.com"
    return user_split(e)