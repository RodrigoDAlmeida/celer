# USER
resource "aws_api_gateway_integration" "api_integration_create_user" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_user.resource_id
  http_method = aws_api_gateway_method.api_method_user.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_create_user.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_get_user" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_user_id.resource_id
  http_method = aws_api_gateway_method.api_method_user_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_get_user.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_list_users" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_user_get.resource_id
  http_method = aws_api_gateway_method.api_method_user_get.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_list_users.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_login" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_user_login.resource_id
  http_method = aws_api_gateway_method.api_method_user_login.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_login.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_delete_user" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_delete_user_id.resource_id
  http_method = aws_api_gateway_method.api_method_delete_user_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_deleteUser.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_update_user" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_put_user.resource_id
  http_method = aws_api_gateway_method.api_method_put_user.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_update_user.invoke_arn
}

# COMPANY

resource "aws_api_gateway_integration" "api_integration_create_company" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_company.resource_id
  http_method = aws_api_gateway_method.api_method_company.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_create_company.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_delete_company" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_delete_company_id.resource_id
  http_method = aws_api_gateway_method.api_method_delete_company_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_delete_company.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_get_company" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_get_company_id.resource_id
  http_method = aws_api_gateway_method.api_method_get_company_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_get_company.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_list_company" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_get_company.resource_id
  http_method = aws_api_gateway_method.api_method_get_company.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_list_company.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_update_company" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_put_company.resource_id
  http_method = aws_api_gateway_method.api_method_put_company.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_update_company.invoke_arn
}

# PRODUCT

resource "aws_api_gateway_integration" "api_integration_create_product" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_product.resource_id
  http_method = aws_api_gateway_method.api_method_product.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_create_product.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_delete_product" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_delete_product_id.resource_id
  http_method = aws_api_gateway_method.api_method_delete_product_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_delete_product.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_get_product" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_get_product_id.resource_id
  http_method = aws_api_gateway_method.api_method_get_product_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_get_product.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_list_product" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_list_products.resource_id
  http_method = aws_api_gateway_method.api_method_list_products.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_list_products.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_update_product" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_update_product.resource_id
  http_method = aws_api_gateway_method.api_method_update_product.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_update_product.invoke_arn
}

# PRODUCT MODEL

resource "aws_api_gateway_integration" "api_integration_create_product_model" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_create_product_model.resource_id
  http_method = aws_api_gateway_method.api_method_create_product_model.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_create_product_model.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_delete_product_model" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_delete_product_model_id.resource_id
  http_method = aws_api_gateway_method.api_method_delete_product_model_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_delete_product_model.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_get_product_model" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_get_product_model_id.resource_id
  http_method = aws_api_gateway_method.api_method_get_product_model_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_get_product_model.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_list_product_model" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_get_product_model_product_id.resource_id
  http_method = aws_api_gateway_method.api_method_get_product_model_product_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_list_product_model.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_update_product_model" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_update_product_model.resource_id
  http_method = aws_api_gateway_method.api_method_update_product_model.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_update_product_model.invoke_arn
}

# ORDER

resource "aws_api_gateway_integration" "api_integration_create_order" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_create_order.resource_id
  http_method = aws_api_gateway_method.api_method_create_order.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_create_order.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_delete_order" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_delete_order.resource_id
  http_method = aws_api_gateway_method.api_method_delete_order.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_delete_order.invoke_arn
}

resource "aws_api_gateway_integration" "api_integration_list_order_by_user_id" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_method.api_method_list_order_by_user_id.resource_id
  http_method = aws_api_gateway_method.api_method_list_order_by_user_id.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_list_order.invoke_arn
}
