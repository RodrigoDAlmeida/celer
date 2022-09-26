# Celer
Celer is a simple POC of a ReactJS web application using some AWS Services, as like Lambda (Python), DynamoDB, API Gateway, Stepfunction and provisioned with Terraform.


![Target Architecture](https://serving.photos.photobox.com/03359686cae8336f847bcdd5b287cdbffe5413620a7e888a479b14d95d7b5fc140644f7e.jpg)

## How to Start

With Terraform properly configured to an AWS account, open the terminal in the /infra directory and run:
```shell
terraform apply
```
After execution, all infrastructure will be provisioned in your AWS account and you are ready to start using

## Database Scheme

![Database Scheme](https://serving.photos.photobox.com/19452723a12274f6c79318124e3789c5961f49c46b8d94029bb54b3030650353b198fa76.jpg)
