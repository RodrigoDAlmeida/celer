#Lambda Layers
data "archive_file" "file_model_lambda_layer" {
  type             = "zip"
  source_dir     = "../src/lambda/model/"
  output_path      = "../build/model_lambda_layer.zip"
}

data "archive_file" "file_repository_lambda_layer" {
  type             = "zip"
  source_dir     = "../src/lambda/repository/"
  output_path      = "../build/repository_lambda_layer.zip"
}

#Lambdas
data "archive_file" "file_lambda_createUser" {
  type             = "zip"
  source_file     = "../src/lambda/createUser.py"
  output_path      = "../build/lambdas/createUser.zip"
}

data "archive_file" "file_lambda_getUser" {
  type             = "zip"
  source_file     = "../src/lambda/getUser.py"
  output_path      = "../build/lambdas/getUser.zip"
}