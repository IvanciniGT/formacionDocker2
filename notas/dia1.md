# Contenedor

Es un entorno aislado dentro de un SO Linux (kernel de Linux) donde ejecutar procesos.
Entorno aislado en cuanto a qué:
- Su propia configuración de red: Su propia IP
- Su propio Sistema de Archivos (FileSystem)
- Limitación de acceso a los recursos Hardware del hierro: memoria / CPU / IO
- Sus propias variables de entorno

Los contendores los creamos desde una imagen de contenedor.


# Contenedorización:

Una tecnología / forma (nueva? formalmente desde el 2013... lleva desde muuuuchos años antes)
                                                    VVVV
                                                    Docker Inc.
de empaquetar, distribuir, instalar y ejecutar Software en computadoras Linux, que está estandarizada.

Independientement del software que corra dentro de un contenedor, yo siempre lo opero de la misma forma:
- Arranco
- Paro
- Reinicio
- Veo sus logs
- Instalo
- Desinstalo
                                                               
                                                               
## Imágen de contenedor

Un triste fichero comprimido (tar), que contiene una estructura de carpetas compatible con la 
especificación POSIX, en las cuales ya se encuentra INSTALADO un(os) programa(s) y configurado(s).
                         Open Container Initiative (Docker Inc.)
Además una imagen de contenedor lleva consigo una serie de configuraciones:
    - El proceso que se tiene que levantar al iniciar un contenedor basado en esta imagen: CMD Command
    - Variables de entorno
    - Que volumenes sería conveniente montar
    - Que puertos se exponen

A cambiado el mundo de las tecnologías de la información... y ha salpicado a todos los perfiles del mundo IT:
- desarrolladores
- tester
- sysadmins

Las imágenes de contenedor se guardan en un repositorios... que los ubicamos dentro de un registry.

Cuál es el registry de repos de imagenes de contenedores?
- docker hub
- quay.io       Redhat
- nexus, artifactory  -> on premise    
- gitlab


√ Una foto de un contenedor

### Quiero instalar mariaDB en mi computador windows. Qué necesito?

1- Descargo de internet un instalador
2- Ejecuto el instalador -> Instalación de MariaDB
3- Configuro el MariaDB

La carpeta o carpetas resultantes de la instalación -> ZIP -> email -> descomprimís en las mismas ubicaciones.

Funciona? Con mucha probabilidad NO.

## Linux

Linux es un SO? NO
Linux es un kernel de SO

## Unix®

Qué es Unix®?  Una especificación (de hecho 2: POSIX, SUS) acerca de cómo montar un SO.
Qué era Unix®? Un SO creado por los lab Bell de AT&T allá por los 70-80. Has principios de los 2000.

Oracle: Solaris    UNIX®    
HP:     HP-Ux      UNIX®    |
IBM:    AIX        UNIX®    |   Kernel SO Unix
Apple:  MacOS      UNIX®

BSD386: Tenemos por fin un SO Unix® gratuito
    netBSD
    freeBSD
    MacOS

GNU:    GNU is Not Unix
        ~~kernel~~                          dos > nt
        librerias/compiladoreS: gcc make    
        shell: cli: bsh, bash               cmd ps1
               ui:  gnome                   fluent design
        editores de texto: gedit            bloc de notas
        juegos: chess                       buscaminas
        
Linus Torvalds: Linus' Unix -> Linux

GNU/Linux < SO completo
75%  25%
    Distribuciones de SO GNU/Linux:
        Redhat: RHEL, Fedora, CentOS, Oracle Unbreackeable linux
        Debian: Ubuntu
        Suse
        
Kernel de SO más usado en el mundo? Linux

SO linux -> Android (kernel Linux) + librerias Google

# Configuración de red

## Interfaz de red?

Conexión lógica (con su configuración correspondiente) a una red < SO
NIC? Network Interface Card: tarjeta física de red

1 interfaz de red - 1 nic
1 interfaz de red - 0 nics
2 interfaces de red - n nics

Cuantas interfaces de red tiene una computadora?
- eth - Ethernet - IP: 172.0.0.0/8 
                       192.168.0.0/16
- loopback - 127.0.0.0/24
             127.0.0.1 - localhost... there is no place like 127.0.0.1

