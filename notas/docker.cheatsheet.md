docker [TIPO DE OBJETO] [VERBO] <args>

TIPOS DE OBJETO:        VERBO:
    - image             pull    list    rm      push    inspect
    - container         create  rm      list    start   stop      restart   logs    exec    inspect
    - volume
    - network
    - secret

** Nota: casi todos los comandos de docker tienen un alias, que s más cortito y más cómodo de utilizar

# Gestión de imágenes de contenedor

## Consultar las imágenes de contenedor que tengo descargadas / presentes en mi host

$ docker image list                                         $ docker images
        Args:
            -q

## Borra imagen de contenedor

$ docker image rm <ID DE LA IMAGEN>                         $ docker rmi <ID DE LA IMAGEN>

## Descargar imagenes de contenedor

$ docker image pull <QUE IMAGEN QUIERO DESCARGAR>           $ docker pull <QUE IMAGEN QUIERO DESCARGAR>
    <QUE IMAGEN QUIERO DESCARGAR>:
        registry/repo:tag
    Los gestores de contenedores (como docker) tienen configurado una serir de registries por defecto
    En el caso de docker es docker hub (puedo cmabiarlo)
    
    nginx: Proxy reverso + funcionalidades de servidor web
    httpd: Servidor web + funcionaldiades de proxy reverso
    
        El targ por defecto que se usa si no especifico tag es :latest
    
    latest es un tag más... no es ninguna palabra especial para docker.
    Quiero decir: Si pongo latest no significa que se busque la última que se haya subido...
    Sino la imagen que se haya subido con el tag latest
        De hecho, el usar el tag latest esta considerado una MALA PRACTICA.. pa' jugar nos vale... pa' na más

## Inspeccionar(ver el detalle) de una imagen de contenedor (ver la configuración adicional que viene con la imagen)

$ docker image inspect <NOMBRE-DE-LA-IMAGEN>

# Contenedores

## Listar contenedores:

$ docker container list                             $ docker ps
    Este comando muestra solamente los contenedores en ejecución
    Si quiero verlos todos: --all

## Creación de contenedores:

$ docker container create <ARGS> <IMAGEN-DE-PARTIDA> <COMANDO-A-EJECUTAR>
    Esto realemnte solo está creando una triste carpeta en nuestro filesystem del host
    ARGS:
        --name NOMBRE
        -p     IPHOST:PuertoHOST:PuertoContenedor                   Hacer un nateo (redirección de puertos)
                IPHOST por defecto vale 0.0.0.0 = Todas las IPs del host
        -e VARIABLE=valor   Permite inyectar variables de entorno a un contenedor
    
## Arrancar un contenedor

$ docker container start <NOMBRE-DEL-CONTENEDOR>       $ docker start <NOMBRE-DEL-CONTENEDOR> 

## Parar un contenedor

$ docker container stop <NOMBRE-DEL-CONTENEDOR>       $ docker stop <NOMBRE-DEL-CONTENEDOR> 

## Borrado de contenedores:

$ docker container rm <NOMBRE>                          $ docker rm <NOMBRE>
        -f      Fuerza el borrado aunque esté corriendo el contenedor

## Obtener información del contenedor

$ docker container inspect <NOMBRE-DEL-CONTENEDOR>      $ docker inspect <NOMBRE-DEL-CONTENEDOR>

## Ejecutar procesos dentro de un contenedor

$ docker exec <NOMBRE-DEL-CONTENEDOR> <COMANDO-QUE-QUIERO-EJECUTAR>

## Ver los logs de un contenedor

$ docker logs <NOMBRE_CONTENEDOR>
