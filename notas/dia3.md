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

VAmos a empezar montando una imagen de contenedor que lleve un nginx funcionado, partiendo de una imagen UBUNTU
    Ahi vienen las carpetas posix + 4 comandos basicos de la shell + apt