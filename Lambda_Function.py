import json
import boto3
import random

dynamodb = boto3.resource('dynamodb')

drivers_table = dynamodb.Table('Drivers')
rides_table = dynamodb.Table('Rides')

def lambda_handler(event, context):
    
    user_id = event.get('user_id', 'U1')
    ride_id = "R" + str(random.randint(100,999))
    
    response = drivers_table.scan()
    drivers = response['Items']
    
    available_driver = None
    for driver in drivers:
        if driver['status'] == 'available':
            available_driver = driver
            break
    
    if not available_driver:
        return {
            'statusCode': 200,
            'body': 'No drivers available'
        }
    
    driver_id = available_driver['driver_id']
    
    rides_table.put_item(
        Item={
            'ride_id': ride_id,
            'user_id': user_id,
            'driver_id': driver_id,
            'status': 'assigned'
        }
    )
    sns = boto3.client('sns')

    sns.publish(
        TopicArn="arn:aws:sns:ap-south-1:506609161158:RideNotifications",
        Message=f'New ride assigned: {ride_id}, Driver: {driver_id}',
        Subject='Ride Alert'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'ride_id': ride_id,
            'driver_assigned': driver_id
        })
    }