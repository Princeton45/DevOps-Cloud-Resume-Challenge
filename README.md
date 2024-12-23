# DevOps Cloud Resume Challenge - AWS Implementation

## Visit My Cloud Resume Website
https://princetonabdulsalam.cloud/resume-home/

## Project Overview
This project is my implementation of the Cloud Resume Challenge using AWS services. It demonstrates a full-stack cloud application, showcasing skills in front-end development, back-end serverless architecture, infrastructure as code, and CI/CD practices.

For more information on the original challenge see:
https://cloudresumechallenge.dev/docs/the-challenge/aws/

For more information on the Terraform extension to the original challenge see: https://cloudresumechallenge.dev/docs/extensions/terraform-getting-started/

## How It Works
The project combines various AWS services to create a serverless, highly available web application. Here's how the components work together:

1. **Front-end**:
   - HTML/CSS: The resume content is written in HTML and styled with CSS.
   - JavaScript: Handles the visitor counter functionality on the client side.
   - S3: Hosts the static website files (HTML, CSS, JS).
   - CloudFront: Provides content delivery and HTTPS security for the S3-hosted website.
   - Custom Domain: Purchased from Porkbun, with DNS records configured to point to the CloudFront distribution.


2. **Back-end**:
   - API Gateway: Exposes a HTTP API endpoint that the front-end can call.
   - Lambda (Python): Contains the logic to update and retrieve the visitor count.
   - DynamoDB: Stores the visitor count data.

3. **Interaction Flow**:
   - When a user visits the website, the HTML/CSS/JS files are served from S3 through CloudFront.
   - The JavaScript on the page makes an API call to the API Gateway endpoint.
   - API Gateway triggers the Lambda function.
   - The Lambda function interacts with DynamoDB to update and retrieve the visitor count.
   - The count is returned through API Gateway to the client-side JavaScript.
   - JavaScript updates the visitor count displayed on the webpage.

   ![Flow](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/image%20(1).png)

4. **Infrastructure as Code**:
   - Terraform is used to define and manage all AWS resources, ensuring reproducibility and version control of the infrastructure.

5. **CI/CD Pipeline**:
   - GitHub Actions workflows automate the testing and deployment process for both front-end and back-end changes.

## Key Components and Services Used
- Amazon S3 for static website hosting
- Amazon CloudFront for content delivery and HTTPS
- Amazon DynamoDB for the visitor counter database
- AWS Lambda for serverless backend logic
- Amazon API Gateway for HTTP API
- Terraform for Infrastructure as Code
- GitHub Actions for CI/CD pipelines

## CI/CD Workflows
1. **Terraform Cloud Workflow**: Automates Terraform operations
   - Runs on pushes to the master github branch and manual triggers
   - Performs Terraform init, validate, and plan
   - Integrates with Terraform Cloud for apply operations

2. **S3 Deployment Workflow**: Handles front-end deployment
   - Triggers on changes to website files
   - Syncs updated files to S3
   - Invalidates CloudFront cache

3. **Lambda CI/CD Workflow**: Manages backend deployment
   - Activates on changes to Lambda function code
   - Runs Python tests
   - Deploys updated Lambda function if tests pass

   Please visit [Github Workflows README](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/tree/master/.github/workflows) for a more in depth overview of the workflows and their code.

## Skills Demonstrated
- Cloud Architecture with AWS
- Infrastructure as Code with Terraform
- CI/CD implementation with GitHub Actions
- Front-end development (HTML, CSS, JavaScript)
- Back-end development with Python
- Serverless architecture
- API development and integration
- Version control with Git
- HTTPS and DNS management




## Infrastructure Provisioning with Terraform

- The main.tf terraform file is calling the backend_infrastructure and frontend_infrastructure sub-modules that contain the actual terraform infrastructure code.
![terraform](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/terraform_image.png)

## Lambda Function.

![lambda_function](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/lambda_function.png)

- Increments visitor count in DynamoDB
- Handles new counter initialization
- CORS-enabled for web browser access
- Includes error handling
- Properly handles DynamoDB Decimal type conversion

[FULL CODE W/ COMMENTS](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/backend_infrastructure/Lambda%20Folder/lambda_function.py)

## Lambda Function Tests.

![lambda_function_tests2](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/lambda_function_tests2.png)

- Test suite for AWS Lambda visitor counter using moto library to mock DynamoDB services
- Contains three main test cases: first visit (counter starts at 1), subsequent visits (counter increments), and error handling
- Tests can be run locally using pytest without requiring actual AWS resources
![lambda_function_tests](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/lambda_function_tests.png)

[FULL CODE W/ COMMENTS](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/backend_infrastructure/Lambda%20Folder/test_lambda_function.py)


## AWS S3 Bucket configuration hosting my website files

![s3_bucket](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/s3bucket1.png)

## AWS CloudFront Distribution

![cloudfront](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/cloudfront.png)

## AWS API Gateway

![api_gateway](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/api_gateway1.png)

## AWS Lambda Function

![lambda](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/lambda.png)

## AWS DynamoDB Database

![dynamodb](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/dynamodb.png)

## Lambda CI/CD Pipeline
- This workflow automates testing and deployment of the AWS Lambda Function.
- Activates on pushes that modify `backend_infrastructure/Lambda Folder/lambda_function.py`

[READ MORE HERE](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/tree/master/.github/workflows)
![lambda_cicd](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/lambda_cicd.png)

## S3 CI/CD Pipeline
- This workflow handles continuous deployment to AWS S3 and CloudFront.
   - When the local website file code is edited and pushed to the repository, it will trigger this workflow and automatically upload the changed code to S3 and invalidate the cache.

[READ MORE HERE](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/tree/master/.github/workflows)
![s3_cicd](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/s3_cicd.png)

## Terraform CI/CD Pipeline
- This workflow is triggered when a push is made to the master branch from a local development environment, where Terraform configuration files (.tf) are written and committed, initiating the GitHub Actions workflow that validates these configurations by performing format checks, initialization, validation, and planning steps along the way.  A Terraform Apply is only ran when manually triggering the workflow through the GitHub Actions tab.
   
   - Best practice is to review your terraform plan first before applying it to ensure the proposed changes align with your intended infrastructure modifications and to prevent any unintended changes or deletions.

   
[READ MORE HERE](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/tree/master/.github/workflows)
![terraform_cicd](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/terraform_cicd.png)



## Troubleshooting along the way

### 403 Error
![Error](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/403_error.png)

I could go to the cloudfront distribution domain name for my setup fine but when I tried going through my princetonabdulsalam.cloud domain name I got the error above.

To fix it, I had to add my princetonabdulsalam.cloud as an alternate domain alias in the cloud front distribution.

![alt_domain](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/alt_domain.png)

### API Gateway Error

![api_gateway_error](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/api_gateway_error.png)

The API Gateway started throwing a timeout log error ( enabled logging for the API then created a log group in cloudwatch using the APIs ARN to then log all the API logs to the log group) in cloudwatch. Basically, the default timeout for the lambda function was 3 seconds so if a response was not heard from the lambda function back to the API within 3 seconds, it would throw an error and not load the visitor counter on my website.

I changed the max timeout on the function to 15 minutes and now the issue doesn’t happen.