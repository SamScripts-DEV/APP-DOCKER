
# Proyecto con Docker Compose

Este proyecto utiliza Docker Compose para levantar múltiples servicios, incluidos servidores web (3 nodos), balanceador de carga NGINX, bases de datos (maestra y esclava), phpMyAdmin para gestión de bases de datos y Locust para pruebas de carga.

## Requisitos previos

1. **Docker**: Asegúrate de tener Docker instalado en tu máquina. Puedes obtenerlo desde [docker.com](https://www.docker.com/get-started).
2. **Docker Compose**: Docker Compose debe estar instalado para gestionar los servicios. Si no lo tienes, sigue las instrucciones en [docker-compose](https://docs.docker.com/compose/install/).

## Cómo ejecutar el proyecto

Sigue estos pasos para levantar los servicios definidos en el archivo `docker-compose.yml`:

1. **Clona o descarga el repositorio**:

   Si no tienes el proyecto en tu máquina, clónalo usando Git:
    ```bash
   git clone https://github.com/SamScripts-DEV/APP-DOCKER.git
   cd APP-DOCKER
   ```
2.  **Levanta los servicios con Docker Compose**:
    
    Desde el directorio raíz del proyecto, ejecuta el siguiente comando para iniciar todos los contenedores:
    
    ```bash
    docker-compose up
    ```
    
    Este comando descargará las imágenes necesarias y configurará los contenedores para los siguientes servicios:
    
    -   3 contenedores web (`web1`, `web2`, `web3`) que ejecutan tu aplicación.
    -   Un balanceador de carga NGINX que distribuye el tráfico entre los servidores web.
    -   2 bases de datos MySQL (una maestra y una esclava).
    -   2 instancias de phpMyAdmin para gestionar las bases de datos maestra y esclava.
    -   Un servicio Locust para realizar pruebas de carga en el balanceador NGINX.
3.  **Accede a los servicios**:
    
    Una vez que Docker Compose haya levantado los contenedores, puedes acceder a los siguientes servicios:
    
    -   **Aplicación Web**:
        
        -   `web1` en [http://localhost:8001](http://localhost:8001/)
        -   `web2` en [http://localhost:8002](http://localhost:8002/)
        -   `web3` en [http://localhost:8003](http://localhost:8003/)
    -   **Balanceador de Carga NGINX**: [http://localhost](http://localhost/)
        
    -   **phpMyAdmin - Base de datos maestra**: [http://localhost:8081](http://localhost:8081/)
        
    -   **phpMyAdmin - Base de datos esclava**: [http://localhost:8082](http://localhost:8082/)
        
    -   **Locust para pruebas de carga**: [http://localhost:8089](http://localhost:8089/)
        
4.  **Detener los contenedores**:
    
    Para detener los contenedores, puedes usar el siguiente comando:
    
    ```bash
    docker-compose down
    ```
    

Este comando detiene y elimina todos los contenedores, pero preserva las imágenes y volúmenes definidos en `docker-compose.yml`.


