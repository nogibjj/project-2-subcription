[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
# Project 2: Kubernetes based Continuous Delivery - Subscription Manager

Via Apprunner: https://d44eqbhn5b.us-east-1.awsapprunner.com/

This repository contains the code for a subscription service that allows users to subscribe to various services and manage their subscriptions. The project uses Python language and is built and tested using Minikube.

## Intro

Do you hate that your subscription auto-renewed but you can do nothing because you forget to cancel it? Here is a microservice to remind you of your subscription renewal and remind you to cancel it if you want.

## Goals:
* Create a customized Docker container from the current version of Python that deploys a simple python script.
* Push image to DockerHub, or Cloud based Container Registery (ECR)
* Project should deploy automatically to Kubernetes cluster
* Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)


## Automatic Deployment
A. Containerized with Docker and Deployed with AWS ECR and Apprunner.

   1. Clone and open the repo in AWS Cloud9, create source the virtual environment
   ```
   python3 -m venv env
   source env/bin/activate
   ```
   2. Create a Repository in AWS ECR.
   ![ECR](https://user-images.githubusercontent.com/68854273/235836315-1bdb3cf5-b844-497c-b32a-124167551e2a.png)
   3. Write the corresponding Dockerfile (skip if done in local)
   4. View the push commands in ECR, follow the steps in Cloud9 terminal.
   ![ECR Push Commands](https://user-images.githubusercontent.com/68854273/235836530-7305f394-3f11-4b1f-be4c-db66287f98d5.png)
   ```
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 962268758789.dkr.ecr.us-east-1.amazonaws.com
   ```
   ```
   docker build -t subscription-manager .
   ```
   ```
   docker tag subscription-manager:latest 962268758789.dkr.ecr.us-east-1.amazonaws.com/subscription-manager:latest
   ```
   ```
   docker push 962268758789.dkr.ecr.us-east-1.amazonaws.com/subscription-manager:latest
   ```
   After it finishs, you can go back to the ECR and view the images.
   ![ECR Images](https://user-images.githubusercontent.com/68854273/235837125-2672abfe-b038-42df-9c1b-0b7707b12a49.png)
   5. Go to AWS Apprunner, click `create services`, choose the corresponding Container image URI. You can set other field as default. Click `Create and Deploy`. 
   *Note: To pass the health attack, you need to make sure the host address in app.py is "0.0.0.0", and the port number should match the one you expose in Dockerfile.*
   6. After it finish, the program is deployed and can be visited at https://d44eqbhn5b.us-east-1.awsapprunner.com/ .
   
   7. Demos
   Homepage
   ![Homepage](https://user-images.githubusercontcreate deployment and view it
    kubectl create deployment hi-minikube --image=registry.hub.docker.com/sasays/randfood
    kubectl get deploymentsent.com/68854273/235838816-b070825c-85e5-44ac-b3d9-bf81eba07419.png)
   Add a subscription
   ![Add](https://user-images.githubusercontent.com/68854273/235838852-e23b46d7-6cf9-473b-a3de-0ab41dbca81f.png)
   Delete a subscription
   ![Inactivate](https://user-images.githubusercontent.com/68854273/235838881-e8bcd9e8-ffd7-4449-bd28-08633f5a8d1b.png)

B. Minikube
   1. Login to Docker Hub. Build and push:
   ```
   docker login --username=<your-dockerhub-username>
   docker build . -t <your-dockerhub-username>/<your-application-name>
   docker push <your-dockerhub-username>/<your-application-name>
   ```
   2. `minikube start`
   3. Run `minikube dashboard --url` to view dashboard
   4. create deployment and view it
   ```
   kubectl create deployment sub --image=registry.hub.docker.com/zhuminghui17/sub
   kubectl get deployments
   ```
   5. deploy microserver and expose it
   ```
   kubectl expose deployment sub --type=LoadBalancer --port=8080
   kubectl get service sub
   minikube service sub  --url
   ```
   6. we can get `http://127.0.0.1:51757` url.
   ![img](https://user-images.githubusercontent.com/68854273/235875844-2bfc0192-f8a9-4938-a7c0-8dd4fd49b3d0.png)
   

   

