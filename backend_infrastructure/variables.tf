variable "integration_uri" {
  description = "ARN of the Lambda function"
  type        = string
}

# This is so that I am not hardcoding the ARN in the code. Instead its stored as a secret