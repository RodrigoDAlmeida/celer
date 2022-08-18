resource "aws_iam_role" "lambda-role" {
  name               = "lambda-role"
  assume_role_policy = <<EOF
        {
            "Version": "2012-10-17",
            "Statement": [
              {
                "Action": "sts:AssumeRole",
                "Principal": {
                  "Service": "lambda.amazonaws.com"
                },
                "Effect": "Allow",
                "Sid": ""
              }
            ]
        }
        EOF
}

resource "aws_iam_role_policy" "dynamodb_access" {
  name   = "dynamodb_access"
  role   = aws_iam_role.lambda-role.id
  policy = file("policy/dynamodb_policy.json")
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn = "${aws_api_gateway_rest_api.api_gateway.execution_arn}/*/*"
}

