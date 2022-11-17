# c1-python-lambda

## Description
This application is a proof of concept for testing `TrendMicro Cloud One Application Security` on a `Python 3.8 Lambda` function running in AWS.

![Architecture](images/architecture.png)

## DynamoDB
Create a new table named `users` with partition key `email` of type String.

![DynamoDB](images/create_dynamo.png)

## Lambda
Create a new lambda function from scratch named `c1-python-lambda` using runtime `Python 3.8`, architecture `x86_64` and existing role `MS-Lambda-API`.

![Lambda](images/create_lambda.png)

Copy and paste the source code in the `Code source` editor, then save it and click `Deploy`.

![LambdaCode](images/lambda_code.png)


## API Gateway
Create a new API Gateway of type `REST API` then in the next page select protocol `REST` and create `New API`. Use `c1-python-lambda-api` as the API name.

![APIGW](images/apigw_create.png)

Create Method a GET method selecting `Use Lambda Proxy integration` and lambda function `c1-python-lambda`.

![APIGW_get](images/apigw_get.png)

Create Method a POST method selecting `Use Lambda Proxy integration` and lambda function `c1-python-lambda`.

![APIGW_post](images/apigw_post.png)

Then deploy API creating a new deployment stage call `prod`.

![APIGW_deploy_1](images/apigw_deploy_1.png)

Take a note of the invoke URL which will be use in Postman, in this case `https://0u5d1ab8i4.execute-api.eu-west-1.amazonaws.com/prod`

![APIGW_deploy_2](images/apigw_deploy_2.png)

## Postman
Example of GET usage
![postman_get](images/postman_get.png)

Example of POST usage, it this case a body must be defined, like the one in the following example:

Body (RAW/JSON)
```json
{
    "username": "valerio",
    "email": "valerio@gmmail.com"
}
```
![postman_post](images/postman_post.png)



## TrendMicro
#### Reference
https://cloudone.trendmicro.com/docs/application-security/aws-lambda-with-official-runtimes/#python-layers

Add a new Layer to the lambda function and specify the following ARN:
```
arn:aws:lambda:eu-west-1:800880067056:layer:CloudOne-ApplicationSecurity-python:1
```

![lambda_layer](images/lambda_layer.png)

Then configure the following environment variables:
```txt
AWS_LAMBDA_EXEC_WRAPPER: /opt/trend_app_protect
TREND_AP_CACHE_DIR: /tmp/trend_cache
TREND_AP_HELLO_URL: https://agents.de-1.application.cloudone.trendmicro.com/
TREND_AP_HTTP_TIMEOUT: 5
TREND_AP_INITIAL_DELAY_MS: 1
TREND_AP_KEY: <get_it_on_trendmicro_dashboard>
TREND_AP_LOG_FILE: STDERR
TREND_AP_MAX_DELAY_MS: 100
TREND_AP_MIN_REPORT_SIZE: 1
TREND_AP_PREFORK_MODE: False
TREND_AP_READY_TIMEOUT: 30
TREND_AP_SECRET: <get_it_on_trendmicro_dashboard>
TREND_AP_TRANSACTION_FINISH_TIMEOUT: 10
```

![lambda_env](images/lambda_env.png)

#### Attack Patterns
Malicious Payload Example 1
```
https://7c6x4l6zga.execute-api.eu-west-1.amazonaws.com/prod?url=https%3A%2F%2Fphishingexample.com/goodbankfrauddept
```

Malicious Payload Example 2
```
https://7c6x4l6zga.execute-api.eu-west-1.amazonaws.com/prod?url=https%3A%2F%2Fmalwareexample.com/currentevent.pdf
```