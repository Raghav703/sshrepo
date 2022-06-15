import boto3

def handler(event,context):
    print ("welcome to lambda")

    return {

            statuscode:200
            body: json.dumps("hello world")
            }^S     
