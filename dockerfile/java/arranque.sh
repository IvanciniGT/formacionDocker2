#!/bin/sh
echo "CAMBIAMOS EL PUERTECITO DEL TOMCAT !!!!!!!"
sed -i "s/port=\"8080\"/port=\"${PUERTO_TOMCAT}\"/g" /opt/bitnami/tomcat/conf/server.xml

echo "YA ESTA. ARRANCO EL TOMCAT !!!!!!!"
/opt/bitnami/scripts/tomcat/run.sh