# Sistema de Archivos POSIX
/
    bin/        Comandos / binarios ejecutables
    dev/
    etc/        Configruaciones
    home/       Usuarios
    tmp/        Temporal
    root/       Carpeta del usuario root
    usr/
    var/        Datos de programas
    opt/        Programas
    sbin/

# Tipos de software:

- Sistema operativo
- Aplicaciones          Software con ejecución indefida en el tiempo y en primer
                        plano pensado para interactuar con humanos
                          Word, Chrome, photoshop
-----------------------------------------------------VVV de aqui para abajo en contenedores
- Driver
- Demonios              Software con ejecución indefida en el tiempo y en segundo
                        plano.
    - Servicio          Pensados para interactuar con otros procesos /programas
                            Servidor BBDD: mysql, mariadb, postgresql, mongo
                            Servidor web: httpd, nginx
                            Servidor de apps: tomcat, weblogic, liberty, jboss, wildfly
- Comando               Software que se ejecuta haciendo una tarea concreate y acaba
                            ls, pwd, uname
- Script                Software que ejecuta una serie (secuencia) de tareas y acaba

Puedo poner un SO dentro de un contenedor linux???? NI DE COÑA !!!!!!!!!!!!

# Cómo instalamos y ejecutamos procesos dentro de computadoras

## Modelo más tradicional:

     App1 + App2 + App3         Problemas: 
    ---------------------           Incompatibilidad en las configuraciones / dependencias
             SO                     Actualizaciones de SO
    ---------------------           App1 se vuelve loca (100% CPU)-> App1 se va pa' cuenca
           HIERRO                           App2 y App3 van detrás
                                    Problemas de seguridad

## Modelo basado en Máquinas Virtuales:

     App1   | App2 + App3           Problemas:
    ---------------------               Mantenimiento y configuración se vuelven más complejos
     SO 1   |     SO 2                  Arquitectura es mucho más compleja
    ---------------------               Desperdicio de recurso
     MV 1   |     MV 2                  Merma en el rendimiento
    ---------------------   
        Hipervisor: 
    vmware, hyperV, virtualBox
    citrix, kvm
    ---------------------           
             SO             
    ---------------------   
           HIERRO           

## Modelo basado en contendores

     App1   | App2 + App3           
    ---------------------           
     C 1    |     C 2               
    ---------------------   
    Gestor de contenedores:
      docker, containerd,
         podman, crio
    ---------------------           
          SO Linux            
    ---------------------   
    HIERRO  (real o virtual)
    
# Docker Inc

Tiene muchos productos de software:
    - docker engine <<<< Este es el habitual
    - docker desktop (4mac & windows)
    - docker hub
    - docker-compose
    - docekr-swarm
    
# Servicios en una maquina linux:

Init Scripts ->  rc.0 rc-1 < Spec Unix SystemV - SysV
Systemd      -> lleva gestión de servicios, puntos de montaje
    ^^^
    systemctl
    

dockerd -> Demonio de docker
    ^^^^
    docker  -> cliente de docker < docker-compose
    

dockerd
    generar imágenes de contenedor propias
    subir imágenes de contenedor a un registry
    containerd 
        Crear contenedors
        Borrar contenedors
        Controlar la ejecución de un contenedor
            Correr un contenedor -> runc
        Descargar imágenes de contenedores de un registry
        
# Acciones        

docker pull nginx:                                  Descargar una imagen de contenedor (latest) 
                                                        + Descomprimir el tar en algún sitio
docker container create --name minginx nginx        Crear una carpeta para el contendor
                                                    Crear un entorno aislado dentro del SO Linux del host

docker container start minginx                      A través de runc poner en funcionamiento el contenedor
                                                        + Ha puesto a correr dentro del entorno aislado los procesos
                                                          que se hayan definido en la imagen de contenedor
## JSON: JS Object Notation

Lenguaje de marcado de información. 

[] -> Lista de objetos (array)
{} -> Mapa/diccionario/array asociativo/hashmap.   Conjunto de claves / valor

# Lenguajes informáticos:

