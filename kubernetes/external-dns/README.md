# External DNS instructions
Create key file and download into `key.json`.
Install using 
```
helm --namespace nginx-ingress upgrade external-dns bitnami/external-dns --values values.yaml --set-file google.serviceAccountKey=key.json
```