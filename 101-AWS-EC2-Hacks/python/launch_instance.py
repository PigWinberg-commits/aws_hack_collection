#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Launch an EC2 instance
- Info   : Launch an EC2 instance
"""

import boto

def launch():
    ec2 = conn_default.run_instances("ami-1be5e672",key_name="test",instance_type="m1.small",security_groups=['test'])
    print ec2

if __name__ == "__main__":
   conn_default = boto.connect_ec2()
   launch()
