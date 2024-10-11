# GitHub Actions Workflow for Terraform Cloud

This workflow automates Terraform operations using GitHub Actions in conjunction with Terraform Cloud.

## Workflow Overview

The workflow consists of a single job named 'Terraform' that performs the following steps:

1. Checkout the repository
2. Set up Terraform CLI
3. Run Terraform format check
4. Initialize Terraform
5. Validate Terraform configuration
6. Plan Terraform changes
7. Trigger a new run in Terraform Cloud (conditional)

## Key Features

- Runs automatically on pushes to the master branch and when manually triggered.
- Performs Terraform init, format check, validate, and plan on every run.
- Triggers a new run in Terraform Cloud only when manually triggered on the master branch.
- Fully integrates with Terraform Cloud's VCS-driven workflow.

## Using the Workflow

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

   ![VCS](.github/workflows/images/VCS.png)


## Important Notes

- This workflow is designed to work with Terraform Cloud's VCS-driven workflow.
- Actual execution of Terraform commands (including apply) happens on Terraform Cloud, not in the GitHub Actions environment.
- The workflow does not directly apply changes; it triggers a run in Terraform Cloud when manually activated.

## Environment Variables

The workflow uses the following environment variables:

- `TF_CLOUD_ORGANIZATION`: The Terraform Cloud organization
- `TF_API_TOKEN`: The Terraform Cloud API token (stored as a GitHub secret)
- `TF_WORKSPACE`: The Terraform Cloud workspace name