This repository contains various DevOps-related projects, each stored in a different branch. Below is an overview of each project along with instructions to access and use them.

# Table of Contents
- [Serverless Payment API](https://github.com/liujikuan/DevOps/tree/serverlessPaymentAPI)

- [GitHub API Automation Tool](https://github.com/liujikuan/DevOps/tree/GithubAPIAutomationTool)

- [2-factor authentication](https://github.com/liujikuan/DevOps/tree/2FA)

- [Service Container & RedisClient](https://github.com/liujikuan/DevOps/tree/serviceContainerAndRedisClient)

- [Secrets & Variables in Github Actions](https://github.com/liujikuan/DevOps/tree/envVar) 
  
- [python CI/CD azure](https://github.com/liujikuan/DevOps/tree/python-cicd-azure)


# Serverless Payment API

**Branch:** `serverlessPaymentAPI`

**Description:**

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

## Setup Instructions:

### *Install AWS SAM CLI*

AWS SAM CLI is required to build and deploy the serverless application. Install it by following these steps:

```bash
curl -Lo sam-installation.zip https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
unzip sam-installation.zip -d sam-installation
sudo ./sam-installation/install
```

# GitHub API Automation Tool
**Branch:** `GithubAPIAutomationTool`

**Description:**
This is a Python-based DevOps utility that interacts with the GitHub REST API to simulate a scenario where developers need to streamline feature delivery using automation tools.

It automates the following Continuous Integration steps:

- Creating a new branch from a base branch
- Committing a new file to that branch
- Creating a pull request (PR) from the branch
- (Optional) Triggering GitHub Actions workflows manually

**📌Features:**

- 🔧 Fully scriptable via Python and GitHub API
- 📤 Automates pull request creation
- 🚀 Easy to integrate into CI/CD pipelines
- 🔐 Secure configuration using external JSON file (token not hardcoded)



# 2-Factor Authentication

**Branch:** `2FA`

**Key Features:**

● Developed web interfaces for two-factor authentication using ***Java*** to mitigate unauthorized access, enhancing security for users.

● To improve security for applications, integrated a source code scanning plugin into a ***Jenkins*** pipeline, triggered by new commits to GitHub. Upon receiving a vulnerability clearance report outputted by the plugin, the pipeline automatically provisions virtual machines on ***Azure***, reducing the manual error.

● Built CI/CD pipelines using GitHub actions, automating testing, building, and deployment processes.

**Tech Stack:** JAVA, Jenkins, Azure, GitHub Actions



# Service Container & Redis Client

**Branch:** `serviceContainerAndRedisClient`

**Description:**

This repository contains a sample **JavaScript GitHub Action** that interacts with a Redis service container which would be destroyed when the job completes.

The workflow has two jobs demonstrating the difference between a job running in a container and a job running on an Ubuntu runner while connecting to a service container.

# Secrets & Variables in Github Actions

**Branch:** `envVar` 

**Description:**
This GitHub Actions workflow demonstrates how to use secrets and variables at different scopes, including workflow-level, job-level, environment-level, and repository-level.

# Python CI/CD Azure

**Branch:** `python-cicd-azure` 

**Description:**
This project demonstrates a fully automated CI/CD pipeline for deploying a Dockerized Python application to Azure App Service using GitHub Actions and Azure CLI.

**Pipeline features:**
1. Integrated code quality checks with Flake8 (linter), Pytest (functional tests), and Trivy (Docker image vulnerability scanning).
2. Automated deployment of code changes to Azure Web App.
3. Immediate visibility of changes via the public Azure Web App URL displayed in the GitHub Actions UI.
4. Includes static code analysis with CodeQL for enhanced security.



# Note

## some useful Git commands

git remote set-url origin `https://liujikuan:<personal access token>@github.com/liujikuan/DevOps.git`

git log --all --decorate --oneline --graph

## Github actions 

**are categorized into two:**
1. use a container action to run containerized code
2. use a JavaScript action to run javascript code such as Node.js code



**The following command triggers a GitHub Actions workflow for the specified branch using the GitHub API**

curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token `<personal access token>`" \
  https://api.github.com/repos/liujikuan/DevOps/actions/workflows/main.yml/dispatches \
  -d '{"ref":"main"}'



## Jenkins pipeline

### Configure Github webhook to trigger the pipeline

1. Use ngrok as a HTTP proxy
2. create a freestyle project, and set the Git repository in the *Source Code Management* section
3. check the *GitHub hook trigger for GITScm polling* option in Jenkins.
4. create or update a file in the repository

