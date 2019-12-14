# Pod Disruption Budgets for kube-system pods

For the cluster autoscaler to function correctly, PDBs must be specified in the kube-system namespace

NB: Metric server only runs one POD and will be unavailable for 1 minute when starting. This will affect HPA!
