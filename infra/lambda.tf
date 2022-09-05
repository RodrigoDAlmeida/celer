#Layers
resource "aws_lambda_layer_version" "jsonpickle_lambda_layer" {
  filename   = "../dep-layers/jsonpickle.zip"
  layer_name = "jsonpickle"
  compatible_runtimes = [var.python_version]
  tags = {"App":"celer"}
}

resource "aws_lambda_layer_version" "repository_lambda_layer" {
  filename         = data.archive_file.file_repository_lambda_layer.output_path
  source_code_hash = data.archive_file.file_repository_lambda_layer.output_base64sha256
  layer_name = "celer-repository"
  compatible_runtimes = [var.python_version]
  tags = {"App":"celer"}
}

#Functions
resource "aws_lambda_function" "lambda_create_user" {
  function_name = "celer-create-user"
  filename         = data.archive_file.file_lambda_createUser.output_path
  source_code_hash = data.archive_file.file_lambda_createUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "createUser.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.repository_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_get_user" {
  function_name = "celer-get-user"
  filename         = data.archive_file.file_lambda_getUser.output_path
  source_code_hash = data.archive_file.file_lambda_getUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "getUser.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.repository_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_list_users" {
  function_name = "celer-list-users"
  filename         = data.archive_file.file_lambda_listUsers.output_path
  source_code_hash = data.archive_file.file_lambda_listUsers.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "listUsers.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.repository_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_login" {
  function_name = "celer-login"
  filename         = data.archive_file.file_lambda_login.output_path
  source_code_hash = data.archive_file.file_lambda_login.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "login.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.repository_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_deleteUser" {
  function_name = "celer-delete-user"
  filename         = data.archive_file.file_lambda_deleteUser.output_path
  source_code_hash = data.archive_file.file_lambda_deleteUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "deleteUser.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.repository_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}

resource "aws_lambda_function" "lambda_update_user" {
  function_name = "celer-update-user"
  filename         = data.archive_file.file_lambda_updateUser.output_path
  source_code_hash = data.archive_file.file_lambda_updateUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "updateUser.lambda_handler"
  runtime = var.python_version
  layers = [aws_lambda_layer_version.repository_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  tags = {"App":"celer"}
}


