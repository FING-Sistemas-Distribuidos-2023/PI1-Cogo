source /rediscluster/create_cluster
kubeclt apply -f ./01-backend.yaml
kubeclt apply -f ./02-frontend.yaml