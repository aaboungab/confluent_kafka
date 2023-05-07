import boto3

def upload_empty_file_to_s3(bucket_name, file_name):
    # Create a new session using your AWS credentials
    session = boto3.Session(
        aws_access_key_id='AKIAXKRAK3ZCAPZGZALK',
        aws_secret_access_key='k8O7bQ7QO8QQ/NVRGgm+6+SkmMoPlfYX08znEKGY',
    )

    # Create an S3 client using the session
    s3_client = session.client('s3')

    # Upload an empty file to the specified bucket
    try:
        s3_client.put_object(Body='', Bucket=bucket_name, Key=file_name)
        print(f"Empty file '{file_name}' uploaded to '{bucket_name}' successfully.")
    except Exception as e:
        print(f"Error uploading the file: {e}")

# Set the bucket name and file name
bucket_name = 'my-data-bucket-aa-s3'
file_name = 'file.txt'

# Call the function to upload the empty file to S3
upload_empty_file_to_s3(bucket_name, file_name)