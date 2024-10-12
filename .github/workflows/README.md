# Explaining the 3 CI/CD Pipeline Workflows

## 1. GitHub Actions Workflow for Terraform Cloud

This workflow automates Terraform operations using GitHub Actions in conjunction with Terraform Cloud.

### Workflow Overview

The workflow consists of a single job named 'Terraform' that performs the following steps:

1. Checkout the repository
2. Set up Terraform CLI
3. Run Terraform format check
4. Initialize Terraform
5. Validate Terraform configuration
6. Plan Terraform changes
7. Trigger a new run in Terraform Cloud (conditional)

### Key Features

- Runs automatically on pushes to the master branch and when manually triggered.
- Performs Terraform init, format check, validate, and plan on every run.
- Triggers a new run in Terraform Cloud only when manually triggered on the master branch.
- Fully integrates with Terraform Cloud's VCS-driven workflow.

### Using the Workflow

1. **Automatic Checks**: 
   Every push to the `master` branch automatically triggers the workflow, running Terraform init, validate, and plan.

2. **Reviewing Plans**:
   You can review the output of the plan in the GitHub Actions logs and the Terraform Cloud console.

3. **Triggering Terraform Cloud Run**:
   To trigger a new run in Terraform Cloud:
   - Go to the Actions tab in the GitHub repository
   - Select the "Terraform CI/CD" workflow
   - Click "Run workflow"
   - Select the master branch
   - Click "Run workflow"

   This will create a new run in Terraform Cloud. What the workflow does when manually triggered on the master branch is:

   - It sends a request to Terraform Cloud to create a new run.
   - This run in Terraform Cloud will include both a plan and an apply phase.

   The actual apply in Terraform Cloud depends on your workspace settings:

   - If the  workspace is set to "Auto apply", then the run will automatically apply the changes after the plan phase.

   - If the workspace is not set to "Auto apply", then the run will stop after the plan phase, waiting for manual approval in the Terraform Cloud console before applying.

   ![VCS](https://github.com/Princeton45/DevOps-Cloud-Resume-Challenge/blob/master/.github/workflows/images/VCS.PNG)

### Important Notes

- This workflow is designed to work with Terraform Cloud's VCS-driven workflow.
- Actual execution of Terraform commands (including apply) happens on Terraform Cloud, not in the GitHub Actions environment.
- The workflow does not directly apply changes; it triggers a run in Terraform Cloud when manually activated.

### Environment Variables

The workflow uses the following environment variables:

- `TF_CLOUD_ORGANIZATION`: The Terraform Cloud organization
- `TF_API_TOKEN`: The Terraform Cloud API token (stored as a GitHub secret)
- `TF_WORKSPACE`: The Terraform Cloud workspace name

## 2. S3 Workflow

This workflow handles continuous deployment to AWS S3 and CloudFront.

### Workflow Overview

- **Trigger**: Pushes to the `master` branch that affect files in the `frontend_infrastructure/website_homepage/` directory.
- **Environment**: Runs on Ubuntu latest.
- When the local website file code is edited and pushed to the repository, it will trigger this workflow and automatically upload the changed code to S3 and invalidate the cache.

### Steps:

1. **Checkout**: Fetches the repository code.
2. **AWS Credentials**: Configures AWS credentials for deployment.
3. **S3 Deployment**: Syncs the website files to an S3 bucket.
4. **CloudFront Invalidation**: Invalidates the CloudFront cache to ensure updates are immediately visible.

## 3. Lambda CI/CD Workflow

This workflow automates testing and deployment of the AWS Lambda function.

### Trigger
- Activates on pushes that modify `backend_infrastructure/Lambda Folder/lambda_function.py`

### Jobs

#### 1. Test
- Runs on Ubuntu
- Sets up Python 3.9
- Installs dependencies
- Executes pytest

#### 2. Deploy
- Configures AWS credentials
- Zips and updates Lambda function code

**Note:** The deploy job has a `needs: test` line. This means that the deploy job will only run if the test job completes successfully. If any step in the test job fails (including the pytest step), the deploy job won't run at all.

## Using Git to push to GitHub:
1. `git add .` <-- stages the files
2. `git commit -m "<commit_message>"`
3. `git push` (make sure to set the origin for the repo and set-upstream)