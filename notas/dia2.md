# Qué es un contenedor?

Es un entorno aislado dentro de un SO Linux donde ejecutar procesos.

UN CONTENEDOR NO TIENE DENTRO UN SISTEMA OPERATIVO - GRAN DIFERENCIA CON RESPECTO A LAS MAQUINAS VIRTUALES

Al trabajar con contenedor solo hay 1 unico sistema operativo, el del host: del que se utilzia el kernel.

Aislado???
- Su propia configuración de red -> Su propia IP
        En qué red? En una red virtual creada por docker... que por defecto opera en el tramo de red: 172.17.0.0/16
- Su propio sistema de archivos
- Puede tener limitación de acceso a los recursos HW del host
- Tiene sus propias variables de entorno

Los contenedores se crean basados en una IMAGEN DE CONTENEDOR

Imagen de contenedor???

Un fichero comprimido que tiene dentro: 
- Un sistema de archivos compatible con POSIX
- Una serie de programas ya instalados y configurados

+ unas configuraciones para los contenedores que se creen desde esa imagen:
    + Comando por defecto que debe ejecutar dentro de un contenedor creado desde una imagen al hacer un start

Donde se guardan? En un repo de un registry de repos de imagenes de contenedor
Cada imagen se identifica mediante:
    registry/repo:tag
        artefactos.iochannel.tech/ivancinigt/iochannel-ssh-container:latest
        mariadb:latest
    El registry, nuestro gestor de contenedores tiene uno configurado por defecto.

Con qué herramienta trabajamos? docker engine

Otras: containerd, podman, crio

Al trabajar con docker engine:
- dockerd (gestionado por systemd < systemctl)
- docker:
    $ docker [TIPO_OBJETO] [VERBO] <args>

Tipos de objeto:    Verbos
- Image             pull    push    list    rm      inspect
- Container         create  rm      list    inspect logs    exec    start   stop
- Volume
- Network
- Secret

run < Para ejemplos de libro... o para ejecutar contnedores de un uso y que estén ejecutando algo que acabe:
    image pull
    container create
    container start
    container attach
    container rm

docker container create --name minginx -p 8081:80 nginx

    -p 8081:80
        -p 0.0.0.0:8081:80
           -------
           IPs donde hacer la redirección de puertos
                   ----
                   Puerto del host que atenderá peticiones
                        Puerto del contenedor al que se redirige el trafico

Para qué me dirve el nombre de un contenedor:
    Para arrancarlo
    Para ver los logs
    Para inspeccioanrlo
    Para pararlo
    Para borrarlo

pondremos siempre un nombre de contenedor?  Podré no ponerlo (y no lo pondré) cuando:
    - No vaya a arrancarlo yo
    - No vaya a pararlo yo
    - No vaya a borrarlo yo
    - No vaya a inspeccioanrlo yo
    - No vaya a solicitar sus logs yo

Cuando vaya a crear un contenedor para ejecutar un comando, que arranca y para.

# IMAGEN BASE DE CONTENEDOR

Es una imagen que me proporciona:
- La estructura de carpetas POSIX
- Comandos básicos para ponerar en un entorno linux: ls, mkdir, chmod, clear, sh

ALPINE: No lleva casi comandos... los más básicos. 2,5 Mbs
UBUNTU/DEBIAN: Lleva algunos comandos más: apt, bash
CentOS. Fedora: Lleva algunos comandos más: yum, dnf, bash

Son imágenes desde la que yo contruir mis propias imagenes de contenedor.


En POSIX cualquier proceso acaba devolviendo un codigo de respuesta:
- 0                             Todo ha ido bien
- Otro numero mayor que cero    Algún fallo

TRUCOS PARA MANETNER UN CONTENEDOR CORRIENDO:
    sleep 3600
    tail -f /dev/null

QUIERO :
Un mariadb
con una bbdd llamada curso
usuario: usuario
contraseña del usuario y root: password

docker container create \
    --name mimariadb \
    --env MARIADB_USER=usuario \
    --env MARIADB_PASSWORD=password \
    -e MARIADB_ROOT_PASSWORD=password \
    -e MARIADB_DATABASE=curso \
    -p 0.0.0.0:3307:3306 \
    mariadb:latest

Puerto mariadb=mysql=3306


docker exec -it mimariadb bash
    mysql -u usuario -p 
        use curso
        create table PRUEBA (ID INT, TEXTO VARCHAR(50));
        select * from PRUEBA;
        
Sigue estando la tabla alli dentro?
    SI I

El sistema de archivos de un contenedor es persistente?
    Es una pregunta con respuesta compleja.
    Respuesta corta: SI, es persistente... mientras no borre el contenedor
    
Vamos a borrar un contenedor una vez creado con frecuencia?
Si me creo un contenedor con mariadb, y le cargo datos... lo querré borrar con frecuencia?
DE CONTINUO!

!!!VOLUMENES!!!
