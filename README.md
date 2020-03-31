# Lambda Setup for Flask

There are several methods to deploy serverless function on  AWS Lambda, as follows:

- Pure Aws Labmda procedure
- Zappa for Python (https://github.com/Miserlou/Zappa)
- Serverless CLI (serverless.com and pypi packages, also https://github.com/serverless) 
    1. Use, the default out of box, serverless handler to return json and CORS can be done through settings in serverless.xml
    2. **Stay with Flask to work as API**

Here will cover the methods 2, because it is a complete python program infra-structure and easily to be compared or transmitted from old projects onto Lambda.


## Concepts 

#### AWS Lambda Layers

There are always additional packages as dependencies need to be installed, no matter Javascript or Python. These dependencies are packaged into Lambda Layers to provide these fundamental modules and functions. Here are quotes from docs of AWS: https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html

    You can configure your Lambda function to pull in additional code and content in the form of layers. A layer is a ZIP archive that contains libraries, a custom runtime, or other dependencies. With layers, you can use libraries in your function without needing to include them in your deployment package.

#### Lambda Function Region

Region can be configured in the auto generaged serverless.xml, otherwise the default is us-east-1.

The functions deployed in other region can be remove by:

```
sls remove --region us-east-1
```

#### VPC and Security Groups for Lambda functions

Fcuntions are similiar to resources like EC2, the connectivity relys on the VPC/Region/SecurityGroups.

#### Flask Factory mode

Flask starts using factory mode, it runs like:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

For Lambda functions, this flask app need to be changed to be run by Python. Here using ```python api.py```, in which **flaskr** is imported as python module.


More details see the file of ```api.py``` and official docs here:
https://flask.palletsprojects.com/en/1.0.x/tutorial/factory/



## SLS Deoplyment Procedure

### Setup accounts 

- account on serverless.com
- in the profile, connect AWS.

The permissions for user/group/role all done here.


### Installtion

serverless commands:
```
# Install the Serverless Framework.
npm install -g serverless

# Log into your Serverless Framework account.
serverless login

# Start a new Serverless Framework service, or connect the dashboard to an existing service.
serverless --org <USER ACCOUNT> --app <APP NAME>

# Deploy your new service, or redeploy your existing service.
cd <APP NAME>
serverless deploy
```

serverless plugin:
```
# wsgi handler for python lambda
sls plugin install -n serverless-wsgi

# lambda layer for python requirements
sls plugin install -n serverless-python-requirements
```

localhost flask test:
```
sls wsgi serve
```


Coding before ```serverless deploy``` or ```sls deploy```.

### Database Connection

Under the configuration of Functions in AWS Lambda, there are sections for VPC and Database proxies (preview), in which only RDS database available so far, March 2020.

Here, configure the VPC of Lambda function within same VPC (whatever at least 2 available zones) and same security group with AWS DocumentDB (MongoDB).


