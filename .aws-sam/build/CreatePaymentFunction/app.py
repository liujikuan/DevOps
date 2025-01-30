import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = event.get('body', {})
    if not body:
        return {"statusCode": 400, "body": "Invalid input"}

    payment_id = str(uuid.uuid4())
    payment = {
        "PaymentId": payment_id,
        "Amount": body.get("amount"),
        "Currency": body.get("currency"),
        "Status": "Pending"
    }
    
    table.put_item(Item=payment)
    
    return {
        "statusCode": 200,
        "body": f"Payment created with ID: {payment_id}"
    }
