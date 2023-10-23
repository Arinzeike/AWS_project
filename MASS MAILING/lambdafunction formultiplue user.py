import boto3
import json
import os

def get_file_size(bucket_name, object_key):
    s3 = boto3.client('s3', region_name='us-east-1')
    response = s3.head_object(Bucket=bucket_name, Key=object_key)
    file_size = response['ContentLength']
    return file_size

def get_file_extension(object_key):
    return os.path.splitext(object_key)[1]

def lambda_handler(event, context):
    # Define recipient email addresses
    recipient_emails = ["aikeojukwu@gmail.com", "ikeojukwua@gmail.com", "chikaikeojukwu@gmail.com"]

    # Define the name of the S3 bucket and the object (file) you want to attach
    bucket_name = "mys3lambda33"
    object_key = "34test.txt"

    # Get the file size
    file_size = get_file_size(bucket_name, object_key)

    # Get the file extension
    file_extension = get_file_extension(object_key)

    # Create an SES client
    ses_client = boto3.client('ses', region_name='us-east-1')

    # Generate a pre-signed URL for the S3 object
    s3 = boto3.client('s3', region_name='us-east-1')
    s3_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_key}, ExpiresIn=36000000)

    # Compose the email message
    email_subject = f"Download Attachment: {object_key}"

    email_body = f"""
<html>
<head></head>
<body>
    <p>Dear Recipients,</p>
    <p>We are pleased to inform you that a new file has been shared with you. Please find the details below:</p>
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
        'body': json.dumps(f"Email sent to {', '.join(recipient_emails)} with the attachment URL.")
    }
