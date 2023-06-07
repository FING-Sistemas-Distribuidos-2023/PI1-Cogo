# Trabajo Integrador para Sitemas Distribuidos 2023

## Descripción del Trabajo integrador
El trabajo integrador consiste en crear una aplicacion compuesta por 3 componentes un "backend", un "frontend" y una cola de mensjaes "Redis" contenerizados y que corran en un cluster de kubernetes con 3 nodos.

Para este trabajo he decidido que la aplicació sera una calculadora. La aplicación esta totalmente desarollada en python y utilizando el framework django para generar las vistas del frontend.

Las imagenes de los dockers utilizados por el manifiesto frontend y backend han sido publicadas en docker.hub: 
- https://hub.docker.com/r/mrtc101/frontend
- https://hub.docker.com/r/mrtc101/backend	

## Contenido de los manifiestos
En los manifiestos de kubernetes se crean los siguientes objetos de kubernetes:
- 00-redis.yaml : contiene declarado el pod llamado redis en el que corre la imagen de redis sobre un alpine linux y el objeto service llamdo redis-service.
- 01-backend.yaml : contiene delcarado el pod con el container donde corre el backend.
- 02-frontend.yaml : contiene declarado el pod con el container donde corre le frontend, el frontend-service y el frontend-ingress.

## Prerequisitos
- La IP en la que se encuentra el nginx-ingress-controller es la 10.230.40.11. El dominio que permite el acceso a la aplicación es el http:/martin.integrador/ es nesesario ingresar desde este dominio para poder ser redirigido al container que sirve la pagina.

Como no se trata de un dominio registrado es nesesario agregar al archivo /etc/hosts del sistema la siguiente linea:
	10.230.40.11    martin.integrador

## Aplicando manifiestos de kubernetes
Para poner en funcionamiento la aplicación es nesesario aplicar los manifiestos de kubernetes 00-redis,01-backend y 02-frontend en orden:  

    kubeclt apply -f ./00-redis.yaml
    kubeclt apply -f ./01-backend.yaml
    kubeclt apply -f ./02-frontend.yaml
    
Esto puede hacerse simplemente ejecutando el archivo applymanifests.sh
	source applymanifests.sh
