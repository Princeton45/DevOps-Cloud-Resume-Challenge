# Defines the HTTP API resource:
resource "aws_apigatewayv2_api" "visitor_counter_api" {
  name          = "VisitorCounterAPI"
  protocol_type = "HTTP"

# Defines the CORS configuration
  cors_configuration {
    allow_credentials = false
    allow_headers     = ["content-type"]
    allow_methods     = ["GET", "OPTIONS", "POST"]
    allow_origins     = ["*"]
    max_age           = 0
  }
}

# Defines the routes for the API

resource "aws_apigatewayv2_route" "visitor_counter_function_any" {
  api_id    = aws_apigatewayv2_api.visitor_counter_api.id
  route_key = "ANY /VisitorCounterFunction"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"

  depends_on = [
    aws_apigatewayv2_api.visitor_counter_api,
    aws_apigatewayv2_integration.lambda_integration
  ]
}

resource "aws_apigatewayv2_route" "count_post" {
  api_id    = aws_apigatewayv2_api.visitor_counter_api.id
  route_key = "POST /count"
  target    = "integrations/esiviqm"

  depends_on = [
    aws_apigatewayv2_api.visitor_counter_api,
    aws_apigatewayv2_integration.lambda_integration
  ]
}

# Defines the Lambda integration

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id                 = aws_apigatewayv2_api.visitor_counter_api.id
  integration_type       = "AWS_PROXY"
  integration_uri        = var.integration_uri
  integration_method     = "POST"
  payload_format_version = "2.0"

  depends_on = [aws_apigatewayv2_api.visitor_counter_api]
}

# In the Terraform configuration, the variable declaration clearly defines "$default" as a string value.
# When referencing the variable in the resource, Terraform knows to treat its value as a literal string.
# During the import process, Terraform uses the variable's value without any special interpretation of the "$" character
# This approach essentially tells Terraform, "This is just a string, don't try to interpret it in any special way," which allows it to correctly match and import the existing AWS resource.

variable "default_stage_name" {
  default = "$default"
  type    = string
}

# Defines the default stage.
resource "aws_apigatewayv2_stage" "default" {
  api_id      = aws_apigatewayv2_api.visitor_counter_api.id
  name        = var.default_stage_name
  auto_deploy = true

  depends_on = [
    aws_apigatewayv2_api.visitor_counter_api,
    aws_apigatewayv2_route.visitor_counter_function_any,
    aws_apigatewayv2_route.count_post,
    aws_apigatewayv2_integration.lambda_integration
  ]
}
