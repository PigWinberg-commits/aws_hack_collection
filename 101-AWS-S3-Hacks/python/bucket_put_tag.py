#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Tag an s3 bucket
- AWS CLI: aws s3api put-bucket-tagging --bucket us-west-2.nag --tagging 'TagSet=[{Key=name,Value=nag}]'
"""

import boto3

if __name__ == "__main__":
#   client = boto3.client('s3')
   client = boto3.client('s3',region_name="us-west-2")
   bucketname = "us-west-2.nag"
   print client.put_bucket_tagging(Bucket=bucketname,Tagging={
        'TagSet': [
            {
                'Key': 'Name',
                'Value': 'Nag'
            },
        ]
    })
