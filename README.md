# Trabajo Integrador para Sitemas Distribuidos 2023
## Consigna
Crear una aplicacion que este compuesta por un backend y un frontend que se comuniquen mediante una cola de mensajes Redis.
## Ejecucion
La url donde se ejecuta la caluduladora esta en:
    http:/10.230.40.13/calculadora/
### Prerequisitos
- Tener un cluster de kubernetes
- Tener activada la VPN zerotier y pertenecer al grupo
### Mediante applymanifest.sh
Ejecutar dentro de la carpeta del respositorio:  

    source applymanifest.sh
### Aplicando manifiestos de kubernetes
Aplicar los manifiestos 00-redis,01-backend y 02-frontend en orden:  

    kubeclt apply -f ./00-redis.yaml
    kubeclt apply -f ./01-backend.yaml
    kubeclt apply -f ./02-frontend.yaml
