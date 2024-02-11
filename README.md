# AWS Cloud Cost Optimization
This repo will contain lambda functions for the optimization of AWS resources.

## Identifying Stale Elastic Block Storage Snapshots
This will create a Lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and delete them to save on storage costs.



## S3 Cost Optimization
 AWS Lambda function using Python and Boto3 to transition objects from Amazon S3 Standard storage to S3 Glacier after 30 days
