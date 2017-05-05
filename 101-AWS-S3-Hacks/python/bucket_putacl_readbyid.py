#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Grant read access to a bucket by CanonicalUser
- AWS CLI: aws s3api put-bucket-acl --bucket us-west-2.nag --grant-read id=xxxxxxxx

"""

import json
import boto3

acp = {
    "Grants": [
        {
            "Grantee": {
                "Type": "CanonicalUser",
                "ID": "xxxx"
            },
            "Permission" : "READ"
        }

    ],
    "Owner" : {
        "DisplayName": "nagm",
        "ID": "xxxx"

      }
}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_bucket_acl(Bucket=bucketname, AccessControlPolicy=acp)
