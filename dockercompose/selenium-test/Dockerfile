#FROM python:latest     # Esta imagen a que apunta???
                       # Que contiene? Posiblemente la ultima version de python que haya disponible en un momento dado
                        # Hoy puede ser que apunte a la 3.9.13
                        # Y mañana???   3.9.14 o 3.10 o la 4.0.0
                       # De la version 3.9.13 -> 3.9.14  

FROM python:3.9        
                       # Esta imagen a que apunta???
                       # Que contiene? Posiblemente la ultima version de python que haya disponible en un momento dado
                        # Hoy puede ser que apunte a la 3.9.13
                        # Y mañana???   3.9.14 o 3.9.15

                        # MUY BUENA PRACTICA

#FROM python:3.9.13     # Esta imagen a que apunta???
                       # Que contiene? python 3.9.13

ARG SOURCE_PATH=.
ARG MAIN_PROGRAM

WORKDIR /app

COPY init.sh /
COPY $SOURCE_PATH .                
# Copiar en nuestro caso:
#       test.py
#       requirements.py

# Y si no hay requirements???
RUN [ -f "requirements.txt" ] && pip install --no-cache-dir -r requirements.txt || echo "No hay requirements.txt"
# Ejecuta durante el momento de crear la imagen un comando.... La imagen que salga, ya lleva esto configurado de serie

ENV MAIN_PROGRAM=$MAIN_PROGRAM
RUN mkdir /instantaneas
          
# Opcion 1
#CMD [ "/bin/sh", "-c", "python $MAIN_PROGRAM" ]
# Opcion 2
CMD [ "/init.sh"]
# Establece el comando por defecto que debe ejecutarse al arrancar un contenedor
# creado en el futuro desde esta imagen de contenedor que estamos generando

# NO NOS VA A FUNCIONAR NI DE COÑA !!!!!

# Aviso a navegantes !!!!
# Te puede interesar montar esa carpeta como un volumen
VOLUME [/instantaneas]
# Esto lo hacemos siempre!!!!
