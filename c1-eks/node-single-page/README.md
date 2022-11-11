## Build and push Docker image to Docker Hub
```sh
$ docker build -t msignorini/kub-first-app:1 .
$ docker login
$ docker push msignorini/kub-first-app:1
```

## Create a deployment using the previous image
```sh
$ kubectl create deployment first-app --image=msignorini/kub-first-app
```

## View Kubernetes deployments
```sh
$ kubectl get deployments
```

## Delete Kubernetes deployment
```sh
$ kubectl delete deployment first-app
```

## View Kubernetes pods
```sh
$ kubectl get pods
```

## View Kubernetes pods info
```sh
$ kubectl describe pod first-app
```

## Expose deployment
```sh
$ kubectl expose deployment first-app --type=LoadBalancer --port=8080
$ kubectl expose deployment first-app --type=NodePort --port=8080
```

## View Kubernetes services
```sh
$ kubectl get services
```

## View Kubernetes services info
```sh
$ kubectl describe service first-app
```

## Delete Kubernetes services
```sh
$ kubectl delete service first-app
```

## Scale Up
```sh
$ kubectl scale deployment/first-app --replicas=3
```

## Update image
```sh
# Work only with image with version number
$ kubectl set image deployment/first-app kub-first-app=msignorini/kub-first-app:2
```

## Config file for Deployment
first-app-deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: first-app-deployment
spec: # configuration of the deployment
  replicas: 1 # default 1 if not specified
  selector:
    matchLabels: # (AND condition)
      project: first-app
      auhtor: marco
  template:
    metadata:
      labels: 
        project: first-app
        auhtor: marco
    spec: # configuration of individual pod
      containers:
        - name: first-node-app
          image: msignorini/kub-first-app:1
          livenessProbe:
            httpGet:
              path: /
              port: 8080
            periodSeconds: 3
            initialDelaySeconds: 10
```

## Create declarative deployment
```sh
$ kubectl apply -f first-app-deployment.yaml
```

## Delete declarative deployment
```sh
$ kubectl delete -f first-app-deployment.yaml
```

## Config file for Service
first-app-service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: first-app-service
spec:
  selector:
    project: first-app
  ports:
    - protocol: 'TCP'
      port: 80
      targetPort: 8080 # container listing port
  type: NodePort
```

## Create declarative service
```sh
$ kubectl apply -f first-app-service.yaml
```

## Single Config file for Service and Deployment
Use `---` as YAML separator. It is a best practice to have Service first then Deployment.
first-app-complete.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: first-app-service
spec:
  selector:
    project: first-app
  ports:
    - protocol: 'TCP'
      port: 80
      targetPort: 8080 # container listing port
  type: NodePort
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: first-app-deployment
spec: # configuration of the deployment
  replicas: 1 # default 1 if not specified
  selector:
    matchLabels: # (AND condition)
      project: first-app
      auhtor: marco
  template:
    metadata:
      labels: 
        project: first-app
        auhtor: marco
    spec: # configuration of individual pod
      containers:
        - name: first-node-app
          image: msignorini/kub-first-app:1
          livenessProbe:
            httpGet:
              path: /
              port: 8080
            periodSeconds: 3
            initialDelaySeconds: 10
```

## Create namespace
```sh
kubectl create namespace marco-namespace
```

## Set default namespace
```sh
kubectl config set-context --current --namespace=marco-namespace
```

## Delete namespace
```sh
kubectl delete namespace marco-namespace
```

## Single Config file for Service and Deployment without allowPrivilegeEscalation
Use `---` as YAML separator. It is a best practice to have Service first then Deployment.
first-app-complete.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: first-app-service
spec:
  selector:
    project: first-app
  ports:
    - protocol: 'TCP'
      port: 80
      targetPort: 8080 # container listing port
  type: NodePort
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: first-app-deployment
spec: # configuration of the deployment
  replicas: 1 # default 1 if not specified
  selector:
    matchLabels: # (AND condition)
      project: first-app
      author: marco
  template:
    metadata:
      labels:
        project: first-app
        author: marco
    spec: # configuration of individual pod
      securityContext:
        runAsUser: 1000
        runAsGroup: 3000
        fsGroup: 2000
      containers:
        - name: first-node-app
          image: msignorini/kub-first-app:1
          livenessProbe:
            httpGet:
              path: /
              port: 8080
            periodSeconds: 3
            initialDelaySeconds: 10
          securityContext:
            allowPrivilegeEscalation: false
```

## Create declarative deployment with custom namespace
```sh
$ kubectl apply -f first-app-complete-sec.yaml --namespace=marco-namespace
```

## Delete declarative deployment with custom namespace
```sh
$ kubectl delete -f first-app-complete-sec.yaml --namespace=marco-namespace
```

## Delete namespace
```sh
kubectl delete namespace marco-namespace
```