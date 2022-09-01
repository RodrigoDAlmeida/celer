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
  attribute{
    name = "login"
    type = "S"
  }
  global_secondary_index {
    hash_key           = "login"
    name               = "login-index" 
    projection_type    = "ALL"
  }
}




