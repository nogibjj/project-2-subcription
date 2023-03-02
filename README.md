[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
# Project 2: Kubernetes based Continuous Delivery - Subscription Manager

Do you hate that your subscription auto-renewed but you can do nothing because you forget to cancel it? Here is a microservice to remind you of your subscription renewal and urge you to cancel it if you want.

## Goals:
* Create a customized Docker container from the current version of Python that deploys a simple python script.
* Push image to DockerHub, or Cloud based Container Registery (ECR)
* Project should deploy automatically to Kubernetes cluster
* Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)


## Steps

1. Set up the virtual environment
    * `python3 -m venv env`
    * `source env/bin/activate`

2. Set up the database

3. Build application in Python Flask API.
    * First Set up Twilio account and test it.
