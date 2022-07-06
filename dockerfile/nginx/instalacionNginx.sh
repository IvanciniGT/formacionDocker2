
# Alta de los repos de nginx oficiales
echo "deb https://nginx.org/packages/ubuntu/ bionic nginx" > /etc/apt/sources.list.d/nginx.list
echo "deb-src https://nginx.org/packages/ubuntu/ bionic nginx" >> /etc/apt/sources.list.d/nginx.list 
# Descarga de la clave doficial de la gente de nginx
wget http://nginx.org/keys/nginx_signing.key
# Alta la clave de nginx... para que no pete apt cuando descarge paquetes de esos repos
apt-key add nginx_signing.key
# Que apt se conecte con todos los respo (nos interesa basicamente el nuevo) para que sea consciente 
# de los paquetes que hay ahi y pueda localizarlos cuando le pida que los instale
apt update
# Instala el paquete nginx, sin preguntar, NADA !!!
apt install nginx -y
