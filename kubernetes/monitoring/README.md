### Create a cluster with kind

We're going to create the cluster with kind tool with 3 nodes by running this command

```bash
kind create cluster --config kind.yaml
```

In order to deploy all the necessary monitoring components we need to
- 1) Deploy all the needed CRDs
- 2) Deploy all the monitoring components (Configmaps,Services,Deployments,etc)

We should run the following kubectl commands
```bash
kubectl create -f manifests/setup
kubectl create -f manifests/
```
