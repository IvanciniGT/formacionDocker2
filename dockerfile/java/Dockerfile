# REPO DE GIT
# Descargar el codigo.                                  git
# Compilar/empaquetar                                   maven + java
# Instalar la app resultante (WAR) en un tomcat         tomcat


FROM bitnami/git AS clonador
ARG REPO_APP
RUN git clone $REPO_APP /miweb

FROM maven:3.8-openjdk-8 AS empaquetador
COPY --from=clonador /miweb/ /miweb/
WORKDIR /miweb
RUN mvn package

FROM bitnami/tomcat:9.0.64

# Quiero remplazar en el fichero: /opt/bitnami/tomcat/conf/server.xml
# El texto: port="8080"
# Por el texto: port="PUERTO_TOMCAT"
#ARG PUERTO_TOMCAT=8080
#RUN sed -i "s/port=\"8080\"/port=\"${PUERTO_TOMCAT}\"/g" /opt/bitnami/tomcat/conf/server.xml        
COPY --from=empaquetador /miweb/target/webapp.war /app/
ENV ALLOW_EMPTY_PASSWORD=yes

LABEL maintainers="Ivan Osuna Ayuste <iam@ivan.com>"
LABEL license="MIT"
LABEL home="http://miwebapp.com"

COPY ./arranque.sh /opt/bitnami/scripts/tomcat/arranque.sh
#RUN chmod +x /opt/bitnami/scripts/tomcat/arranque.sh

ENV PUERTO_TOMCAT=8080
CMD ["/opt/bitnami/scripts/tomcat/arranque.sh"]
