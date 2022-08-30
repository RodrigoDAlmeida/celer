provider "aws" {
  region  = "us-east-1"

}
resource "aws_dynamodb_table" "dynamodb_user"{
  name = "celer-user"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "id"
  range_key  = "login"
  attribute{
    name = "id"
    type = "S"
  }
  attribute {
    name = "login"
    type = "S"
  }
}


