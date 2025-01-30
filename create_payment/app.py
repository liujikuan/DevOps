import boto3
import uuid
import os
import json

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        # Get body from the event
        body = event.get('body', {})

        # If the body is a string, parse it into a dictionary
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except json.JSONDecodeError:
                return {"statusCode": 400, "body": json.dumps({"error": "Invalid JSON format"})}

        # Validate required fields
        if not isinstance(body, dict) or "amount" not in body or "currency" not in body:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing required fields: amount, currency"})}

        # Generate unique Payment ID
        payment_id = str(uuid.uuid4())

        # Construct payment item
        payment = {
            "PaymentId": payment_id,
            "Amount": body["amount"],
            "Currency": body["currency"],
            "Status": "Pending"
        }

        # Insert into DynamoDB
        table.put_item(Item=payment)

        # Successful response
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Payment created", "PaymentId": payment_id})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        print(f"Body type: {type(body)}")  # Print the type of 'body'
        return {
           "statusCode": 500,
           "body": json.dumps({"error": str(e), "body_type": str(type(body))})
        }
