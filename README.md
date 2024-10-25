# DevOps Cloud Resume Challenge - AWS Implementation

## Visit My Cloud Resume Website
https://princetonabdulsalam.cloud/

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

   ![Flow](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/images/image(1).png)

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


