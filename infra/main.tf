provider "aws" {
  region  = "us-east-1"

}
resource "aws_dynamodb_table" "dynamodb_user"{
  name = "celer-user"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "id"
  attribute{
    name = "id"
    type = "S"
  }
}

resource "aws_lambda_function" "lambda" {
  function_name = "teste"
  filename         = data.archive_file.zip.output_path
  source_code_hash = data.archive_file.zip.output_base64sha256
  role    = aws_iam_role.lambda-role.arn
  handler = "hello.lambda_handler"
  runtime = "python3.8"
}