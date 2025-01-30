import boto3
import os

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    # Extract the payment ID from the query parameters
    payment_id = event.get('queryStringParameters', {}).get('PaymentId')
    
    if not payment_id:
        return {
            "statusCode": 400,
            "body": "PaymentId is required as a query parameter."
        }
    
    try:
        # Retrieve the payment item from DynamoDB
        response = table.get_item(Key={"PaymentId": payment_id})
        payment = response.get('Item')
        
        if not payment:
            return {
                "statusCode": 404,
                "body": f"No payment found with PaymentId: {payment_id}"
            }
        
        # Return the payment details
        return {
            "statusCode": 200,
            "body": payment
        }
    
    except Exception as e:
        # Handle unexpected errors
        return {
            "statusCode": 500,
            "body": f"An error occurred: {str(e)}"
        }
