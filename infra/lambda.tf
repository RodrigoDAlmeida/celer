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