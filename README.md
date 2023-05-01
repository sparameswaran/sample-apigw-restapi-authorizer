# sample-apigw-restapi-authorizer

Sample project for building and testing Lambda Authorizer for API Gateway.
This project contains source code and supporting files for a serverless application that you can deploy with the AWS Serverless Application Model (AWS SAM) command line interface (CLI). It includes the following files and folders:

- `src` - Code for the application's Lambda function.
- `template.yaml` - A template that defines the application's AWS resources.

## Project Details
The application demonstrates building API Gateway REST APIs protected using [Lambda Authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html). These resources are defined in the `template.yaml` file in this project. 
You can update the template to add AWS resources through the same deployment process that updates your application code.
The authorizer expects an authorization header (**AuthorizationToken** set to `allow` or `deny`) in the requests to communicate with a AWS Lambda backend, external service or Lambda as proxy.
Build using SAM cli (requires Python3.9): sam build followed by sam deploy –guided.

### Testing against sample Urls: 

Use curl with `-H "AuthorizationToken: allow"` or `-H "AuthorizationToken: deny"` to test against the api gateway endpoints with appropriate path.

Supported endpoints:
* Lambda Backend (GET) : https://<API_GATEWAY_REST_API_ENDPOINT>.amazonaws.com/dev (custom mapping of requests to backend)
* Lambda Proxy as Backend (GET) : https://<API_GATEWAY_REST_API_ENDPOINT>.amazonaws.com/dev/lambdaProxy (no request mapping template allowed, everything passed directly to Lambda)
* External Service (GET or POST) : https://<API_GATEWAY_REST_API_ENDPOINT>.amazonaws.com/dev/extService (custom mapping of requests to backend)


## Deploy the sample application

The AWS SAM CLI is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the AWS SAM CLI, you need the following tools:

* AWS SAM CLI - [Install the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community).

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

The API Gateway endpoint API will be displayed in the outputs when the deployment is complete.

## Use the AWS SAM CLI to build and test locally

Build your application by using the `sam build` command.

```bash
my-application$ sam build
```

```bash
aws cloudformation delete-stack --stack-name test-restapi-authorizer
```

## Resources

For an introduction to the AWS SAM specification, the AWS SAM CLI, and serverless application concepts, see the [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).

Next, you can use the AWS Serverless Application Repository to deploy ready-to-use apps that go beyond Hello World samples and learn how authors developed their applications. For more information, see the [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/) and the [AWS Serverless Application Repository Developer Guide](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/what-is-serverlessrepo.html).
