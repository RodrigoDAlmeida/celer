#Lambda Layers

data "archive_file" "file_service_lambda_layer" {
  type             = "zip"
  source_dir     = "../src/layer/service/"
  output_path      = "../build/service_lambda_layer.zip"
}

#Lambdas
#USER
data "archive_file" "file_lambda_createUser" {
  type             = "zip"
  source_file     = "../src/lambda/user/create_user.py"
  output_path      = "../build/lambdas/create_user.zip"
}

data "archive_file" "file_lambda_getUser" {
  type             = "zip"
  source_file     = "../src/lambda/user/get_user.py"
  output_path      = "../build/lambdas/get_user.zip"
}

data "archive_file" "file_lambda_listUsers" {
  type             = "zip"
  source_file     = "../src/lambda/user/list_users.py"
  output_path      = "../build/lambdas/list_users.zip"
}

data "archive_file" "file_lambda_login" {
  type             = "zip"
  source_file     = "../src/lambda/user/login.py"
  output_path      = "../build/lambdas/login.zip"
}

data "archive_file" "file_lambda_deleteUser" {
  type             = "zip"
  source_file     = "../src/lambda/user/delete_user.py"
  output_path      = "../build/lambdas/delete_user.zip"
}

data "archive_file" "file_lambda_updateUser" {
  type             = "zip"
  source_file     = "../src/lambda/user/update_user.py"
  output_path      = "../build/lambdas/update_user.zip"
}

#COMPANY

data "archive_file" "file_lambda_createCompany" {
  type             = "zip"
  source_file     = "../src/lambda/company/create_company.py"
  output_path      = "../build/lambdas/create_company.zip"
}

data "archive_file" "file_lambda_deleteCompany" {
  type             = "zip"
  source_file     = "../src/lambda/company/delete_company.py"
  output_path      = "../build/lambdas/delete_company.zip"
}

data "archive_file" "file_lambda_getCompany" {
  type             = "zip"
  source_file     = "../src/lambda/company/get_company.py"
  output_path      = "../build/lambdas/get_company.zip"
}

data "archive_file" "file_lambda_listCompany" {
  type             = "zip"
  source_file     = "../src/lambda/company/list_company.py"
  output_path      = "../build/lambdas/list_company.zip"
}

data "archive_file" "file_lambda_updateCompany" {
  type             = "zip"
  source_file     = "../src/lambda/company/update_company.py"
  output_path      = "../build/lambdas/update_company.zip"
}

#PRODUCT

data "archive_file" "file_lambda_createProduct" {
  type             = "zip"
  source_file     = "../src/lambda/product/create_product.py"
  output_path      = "../build/lambdas/create_product.zip"
}

data "archive_file" "file_lambda_deleteProduct" {
  type             = "zip"
  source_file     = "../src/lambda/product/delete_product.py"
  output_path      = "../build/lambdas/delete_product.zip"
}

data "archive_file" "file_lambda_getProduct" {
  type             = "zip"
  source_file     = "../src/lambda/product/get_product.py"
  output_path      = "../build/lambdas/get_product.zip"
}

data "archive_file" "file_lambda_listProducts" {
  type             = "zip"
  source_file     = "../src/lambda/product/list_products.py"
  output_path      = "../build/lambdas/list_products.zip"
}

data "archive_file" "file_lambda_updateProduct" {
  type             = "zip"
  source_file     = "../src/lambda/product/update_product.py"
  output_path      = "../build/lambdas/update_product.zip"
}

data "archive_file" "file_lambda_createProductModel" {
  type             = "zip"
  source_file     = "../src/lambda/product_model/create_product_model.py"
  output_path      = "../build/lambdas/create_product_model.zip"
}