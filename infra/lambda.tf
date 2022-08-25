#Layers
resource "aws_lambda_layer_version" "jsonpickle_lambda_layer" {
  filename   = "../dep-layers/jsonpickle.zip"
  layer_name = "jsonpickle"
  compatible_runtimes = ["python3.8"]
}

resource "aws_lambda_layer_version" "model_lambda_layer" {
  filename         = data.archive_file.file_model_lambda_layer.output_path
  source_code_hash = data.archive_file.file_model_lambda_layer.output_base64sha256
  layer_name = "celer-model"
  compatible_runtimes = ["python3.8"]
}

resource "aws_lambda_layer_version" "repository_lambda_layer" {
  filename         = data.archive_file.file_repository_lambda_layer.output_path
  source_code_hash = data.archive_file.file_repository_lambda_layer.output_base64sha256
  layer_name = "celer-repository"
  compatible_runtimes = ["python3.8"]
}

#Functions
resource "aws_lambda_function" "lambda_create_user" {
  function_name = "celer-create-user"
  filename         = data.archive_file.file_lambda_createUser.output_path
  source_code_hash = data.archive_file.file_lambda_createUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "createUser.lambda_handler"
  runtime = "python3.8"
  layers = [aws_lambda_layer_version.model_lambda_layer.arn, aws_lambda_layer_version.repository_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  
}

resource "aws_lambda_function" "lambda_get_user" {
  function_name = "celer-get-user"
  filename         = data.archive_file.file_lambda_getUser.output_path
  source_code_hash = data.archive_file.file_lambda_getUser.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "getUser.lambda_handler"
  runtime = "python3.8"
  layers = [aws_lambda_layer_version.model_lambda_layer.arn, aws_lambda_layer_version.repository_lambda_layer.arn, aws_lambda_layer_version.jsonpickle_lambda_layer.arn]
  
}