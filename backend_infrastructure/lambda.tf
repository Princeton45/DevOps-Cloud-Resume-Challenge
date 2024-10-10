# IAM Policy for Lambda Function to access DynamoDB (policy is defined within the role)
resource "aws_iam_role" "visitor_counter_role" {
  name = "VisitorCounterFunction-role-5m87n4nl"
  path = "/service-role/"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# Define the Lambda function resource
resource "aws_lambda_function" "visitor_counter_function" {
  filename         = "${path.module}/lambda_function.zip"
  function_name    = "VisitorCounterFunction"
  role             = aws_iam_role.visitor_counter_role.arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.12"
  source_code_hash = filebase64sha256("${path.module}/lambda_function.zip")

  depends_on = [
    aws_iam_role.visitor_counter_role,
    aws_dynamodb_table.visitor_counter
  ]
}
# Lambda contains the logic to interact with DynamoDB via the lambda_function.zip (python) file