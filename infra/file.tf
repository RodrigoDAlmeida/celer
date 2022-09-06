#Lambda Layers

data "archive_file" "file_repository_lambda_layer" {
  type             = "zip"
  source_dir     = "../src/layer/repository/"
  output_path      = "../build/repository_lambda_layer.zip"
}

#Lambdas
data "archive_file" "file_lambda_createUser" {
  type             = "zip"
  source_file     = "../src/lambda/user/createUser.py"
  output_path      = "../build/lambdas/createUser.zip"
}

data "archive_file" "file_lambda_getUser" {
  type             = "zip"
  source_file     = "../src/lambda/user/getUser.py"
  output_path      = "../build/lambdas/getUser.zip"
}

data "archive_file" "file_lambda_listUsers" {
  type             = "zip"
  source_file     = "../src/lambda/user/listUsers.py"
  output_path      = "../build/lambdas/listUsers.zip"
}

data "archive_file" "file_lambda_login" {
  type             = "zip"
  source_file     = "../src/lambda/user/login.py"
  output_path      = "../build/lambdas/login.zip"
}

data "archive_file" "file_lambda_deleteUser" {
  type             = "zip"
  source_file     = "../src/lambda/user/deleteUser.py"
  output_path      = "../build/lambdas/deleteUser.zip"
}

data "archive_file" "file_lambda_updateUser" {
  type             = "zip"
  source_file     = "../src/lambda/user/updateUser.py"
  output_path      = "../build/lambdas/updateUser.zip"
}