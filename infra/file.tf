#Lambda Layers

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

data "archive_file" "file_lambda_listUsers" {
  type             = "zip"
  source_file     = "../src/lambda/listUsers.py"
  output_path      = "../build/lambdas/listUsers.zip"
}

data "archive_file" "file_lambda_login" {
  type             = "zip"
  source_file     = "../src/lambda/login.py"
  output_path      = "../build/lambdas/login.zip"
}

data "archive_file" "file_lambda_deleteUser" {
  type             = "zip"
  source_file     = "../src/lambda/deleteUser.py"
  output_path      = "../build/lambdas/deleteUser.zip"
}

data "archive_file" "file_lambda_updateUser" {
  type             = "zip"
  source_file     = "../src/lambda/updateUser.py"
  output_path      = "../build/lambdas/updateUser.zip"
}