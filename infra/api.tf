resource "aws_api_gateway_rest_api" "api_gateway" {
  name        = "celer-api"
  description = "API from Celer application"
}

##PROXYS
resource "aws_api_gateway_resource" "api_proxy_user" {
  rest_api_id = "${aws_api_gateway_rest_api.api_gateway.id}"
  parent_id   = "${aws_api_gateway_rest_api.api_gateway.root_resource_id}"
  path_part   = "user"
}

resource "aws_api_gateway_resource" "api_proxy_user_id" {
  rest_api_id = "${aws_api_gateway_rest_api.api_gateway.id}"
  parent_id   = "${aws_api_gateway_resource.api_proxy_user.id}"
  path_part   = "{id}"
}

resource "aws_api_gateway_resource" "api_proxy_user_login" {
  rest_api_id = "${aws_api_gateway_rest_api.api_gateway.id}"
  parent_id   = "${aws_api_gateway_resource.api_proxy_user.id}"
  path_part   = "login"
}

#METHODS

resource "aws_api_gateway_method" "api_method_user" {
  rest_api_id   = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id   = "${aws_api_gateway_resource.api_proxy_user.id}"
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_user_login" {
  rest_api_id   = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id   = "${aws_api_gateway_resource.api_proxy_user_login.id}"
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_user_get" {
  rest_api_id   = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id   = "${aws_api_gateway_resource.api_proxy_user.id}"
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_user_id" {
  rest_api_id   = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id   = "${aws_api_gateway_resource.api_proxy_user_id.id}"
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_delete_user_id" {
  rest_api_id   = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id   = "${aws_api_gateway_resource.api_proxy_user_id.id}"
  http_method   = "DELETE"
  authorization = "NONE"
}



#INTEGRATIONS

resource "aws_api_gateway_integration" "api_integration_create_user" {
  rest_api_id = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id = "${aws_api_gateway_method.api_method_user.resource_id}"
  http_method = "${aws_api_gateway_method.api_method_user.http_method}"
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = "${aws_lambda_function.lambda_create_user.invoke_arn}"
}

resource "aws_api_gateway_integration" "api_integration_get_user" {
  rest_api_id = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id = "${aws_api_gateway_method.api_method_user_id.resource_id}"
  http_method = "${aws_api_gateway_method.api_method_user_id.http_method}"
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = "${aws_lambda_function.lambda_get_user.invoke_arn}"
}

resource "aws_api_gateway_integration" "api_integration_list_users" {
  rest_api_id = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id = "${aws_api_gateway_method.api_method_user_get.resource_id}"
  http_method = "${aws_api_gateway_method.api_method_user_get.http_method}"
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = "${aws_lambda_function.lambda_list_users.invoke_arn}"
}

resource "aws_api_gateway_integration" "api_integration_login" {
  rest_api_id = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id = "${aws_api_gateway_method.api_method_user_login.resource_id}"
  http_method = "${aws_api_gateway_method.api_method_user_login.http_method}"
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = "${aws_lambda_function.lambda_login.invoke_arn}"
}

resource "aws_api_gateway_integration" "api_integration_delete_user" {
  rest_api_id = "${aws_api_gateway_rest_api.api_gateway.id}"
  resource_id = "${aws_api_gateway_method.api_method_delete_user_id.resource_id}"
  http_method = "${aws_api_gateway_method.api_method_delete_user_id.http_method}"
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = "${aws_lambda_function.lambda_deleteUser.invoke_arn}"
}





