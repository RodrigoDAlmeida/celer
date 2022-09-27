
# USER

resource "aws_api_gateway_method" "api_method_user" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_user.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_user_login" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_user_login.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_user_get" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_user.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_user_id" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_user_id.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_delete_user_id" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_user_id.id
  http_method   = "DELETE"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_put_user" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_user.id
  http_method   = "PUT"
  authorization = "NONE"
}

# COMPANY

resource "aws_api_gateway_method" "api_method_company" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_company.id
  http_method   = "POST"
  authorization = "NONE"
}
resource "aws_api_gateway_method" "api_method_delete_company_id" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_company_id.id
  http_method   = "DELETE"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_get_company_id" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_company_id.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_get_company" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_company.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_put_company" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_company.id
  http_method   = "PUT"
  authorization = "NONE"
}

# PRODUCT

resource "aws_api_gateway_method" "api_method_product" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_delete_product_id" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product_id.id
  http_method   = "DELETE"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_get_product_id" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product_id.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_list_products" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_update_product" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product.id
  http_method   = "PUT"
  authorization = "NONE"
}

# PRODUCT MODEL

resource "aws_api_gateway_method" "api_method_create_product_model" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product_model.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_delete_product_model_id" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product_model_id.id
  http_method   = "DELETE"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_get_product_model_id" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product_model_id.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_update_product_model" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product_model.id
  http_method   = "PUT"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_get_product_model_product_id" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_product_model_list_by_product_id.id
  http_method   = "GET"
  authorization = "NONE"
}

#ORDER

resource "aws_api_gateway_method" "api_method_create_order" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_order.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_delete_order" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_order_id.id
  http_method   = "DELETE"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_method_get_order" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.api_proxy_order_id.id
  http_method   = "GET"
  authorization = "NONE"
}