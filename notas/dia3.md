# Cuándo me interesa montar mis propias imágenes de contenedor

- Para distribuir mi SOFTWARE

- Cuando monto un entorno local de desarrollo. 
    - Para que todos trabajen con lo mismo
    - Para ahorrar tiempo en las configuraciones

- Cuando quiero trabajar con una herramienta que no tiene imagen de contenedor 

# Creación de una imagen de contenedor

Partimos de una imagen base (al menos 1):
- Base... base: pela' 
    - Ubuntu
    - Fedora
    - Debian
    - Alpine
- Base que ya traiga algún software: Servidor web, servidor de apps

Vamos a usar unos ficheros llamados Dockerfile (10, 12 palabras + montonones de código bash)

Al crear una imagen de contenedor lo que hace Docker:
- Crear un contenedor temporal desde la imagen BASE
- En ese contenedor va haciendo cosas:
    - Copiarle archivos
    - Ejecutar comandos
- Plancha el contenedor -> Lo mete en un tar ... y ya tengo mi imagen

Sobre las imagenes base:                                                                FROM
- Copiar ficheros del host a la nueva imagen de contenedor que se está generando        COPY    
- Ejecución de comandos dentro de esa "imagen de contenedor" que se está generando      RUN
- Además tenemos que dar algo de información... para la pobre personita que viene detrás y que lo va a usar:
    - Que volumenes debería montar... (En que carpetas mi programa está guardando información que se debería persistir)
                                                                                        VOLUME  
    - Las variables de entorno:                                                         ENV
        - Darles un valor por defecto
        - Informar de las variables que se pueden usar
    - Puertos que se pueden exponer (NAT)... donde mi app sirve                         EXPOSE
- Otra serie de información... no para el tio que viene detrás ... sino para docker
  para cuando cree un contenedor desde esta imagen:
    - Comando que se debe ejecuatr al arrancar el contenedor                            CMD
    - Donde se debe ejecuatr ese comando                                                WORKDIR
    - Usuario con el que debe correr el proceso.                                        USER
        - Una mala practica es usar el usuario ROOT

Vamos a empezar montando una imagen de contenedor que lleve un nginx funcionado, partiendo de una imagen UBUNTU
    Ahi vienen las carpetas posix + 4 comandos basicos de la shell + apt
    
    

---

Que hemos hecho:

Crear una imagen de contenedor a medida... Para qué?

Para distribuir mi app...Soy el desarroollador de nginx.

Yo, qué se un huevo de nginx, por que soy el tio que lo desarrolla, he montado una imagen con una instalación de nginx.
Y esa imagen ahora la puedo distribuir, para que la gente pueda usar mi app (qué es nginx)

Además, me he creado un docker-compose, pa' qué?
Para probar la imagen de contenedor
---
Un servidor web: Recibe peticiones a través de un puerto en un determinado protocolo: http
http -> URL
    protocolo :// servidor (IP,fqdn) : puerto    contexto
    
    http      :// localhost          : 8080      /  
                                                 ^
                                                 Que ruta es esta ???? ROOT

Cuando montamos un servidor web, configuramos dentro de él: Virtual-hosts:
    Abro un puerto en el que escucho peticiones por http
    Y me quedo con la parte del contexto
    en el servidor web hacemos un cambio. / -> Lo que haya configurado en una propiedad DOCUMENT_ROOT
                                                                                        /usr/share/nginx/html
    /usr/share/nginx/html/ruta

---




Ahora no soy el desarrollador de nginx
Soy el desarrollador de un sitio web (frontend), 

que contiene mi proyecto?
carpetas con ficheros: html + js (react, angular, vue) + imagenes, css

donde acaba mi proyecto? es decir, todos esos ficheros????
En un repo de git (en general de cualquier SCM), en concreto será un git

Quiero poner en funcionamiento(instalar) mi página web -> Qué hago????
Tengo que copiar todos esos archivos donde??? en un servidor web, en su document root
    Servidores web: apache httpd, nginx, iis
    
cual sería mi distribuible siguiendo un modelo más tradicional?
Un triste ZIP para que ellos lo descompriman en un servidor web, que ellos hayan instalado y configurado.

Que o cómo podría facilitar a la gente que usen mi web?
Dandole el servidor web instalado y configurado con MI APP DENTRO !!!!!!

como le podría hacer llegar esto? En una imagen de contenedor









----

Somos un desarrollador de una web 
Pero estamos haciendo la parte de backend

JAVA
Tener jdk para compilar el codigo
Cuando compilamos codigo JAVA, solemos usar herramientas que nos ayudan en ese 
    proceso /empaquetado, gestion de dependecias: maven -> Archivo empaquetado .jar .war .ear
    
Para ejecutar una app web java necesitamos JVM + Servidor de apps JAVA: tomcat, weblogic, liberty / websphere, jboss

El codigo lo tendre en un repo.... de git