- Lenguajes de programación: JAVA, C, JS, Python, C#
- Lenguajes de marcado de información: Proposito general (JSON, XML, YAML), Proposito especifico (HTML)
- Lenguajes de consulta a BBDD: SQL
- Lenguajes de modelado: UML
 
# Sha, md5

Hash - Que es un algoritmo de hash? Un algoritmo de HUELLA !!!!
Letra del DNI: algoritmo de huella: Comprobar la validez del número

19237348 / 23 -> División entera (sin decimales) RESTO

2300001 / 23 -> RESTO = 1 .... Los restos están entre : 0-22

## Servidor web:

80: http     nginx 
443: https

curl http://localhost:80
curl localhost


                                    Red de amazon
 ------------------------------------------------------------------------------------------
 |                                                                      |
172.31.14.171  NAT 8081 -> C1:80                                    172.31.14.200
 |                                                                      |
Host    IvanPC - curl 172.17.0.2                                       Host RamotxuPC
 |          |
172.17.0.1  |---loopback (127.0.0.1)
 |
 |- 172.17.0.2:80 - Contenedor nginx
 |
 | red de docker (red virtual
 |  que existe solo en mi host)
    A este red están pinchados los contenedores
    y el host

Docker no es una herramienta que usemos nunca en un entorno de producción.
Docker permite gestionar contenedores en mi(una) maquina  -> Esto vale para un entorno de producción: NO!!!!
Cuando nos vamos a un entorno de producción, SI SEGUIMOS TRABAJANDO CON CONTENEDORES, pero usando otras herramientas:
    kubernetes (k8s, k3s, tamzu, openshift)
    Es un gestor de gestores de contenedores
    Tengo una granja de maquinas, cada una con un gestor de contenedores (tipo docker ---- containerd o crio)
        Monto kubernetes para controlar todos esos gestores de contenedores de forma centralizada

Que características tiene un entorno de producción que no tienen otros entornos?
- Alta disponibilidad:      Intentar garantizar un determinado tiempo de servicio o la no pérdida de información
                                90% de tiempo de servicio     100 dias, el servicio puede estar caido 10...             |   €
                                                              36 dias al año???                                         |   €€
                                99% de tiempo de servicio     Peluqueria (WEB) 1 de cada 100 down. 3,6 dias al año off  |   €€€€
                                99,9 de tiempo de servicio    1000 dias 1 off... 8 horas al año...                      |   €€€€€€€€€€€€
                                99,99                         10000 dias 1 al año... minutos al año < MAS RAZONABLE     v   €€€€€€€€€€€€€€€€€€€€€€€€€€€€
- Escalabilidad:            Adaptar la infraestructura a las necesidades de cada momento
- Seguridad

REDUNDANCIA:            Cluster - group
    - La app instalada en varios servidores fisicos
    - Los datos guardados en varios HDD independientes (RAID)

App1... cuyo modelo de uso es:          COMPLETAMENTE NORMAL: App departamental o interna de una empresa
    Dia 1           1000 personas
    Dia 100         1005 personas       Aquí no hay problemas de escalabilidad
    Dia 1000         997 personas

App2... cuyo modelo de uso es:         COMPLETAMENTE NORMAL: un app de un servicio que ofrezco a unos clientes... cada vez tengo más clientes
    Dia 1           1000 personas
    Dia 100         10000 personas      Aquí que pasa con la escalabilidad? Crecimiento constante       ESCALAMIENTO VERTICAL: Más maquina
    Dia 1000        100000 personas

App3... cuyo modelo de uso es:          ES DIA DE HOY: INTERNET(WEB)
    Dia n           100 personas
    Dia n+1         100000 personas     Black friday            Aquí que pasa con la escalabilidad      ESCALAMIENTO HORIZONTAL: Más maquinas
    Dia n+2         200 personas
    Dia n+3         2000000 personas    Ciber monday



Desarrollo JAVA, JS, PYTHON
        (la creamos con un dockerfile)
    -> Imagen de contenedor -> Registry de repos de imagenes de contenedor
                                    ^
                                Kubernetes
                                
    Necesito probar esa imagen de contenedor... y necesito herramientas auxiliares para que la pruebe... BBDD < Contenedor
                    ^^^^^^                                                                                       ^
                    Contenedor  <------------------------------------------------------------------------------- docker (docker-compose)

