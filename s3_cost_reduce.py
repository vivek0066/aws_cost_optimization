import boto3

def lambda_handler(event, context):
    # Set your S3 bucket name
    bucket_name = 's3-standard-storage-bucket'
    
    # Set the rule name for the lifecycle policy
    rule_name = 'glacier-transition-rule'
    
    # Create an S3 client
    s3 = boto3.client('s3')
    
    # Define the lifecycle configuration
    lifecycle_configuration = {
        'Rules': [
            {
                'ID': rule_name,
                'Filter': {'Prefix': ''},  # Apply the rule to all objects
                'Status': 'Enabled',
                'Transitions': [
                    {
                        'Days': 30,
                        'StorageClass': 'GLACIER'
                    }
                ]
            }
        ]
    }

    # Apply the lifecycle configuration to the bucket
    s3.put_bucket_lifecycle_configuration(Bucket=bucket_name, LifecycleConfiguration=lifecycle_configuration)
    
    print(f"Lifecycle rule '{rule_name}' applied to bucket '{bucket_name}' for Glacier transition after 30 days.")
