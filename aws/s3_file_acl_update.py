import boto3

# Replace these with your AWS credentials or use environment variables or IAM roles
aws_access_key_id = '<ADD_ACCESS_KEY_HERE>'
aws_secret_access_key = 'ADD_SECRET_ACCESS_KEY_HERE'
region_name = 'eu-central-1'
bucket_name = 'pmtech-euc1stage-backoffice'
s3_path = 'my-assets/'

s3 = boto3.client('s3',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=region_name)

def modify_file_acl(file_key):
    new_acl = "public-read"
    try:
        print(f"ACL for file '{file_key}' set to '{new_acl}'")
        s3.put_object_acl(Bucket=bucket_name, Key=file_key, ACL=new_acl)
    except Exception as e:
        print(f"An error occurred: {e}")
      
def modify_s3_file_acl_using_paginator():
    paginator = s3.get_paginator("list_objects_v2")
    response = paginator.paginate(Bucket=bucket_name, Prefix=s3_path, PaginationConfig={"PageSize": 100})
    for page in response:
        files = page.get("Contents")
        for file in files:
            # print(f"file_name: {file['Key']}")
            modify_file_acl(file['Key'])

if __name__ == "__main__":
    modify_s3_file_acl_using_paginator()
