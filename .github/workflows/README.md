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
7. Apply Terraform changes (conditional)

## Key Features

- Runs automatically on pushes to the master branch and when manually triggered.
- Performs Terraform init, format check, validate, and plan on every run.
- The apply step only runs when manually triggered on the master branch.
- Integrates with Terraform Cloud for state management and execution.

## Using the Workflow

1. **Automatic Plan Generation**: 
   Every push to the `master` branch automatically triggers the workflow, running Terraform init, validate, and plan.

2. **Reviewing Plans**:
   You can review the output of the plan in the Terraform Cloud console.

3. **Applying Changes**:
   To apply changes:
   - Go to the Actions tab in the GitHub repository
   - Select the "Terraform CI/CD" workflow
   - Click "Run workflow"
   - Select the master branch
   - Click "Run workflow"

   The apply step will only run when manually triggered on the master branch.

## Important Notes

- This workflow is designed to work with Terraform Cloud's VCS-driven workflow.
- Actual execution of Terraform commands happens on Terraform Cloud, not in the GitHub Actions environment.