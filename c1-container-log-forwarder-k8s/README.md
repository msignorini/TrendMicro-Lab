# Cloud One Container Security Runtime Events Forwarder

Login to ECR
```sh
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 287836408715.dkr.ecr.eu-west-1.amazonaws.com
```

Build the image
```sh
docker build -t 287836408715.dkr.ecr.eu-west-1.amazonaws.com/c1cs_log_forwarder:1  .
```

Push the image to ECR
```sh
docker push 287836408715.dkr.ecr.eu-west-1.amazonaws.com/c1cs_log_forwarder:1
```

Fill the `c1cs-log-forwarder-ecr-sec.yaml` with the relevant env variable and apply it: container to ECR
```sh
kubectl apply -t c1cs-log-forwarder-ecr-sec.yaml
```


