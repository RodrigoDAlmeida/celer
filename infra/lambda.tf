resource "aws_lambda_layer_version" "model_lambda_layer" {
  filename   = data.archive_file.file_model_lambda_layer.output_path
  layer_name = "celer-model"
  compatible_runtimes = ["python3.8"]
}

resource "aws_lambda_layer_version" "repository_lambda_layer" {
  filename   = data.archive_file.file_repository_lambda_layer.output_path
  layer_name = "celer-repository"
  compatible_runtimes = ["python3.8"]
}


resource "aws_lambda_function" "lambda" {
  function_name = "celer-create-user"
  filename         = data.archive_file.file_lambda_createUser.output_path
  role    = aws_iam_role.lambda-role.arn
  handler = "CreateUser.lambda_handler"
  runtime = "python3.8"
  layers = [aws_lambda_layer_version.model_lambda_layer.arn, aws_lambda_layer_version.repository_lambda_layer.arn]
  
}