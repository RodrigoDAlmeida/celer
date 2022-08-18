variable "jar_path"{
  type = string
  default = "../build/libs/yore-celer-1.0-SNAPSHOT-all.jar"
}

variable "java_runtime" {
  type = string
  default = "java11"
}

variable "package" {
  type = string
  default = "com.yore.celes.lambda."
}

provider "archive" {}
data "archive_file" "zip" {
  type        = "zip"
  source_file = "../src/lambda/hello.py"
  output_path = "../build/hello.zip"
}