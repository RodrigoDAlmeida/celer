#Layers
resource "aws_lambda_layer_version" "jsonpickle_lambda_layer" {
  filename   = "../dep-layers/jsonpickle.zip"
  layer_name = "jsonpickle"
  compatible_runtimes = [var.python_version]
}

resource "aws_lambda_layer_version" "service_lambda_layer" {
  filename         = data.archive_file.file_service_lambda_layer.output_path
  source_code_hash = data.archive_file.file_service_lambda_layer.output_base64sha256
  layer_name = "celer-service"
  compatible_runtimes = [var.python_version]
}

resource "aws_lambda_layer_version" "util_lambda_layer" {
  filename         = data.archive_file.file_util_lambda_layer.output_path
  source_code_hash = data.archive_file.file_util_lambda_layer.output_base64sha256
  layer_name = "celer-util"
  compatible_runtimes = [var.python_version]
}

#Functions
#User
resource "aws_lambda_function" "lambda_create_user" {
  function_name = "celer-user-create"
  filename         = data.archive_file.file_lambda_createUser.output_path
  source_code_hash = data.archive_file.file_lambda_createUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "create_user.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_get_user" {
  function_name = "celer-user-get"
  filename         = data.archive_file.file_lambda_getUser.output_path
  source_code_hash = data.archive_file.file_lambda_getUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "get_user.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_list_users" {
  function_name = "celer-user-list"
  filename         = data.archive_file.file_lambda_listUsers.output_path
  source_code_hash = data.archive_file.file_lambda_listUsers.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "list_users.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_login" {
  function_name = "celer-login"
  filename         = data.archive_file.file_lambda_login.output_path
  source_code_hash = data.archive_file.file_lambda_login.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "login.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_deleteUser" {
  function_name = "celer-user-delete"
  filename         = data.archive_file.file_lambda_deleteUser.output_path
  source_code_hash = data.archive_file.file_lambda_deleteUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "delete_user.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_update_user" {
  function_name = "celer-user-update"
  filename         = data.archive_file.file_lambda_updateUser.output_path
  source_code_hash = data.archive_file.file_lambda_updateUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "update_user.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}
#Company

resource "aws_lambda_function" "lambda_create_company" {
  function_name = "celer-company-create"
  filename         = data.archive_file.file_lambda_createCompany.output_path
  source_code_hash = data.archive_file.file_lambda_createCompany.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "create_company.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_delete_company" {
  function_name = "celer-company-delete"
  filename         = data.archive_file.file_lambda_deleteCompany.output_path
  source_code_hash = data.archive_file.file_lambda_deleteCompany.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "delete_company.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_get_company" {
  function_name = "celer-company-get"
  filename         = data.archive_file.file_lambda_getCompany.output_path
  source_code_hash = data.archive_file.file_lambda_getCompany.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "get_company.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_list_company" {
  function_name = "celer-company-list"
  filename         = data.archive_file.file_lambda_listCompany.output_path
  source_code_hash = data.archive_file.file_lambda_listCompany.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "list_company.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_update_company" {
  function_name = "celer-company-update"
  filename         = data.archive_file.file_lambda_updateCompany.output_path
  source_code_hash = data.archive_file.file_lambda_updateCompany.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "update_company.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

#Product
resource "aws_lambda_function" "lambda_create_product" {
  function_name = "celer-product-create"
  filename         = data.archive_file.file_lambda_createProduct.output_path
  source_code_hash = data.archive_file.file_lambda_createProduct.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "create_product.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_delete_product" {
  function_name = "celer-product-delete"
  filename         = data.archive_file.file_lambda_deleteProduct.output_path
  source_code_hash = data.archive_file.file_lambda_deleteProduct.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "delete_product.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_get_product" {
  function_name = "celer-product-get"
  filename         = data.archive_file.file_lambda_getProduct.output_path
  source_code_hash = data.archive_file.file_lambda_getProduct.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "get_product.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_list_products" {
  function_name = "celer-product-list"
  filename         = data.archive_file.file_lambda_listProducts.output_path
  source_code_hash = data.archive_file.file_lambda_listProducts.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "list_products.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_update_product" {
  function_name = "celer-product-update"
  filename         = data.archive_file.file_lambda_updateProduct.output_path
  source_code_hash = data.archive_file.file_lambda_updateProduct.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "update_product.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

#Product Model
resource "aws_lambda_function" "lambda_create_product_model" {
  function_name = "celer-productmodel-create"
  filename         = data.archive_file.file_lambda_createProductModel.output_path
  source_code_hash = data.archive_file.file_lambda_createProductModel.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "create_product_model.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_delete_product_model" {
  function_name = "celer-productmodel-delete"
  filename         = data.archive_file.file_lambda_deleteProductModel.output_path
  source_code_hash = data.archive_file.file_lambda_deleteProductModel.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "delete_product_model.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_get_product_model" {
  function_name = "celer-productmodel-get"
  filename         = data.archive_file.file_lambda_getProductModel.output_path
  source_code_hash = data.archive_file.file_lambda_getProductModel.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "get_product_model.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.util_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_list_product_model" {
  function_name = "celer-productmodel-list"
  filename         = data.archive_file.file_lambda_listProductModel.output_path
  source_code_hash = data.archive_file.file_lambda_listProductModel.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "list_product_model.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.util_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_update_product_model" {
  function_name = "celer-productmodel-update"
  filename         = data.archive_file.file_lambda_updateProductModel.output_path
  source_code_hash = data.archive_file.file_lambda_updateProductModel.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "update_product_model.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.util_lambda_layer.arn]
  tags = {"App":"celer"}
}

#Order
resource "aws_lambda_function" "lambda_create_order" {
  function_name = "celer-order-create"
  filename         = data.archive_file.file_lambda_createOrder.output_path
  source_code_hash = data.archive_file.file_lambda_createOrder.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "create_order.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_delete_order" {
  function_name = "celer-order-delete"
  filename         = data.archive_file.file_lambda_deleteOrder.output_path
  source_code_hash = data.archive_file.file_lambda_deleteOrder.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "delete_order.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_get_order" {
  function_name = "celer-order-get"
  filename         = data.archive_file.file_lambda_getOrder.output_path
  source_code_hash = data.archive_file.file_lambda_getOrder.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "get_order.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.util_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_list_order" {
  function_name = "celer-order-list"
  filename         = data.archive_file.file_lambda_listOrder.output_path
  source_code_hash = data.archive_file.file_lambda_listOrder.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "list_order.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn, aws_lambda_layer_version.util_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_update_order" {
  function_name = "celer-order-update"
  filename         = data.archive_file.file_lambda_updateOrder.output_path
  source_code_hash = data.archive_file.file_lambda_updateOrder.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "update_order.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.service_lambda_layer.arn]
  tags = {"App":"celer"}
}