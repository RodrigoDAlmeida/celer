data "archive_file" "file_model_lambda_layer" {
  type             = "zip"
  source_dir     = "../src/model/"
  output_path      = "../build/model_lambda_layer.zip"
}

data "archive_file" "file_repository_lambda_layer" {
  type             = "zip"
  source_dir     = "../src/repository/"
  output_path      = "../build/repository_lambda_layer.zip"
}


data "archive_file" "file_lambda_createUser" {
  type             = "zip"
  source_file     = "../src/lambda/CreateUser.py"
  output_path      = "../build/lambdas/createUser.zip"
}