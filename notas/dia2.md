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

# Sistema de archivos de un contenedor

1º Descargar imagen y descomprimir la imagen
2º Crear el contenedor < Se crea una carpeta asociada al contenedor





FS HOST
/
    etc/
    home/
    datos/      
        curso/curso.db
    bin/
    opt/
    tmp/
    var/        # Datos de programas
        lib/
            docker/     # Datos de docker
                    containers/
                            mimariadb/
                                            /etc/mariadb/mariadb.conf
                                            /var/mariadb
                            mimariadb2/
                    images/
                            mariadb-latest/   /               <<<< Carpeta base de la imagen del contenedor
                                            bin/
                                                lssh
                                                bash
                                                apt
                                            opt/
                                                mariadb
                                            var/
                                                mariadb< datos de tablas
                                            etc/
                                                mariadb/
                                                    mariadb.conf
                                            tmp/
                                            home/
                                            usr/
                                            
Si creo otro contenedor mariadb2                                            
El sistema de archivos de un contenedor se monta mediante la superposición de N capas:

CAPAS ADICIONALES:
    Volumen0    Ruta host   Ruta contenedor
                /datos      /var/mariadb

CAPA DEL CONTENEDOR:    Recoge todas las modificaciones que se hagan en el fs del contenedor
                        siempre que la ruta del archivo/carpeta que modifique no tenga su propio volumen
                            Borrados
                            Altas
                            Modificaciones
CAPA BASE:              Capa de la imagen del contenedor. Esta capa es inalterable
    





Si hacemos un chroot a la carpeta /var/lib/docker/images/nginx-latest ----> root para el runc
Si ejecuto con esa configuración un ls /... que me sale???



En linux tenemos un comando que permite engañar a un proceso, haciendole creer que el ROOT: /
    del sistema de archivos no es el root REAL, sino otra carpeta arbitraria:                   chroot
    

docker container create \
    --name mimariadb \
    --env MARIADB_USER=usuario \
    --env MARIADB_PASSWORD=password \
    -e MARIADB_ROOT_PASSWORD=password \
    -e MARIADB_DATABASE=curso \
    -p 0.0.0.0:3307:3306 \
    -v /home/ubuntu/environment/datos/mariadb:/var/lib/mysql \
    mariadb:latest

Montar un wordpress, que use de backend nuestra base de datos curso, y que esté expuesto en el puerto 8080 del host



mkdir -p /home/ubuntu/environment/datos/wordpress
chmod 777 /home/ubuntu/environment/datos/wordpress

docker container create \
    --name miwordpress \
    -e WORDPRESS_DB_HOST=172.17.0.1:3307 \
    -e WORDPRESS_DB_USER="usuario" \
    -e WORDPRESS_DB_PASSWORD=password \
    -e WORDPRESS_DB_NAME=curso \
    -v /home/ubuntu/environment/datos/wordpress:/var/www/html \
    -p 8080:80 \
    wordpress

# YAML

Es un lenguaje de marcado de información, equivalente a JSON, XML

GNU                 GNU is not Unix

YAML                YAML aint Markup Language
HTML
 XML
SGML

ML Lenguaje de marcado
<p>Esto es un parrafo</p>

Docker es una herramienta que controla los contenedores de UN HOST

Sirve docker para un cluster ? NO
Hay una herrameinta de docker "que se usa" para montar clusters de maquinas
que pueden ejecuatr conteendores: DOCKER SWARM
    NO LO USA NI EL TATO !!!!!!
Si quiero controlar un cluster de contenedores.... cual es la herramienta KUBERNETES
    USA EL TATO y TODA LA FAMILIA DEL TATO !!!!!!
