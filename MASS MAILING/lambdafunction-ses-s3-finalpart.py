import boto3
import json
import os 

def get_latest_object(bucket_name):
    s3 = boto3.client('s3', region_name='us-east-1')

    # List objects in the specified bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Check if there are any objects in the bucket
    if 'Contents' in response:
        # Find the object with the latest LastModified timestamp
        latest_object = max(response['Contents'], key=lambda x: x['LastModified'])
        return latest_object
    else:
        return None

def get_file_size(bucket_name, object_key):
    s3 = boto3.client('s3', region_name='us-east-1')
    response = s3.head_object(Bucket=bucket_name, Key=object_key)
    file_size = response['ContentLength']
    return file_size

def get_file_extension(object_key):
    return os.path.splitext(object_key)[1]

def lambda_handler(event, context):
    # Define recipient email addresses
    recipient_emails = ["email_1", "email_2"]

    # Define the name of the S3 bucket
    bucket_name = "ogafridayy"

    # Get the latest object in the bucket
    latest_object = get_latest_object(bucket_name)

    if latest_object:
        # Get the latest object's key, size, and extension
        object_key = latest_object['Key']
        file_size = get_file_size(bucket_name, object_key)
        file_extension = get_file_extension(object_key)

        # Create an SES client
        ses_client = boto3.client('ses', region_name='us-east-1')

        # Generate a pre-signed URL for the latest object
        s3 = boto3.client('s3', region_name='us-east-1')
        s3_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_key}, ExpiresIn=36000000)

        # Compose the email message
        email_subject = f"Download Latest Attachment: {object_key}"

        email_body = f"""
<html>
<head></head>
<body>
    <p>Dear Recipients,</p>
    <p>We are pleased to inform you that the latest file has been shared with you. Please find the details below:</p>
    <ul>
        <li><strong>File Name:</strong> {object_key}</li>
        <li><strong>File Size:</strong> {file_size} bytes</li>
        <li><strong>File Type:</strong> {file_extension} Document</li>
    </ul>
    <p>To download the file, simply click the link below:</p>
    <p><a href="{s3_url}">Download File</a></p>
    <p>If you have any questions or need further assistance, please don't hesitate to contact us.</p>
    <p>Best regards,<br>Sender's Name</p>
</body>
</html>
"""

        # Send the email with the attachment to multiple recipients
        response = ses_client.send_email(
            Source="azukaikeojukwu@gmail.com",
            Destination={"ToAddresses": recipient_emails},
            Message={
                "Subject": {"Data": email_subject},
                "Body": {"Html": {"Data": email_body}}
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f"Email sent to {', '.join(recipient_emails)} with the latest attachment URL.")
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps("No objects found in the bucket.")
        }
