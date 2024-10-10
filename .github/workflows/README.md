#===================================================================#
#The workflow is split into two jobs: plan and apply.
#The plan job runs automatically on pushes to the master branch and when the workflow is manually triggered.
#The plan job generates a Terraform plan and saves it as an artifact.
#The apply job is set to run only when the workflow is manually triggered (workflow_dispatch).
#The apply job has an environment: production setting, which allows you to set up required approvals in GitHub.
#The apply job downloads the plan artifact created by the plan job and uses it for the apply step.

To use this workflow:

When you push to the master branch, it will automatically run the plan job, creating a plan and saving it as an artifact.
You can then review the plan by checking the workflow run in GitHub Actions and downloading the tfplan-text artifact.
If you're satisfied with the plan, you can manually trigger the workflow again (using the "Run workflow" button in the Actions tab of your GitHub repository).
This manual trigger will run both the plan and apply jobs, but the apply job will only proceed if you've set up and approved the production environment in your GitHub repository settings.