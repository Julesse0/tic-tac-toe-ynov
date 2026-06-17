# tic-tac-toe

Chart Helm pour packager le jeu CLI Tic Tac Toe.

## Fichiers principaux

- `Chart.yaml` : métadonnées du chart.
- `values.yaml` : paramètres modifiables.
- `templates/` : manifests Kubernetes rendus par Helm.

## Paramètres exposés

- `image.repository` et `image.tag`
- `replicaCount`
- `config` pour la ConfigMap
- `ingress.enabled` et `ingress.host`
- `resources.requests` et `resources.limits`

## Validation

```bash
k3d cluster create ynov-cluster --image rancher/k3s:v1.27.4-k3s1 --api-port 127.0.0.1:6550                                                 

helm lint k8s/helm/tic-tac-toe
helm template k8s/helm/tic-tac-toe
helm install tic-tac-toe-app k8s/helm/tic-tac-toe -n atelier-k8s --create-namespace
helm upgrade tic-tac-toe-app k8s/helm/tic-tac-toe -n atelier-k8s --set replicaCount=2 --set config.APP_ENV=staging
helm uninstall tic-tac-toe-app -n atelier-k8s
```

Le namespace utilisé pour la validation est `tic-tac-toe`.

## Exemple d'upgrade

```bash
helm upgrade mon-app k8s/helm/tic-tac-toe -n tic-tac-toe --set replicaCount=3 --set config.APP_ENV=preprod
```
