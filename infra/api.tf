resource "aws_api_gateway_rest_api" "api_gateway" {
  name        = "celer-api"
  description = "API from Celer application"
  tags = {"App":"celer"}
}

resource "aws_api_gateway_resource" "api_proxy_user" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_rest_api.api_gateway.root_resource_id
  path_part   = "user"
}
resource "aws_api_gateway_resource" "api_proxy_user_id" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_resource.api_proxy_user.id
  path_part   = "{id}"
}

resource "aws_api_gateway_resource" "api_proxy_company" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_rest_api.api_gateway.root_resource_id
  path_part   = "company"
}
resource "aws_api_gateway_resource" "api_proxy_company_id" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_resource.api_proxy_company.id
  path_part   = "{id}"
}

resource "aws_api_gateway_resource" "api_proxy_user_login" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_resource.api_proxy_user.id
  path_part   = "login"
}

resource "aws_api_gateway_resource" "api_proxy_product" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_rest_api.api_gateway.root_resource_id
  path_part   = "product"
}

resource "aws_api_gateway_resource" "api_proxy_product_id" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_resource.api_proxy_product.id
  path_part   = "{id}"
}

resource "aws_api_gateway_resource" "api_proxy_product_model" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_rest_api.api_gateway.root_resource_id
  path_part   = "product-model"
}

resource "aws_api_gateway_resource" "api_proxy_product_model_id" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_resource.api_proxy_product_model.id
  path_part   = "{id}"
}



