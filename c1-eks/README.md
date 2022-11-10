## Prerequisite
Login as an IAM user and not SSO.
AWS CLI installata sul computer, usando lo stesso user IAM del punto 1.
Installare kubectl
Helm installto sul computer

## IAM Roles
The first IAM role will be used by the EKS service. Open the IAM service and create a new role using the `EKS - Cluster` use case, which provides the `AmazonEKSClusterPolicy` policy. In the following example the new role is named `MS-eksClusterRole`.

![eks_role_1](images/eks_role_1.png)

Creare ruolo anche per node group


## Networking
In order to create the network will we use a CloudFormation template provided by AWS which will deploy public and private subnets and all the necessary components such as route table, Internet Gateway and NAT Gateway.
The template url is the following
```url
https://s3.us-west-2.amazonaws.com/amazon-eks/cloudformation/2020-10-29/amazon-eks-vpc-private-subnets.yaml
```

Open the CloudFormation console and create a new stack using the above mentioned model.

![stack_1](images/stack_1.png)

Name the stack `eks-net-01` and leave all the other values as default.

![stack_2](images/stack_2.png)

Reference:
https://docs.aws.amazon.com/eks/latest/userguide/creating-a-vpc.html



## EKS cluster deployment
Open the EKS console and create a new cluster named `eks-01` and selecting `MS-eksClusterRole` as Cluster service role.

![eks_1](images/eks_1.png)

In the networking tab select the VPC which were created by CloudFormation, in other words the one which contains `eks-net-01` in tha name. Do the same for the Security Group. For `Cluster endpoint access` select `Public and private`. Leave all the other parameters as default and create the cluster.

![eks_2](images/eks_2.png)

## Configurare kubectl
Create or update the kubeconfig file for your cluster:
https://aws.amazon.com/premiumsupport/knowledge-center/eks-cluster-connection/
```sh
aws eks --region eu-west-1 update-kubeconfig --name EKS-Cluster-01
```

Test your configuration:
```sh
kubectl get svc
```

## Creazione node group
screenshot

## Creazione e config namespace
kubectl create namespace marco-namespace
kubectl config set-context --current --namespace=marco-namespace