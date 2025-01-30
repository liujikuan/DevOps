


# Payment API Application

This project is a **serverless payment API** built using **AWS SAM (Serverless Application Model)**. It leverages AWS services such as **API Gateway, Lambda, DynamoDB, and Cognito** to provide a secure and scalable payment processing system.

## Architecture

The application follows a **multi-tier architecture**:

- **Front Tier:** AWS API Gateway (Handles incoming HTTP requests)
- **Logic Tier:** AWS Lambda (Business logic for payment processing)
- **Data Tier:** Amazon DynamoDB (Stores payment data)
- **Authentication & Authorization:** AWS Cognito (Manages user authentication)

## Features

- **Create a Payment** – Users can initiate a payment request.
- **Retrieve Payment Details** – Users can fetch details of a specific payment.
- **User Authentication** – AWS Cognito ensures secure access.

## Technologies Used

- **AWS Lambda** (Serverless backend)
- **AWS API Gateway** (RESTful API)
- **Amazon DynamoDB** (NoSQL database)
- **AWS Cognito** (User authentication)
- **AWS SAM** (Infrastructure as Code)

## Project Structure

```
📂 root
│── create_payment/
│   └── app.py        # Lambda function to create payments
│── get_payment/
│   └── app.py        # Lambda function to retrieve payments
│── template.yaml     # AWS SAM template for infrastructure
│── README.md         # Documentation
└── events/           # Sample API request payloads

```

## Prerequisites

Before deploying the project, ensure you have:

- **AWS CLI** installed and configured (`aws configure`)
- **AWS SAM CLI** installed ([Install AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html))
- **Python 3.10+** installed

## Deployment Steps

### 1. Clone the Repository
```bash
git clone https://github.com/liujikuan/DevOps.git
cd payment-api
```

### 2. Build the Application
```bash
sam build
```

### 3. Deploy the Application
```bash
sam deploy --guided
```
Follow the prompts to configure deployment settings.

### 4. Testing the API

#### Create a Payment
```bash
curl -X POST https://<your-api-id>.execute-api.region.amazonaws.com/prod/payment \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <your_cognito_access_token>" \
    -d '{"amount": 100, "currency": "USD"}'
```

#### Get Payment Details
```bash
curl -X GET https://<your-api-id>.execute-api.region.amazonaws.com/prod/payment?paymentId=<payment_id> \
    -H "Authorization: Bearer <your_cognito_access_token>"
```

## Cleanup

To remove all deployed resources:
```bash
sam delete
```

## Future Improvements

- Implement a **payment status update** feature.
- Integrate with external payment gateways (e.g., Stripe, PayPal).
- Add logging and monitoring with **AWS CloudWatch**.

