"""
This is a script to backup from local to AWS S3 bucket
"""
import boto3
import shutil
import datetime
import os

# declare backup_file as a fuction:
def backup_file(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name, 'gztar', source)
    return backup_file_name + ".tar.gz"  # return the backup file name with .tar.gz extension

# variables for source and destination directories:
source = "/home/ubuntu/PYTHON_PRACTICE"
destination = "/home/ubuntu/PYTHON_PRACTICE/backups"

# calling boto3 resource to connect to S3 bucket:
s3 = boto3.resource('s3')

# declare upload_backup as a function:
def upload_backup(s3,backup_path,bucket_name,key_name):
    with open(backup_path,'rb') as data: # get the backup file in binary mode and read it, then store it in data variable
        s3.Bucket(bucket_name).put_object(Key=key_name, Body=data) # upload in S3 bucket using put_object method with key_name and data as parameters
    print("Upload backup to S3 bucket completed successfully") # success message after uploading backup to S3 bucket

# variable for S3 bucket name:
bucket_name = "sd00pythonbackup"

# Calling functions:
backup_path = backup_file(source,destination)
upload_backup(s3,backup_path,bucket_name,os.path.basename(backup_path)) # use os.path.basename to get the file name from the backup_path

