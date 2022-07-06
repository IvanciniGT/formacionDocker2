# Instalamos ubuntu 20.04
FROM ubuntu:focal   
# Es el por defecto.. no me hace falta... Como lo se??? Me conozco la imagen
# USER root
RUN apt update && apt install wget gnupg -y
# Alta de los repos de nginx oficiales
RUN echo "deb https://nginx.org/packages/ubuntu/ focal nginx" > /etc/apt/sources.list.d/nginx.list
RUN echo "deb-src https://nginx.org/packages/ubuntu/ focal nginx" >> /etc/apt/sources.list.d/nginx.list 
# Descarga de la clave doficial de la gente de nginx
RUN wget http://nginx.org/keys/nginx_signing.key
# Alta la clave de nginx... para que no pete apt cuando descarge paquetes de esos repos
RUN apt-key add nginx_signing.key
# Que apt se conecte con todos los respo (nos interesa basicamente el nuevo) para que sea consciente 
# de los paquetes que hay ahi y pueda localizarlos cuando le pida que los instale
RUN apt update
# Instala el paquete nginx, sin preguntar, NADA !!!
RUN apt install nginx -y
# Avisos a navegantes...
# Informo a las personas que vayan a usar esta imagen de los puertos donde esto funciona y las carpetas 
# con información relevante que podrían requerir persistencia
EXPOSE 80
VOLUME [/usr/share/nginx/html]
# Configuración de los contenedores que se generen en el futuro
CMD ["nginx", "-g", "daemon off;"]
