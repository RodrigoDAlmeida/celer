provider "aws" {
  region  = "us-east-1"

}
resource "aws_dynamodb_table" "dynamodb_user"{
  name = "celer-user"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "id"
  tags = {"App":"celer"}
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

resource "aws_dynamodb_table" "dynamodb_company"{
  name = "celer-company"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "id"
  tags = {"App":"celer"}
  attribute{
    name = "id"
    type = "S"
  }
  attribute{
    name = "abbreviation"
    type = "S"
  }
  global_secondary_index {
    hash_key           = "abbreviation"
    name               = "abbreviation-index"
    projection_type    = "ALL"
  }
}

resource "aws_dynamodb_table" "dynamodb_product"{
  name = "celer-product"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "id"
  tags = {"App":"celer"}

  attribute{
    name = "id"
    type = "S"
  }
  attribute{
    name = "company_abbreviation"
    type = "S"
  }
  global_secondary_index {
    hash_key           = "company_abbreviation"
    name               = "company-abbreviation-index"
    projection_type    = "ALL"
  }
}




