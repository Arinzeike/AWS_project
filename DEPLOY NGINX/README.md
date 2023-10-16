# Deploy an NGINX Server on EC2 Using CloudFormation CLI

This guide will walk you through the process of deploying an NGINX web server on an Amazon Elastic Compute Cloud (EC2) instance using the AWS CloudFormation Command Line Interface (CLI). AWS CloudFormation is a service that allows you to provision and manage AWS resources using infrastructure as code (IAC). NGINX is a popular web server that can serve as a reverse proxy, load balancer, or a simple web server.

## Prerequisites

Before you begin, ensure you have the following prerequisites in place:

1. **AWS Account**: You should have an active AWS account. If you don't have one, you can sign up for one at [AWS Signup](https://aws.amazon.com/).

![Alt text](<Images/AWS ACC.png>)

2. **AWS CLI and AWS CloudFormation CLI**: Make sure you have the AWS Command Line Interface (CLI) and AWS CloudFormation CLI installed and configured on your local machine. You can download and install them from [AWS CLI Installation](https://aws.amazon.com/cli/) and [AWS CloudFormation CLI Installation](https://aws.amazon.com/cloudformation/).

![Alt text](<Images/AWS CLI AUTH.png>)


## Step 1: Create a CloudFormation Template

Create a CloudFormation template that describes the resources you want to provision. In this case, it's an EC2 instance running NGINX.

![Alt text](<Images/Json Template.png>)


## Step 2: Deploy the Stack

![Alt text](<Images/empty stack.png>)

Use the AWS CloudFormation CLI to deploy the CloudFormation stack, which will create the EC2 instance running NGINX:
```
aws cloudformation create-stack --stack-name(NAME)  --template-body (file path) --capabilities CAPABILITY_IAM 
```

This command will initiate the creation of your stack. You can monitor the stack creation progress using the AWS Management Console or the CLI.

![Alt text](<Images/CREATE STACK.png>)

![Alt text](<Images/stack created CLI.png>)

![Alt text](<Images/stack created GUI.png>)


## Step 3: Access the NGINX Server
Once the stack creation is complete, you can access the NGINX server by opening a web browser and entering the public IP address of the EC2 instance. Follow these steps:

1. **Obtain the Public IP Address:**

In the AWS Management Console, navigate to the EC2 service and select your running EC2 instance. Look for the "Public IPv4 address" in the instance details. Note down this address.

![Alt text](<Images/IP ADDRESS.png>)

2.  **Access the NGINX Web Server:**

Open a web browser on your local machine.
In the address bar, enter the public IP address of your EC2 instance.
```
Example: http://public-ip-address/
```
This will take you to the NGINX web server's default welcome page.

Now you can easily access the NGINX web server by inputting the public IP address in your web browser without the need for SSH access

![Alt text](<Images/WELCOME NG.png>)

## Step 4: Clean Up

To avoid incurring additional costs, make sure to delete the CloudFormation stack when you're done with the NGINX server:

```
aws cloudformation delete-stack --stack-name (NAME)
```

![Alt text](<Images/del stack.png>)

![Alt text](<Images/STACK DELETED CLI.png>)

![Alt text](<Images/STACK DELETED GUI.png>)
## Conclusion

You've successfully deployed an NGINX server on an EC2 instance using the AWS CloudFormation CLI. This approach allows you to automate the provisioning and management of your AWS resources in a consistent and repeatable manner. Remember to clean up your resources to avoid ongoing charges in your AWS account.