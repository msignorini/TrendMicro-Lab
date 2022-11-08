import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# DynamoDB table name
dynamodbTableName = 'users'

# DynamoDB client
dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table(dynamodbTableName) 

def lambda_handler(event, context):

    logger.info(event)
    httpMethod = event['httpMethod']

    if httpMethod == 'GET':
        ret = getUsers()
    elif httpMethod == 'POST':
        ret = insertUser(json.loads(event['body']))
    else:
        message = {"message": "Operation not allowed"}
        ret['statusCode'] = 404
        ret['body'] = message
    
    logger.info(ret)
    return {
        'statusCode': ret['statusCode'],
        'body': ret['body']
    }


def getUsers():
    logger.info('Get Users function')
    try: 
        response = table.scan() 
        result = response['Items']

        while 'LastEvaluatedKey' in response: 
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            result.extend(response['Items'])
 
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }
    except Exception as e:
        logger.exception(e)
        message = {"message": "Error getting the users"}
        return {
            'statusCode': 400,
            'body': json.dumps(message)
        }


def insertUser(requestBody):
    logger.info('Insert User function')
    logger.info(requestBody)
    try: 
        table.put_item(Item=requestBody)
        message = {"message": "Succesfully inserted user"}
        return {
            'statusCode': 200,
            'body': json.dumps(message)
        }
    except Exception as e:
        logger.exception(e)
        message = {"message": "Error saving the user"}
        return {
                'statusCode': 400,
                'body': json.dumps(message)
        }