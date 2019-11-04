# coding: utf-8
import boto3
session= boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for b in s3.buckets.all():
    print(b)
