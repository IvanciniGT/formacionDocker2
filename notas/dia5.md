Contenedor
                        GUAY:   Permiten ejecutar procesos en un entorno aislado
                                Todo queda estandarizado
                                    Me aislo YO, como operador de un software, del software concreto que ejecuto
                                    Al darme igual lo que hay dentro y estar estandarizado, |
                                        puedo crear tareas de automatización genericas      | >>> KUBERNETES

docker engine           Limitación: es que trabaja contenedor a contenedor
                                    todo se pasa como argumentos de un comando shell
                        GUAY:       Queremos contenedores de un solo uso
                                    Operar contenedores:
                                        Listarlos
                                        Inspeccionarlos
                                        Borrarlos

docker-compose          GUAY:       Permite trabajar con múltiples contenedores a la vez
                                    Se guarda toda la información en un fichero YAML que va a un REPO de un SCM

dockerfile              Generar imagenes de contenedor
                        GUAY:
                            Muy simples (10-12 palabras)
                            Podiamos crear imagenes a traves de un proceso Multistage 
                                (usando distinitas imagenes de contenedor para distintas tareas)
                                
Analizar distintos usos que damos a los contenedores:

- Montar programas en entornos locales
- Ejecutar comandos en entornos locales
    - Maven
    - Python
    - Ansible-playbook
    - Terraform
- Montar procesos de despliegue de apps en local
- Distribuir apps / Imagen

- Entornos de preproducción: Servidores de automatización (Jenkins)
    - Pipelines: Ejecutan tareas -> Contenedor

- Entorno de producción



---

Hoy en dia el grueso de las app son:
- Servicios web en backend <> RESTful (JSON)

- Frontales web (que atacan a esos servicios por detrás) - Angular, React, Vue, LitElement, Polymer
    - Selenium
- Frontales moviles (que atacan a esos servicios por detrás)
    - Appium


Python es un lenguaje de programación:
    Compilado o interpretado?
    Interpretado -> Un programa escrito en python requiere un interprete instalado 
                    en la maquina host para poder ser ejecutado
                    cython, pypy, jython
                    
Las versiones de un software siguen un determinado esquema:
    3.9.13
    3  = mayor  -> Cambio drastico en el código que puede romper con compatibilidad
    9  = minor  -> ampliar funcionalidad
    13 = micro  -> bugs
    
    
----
Nosotros creamos una imagen con: docker build 
                                 docker-compose build
Al crear la imagen se crean contenedores temporales
Y en ellos ejecutamos comandos
    En esos contenedores temporales, tenemos disponibles las variables definidas con la palabra ARG

Y como resultado de este proceso se obtiene UNA IMAGEN DE CONTENEDOR
---
Desde esa imagen de contenedor nosotros generamos CONTENEDORES, ya para trabajar.
    En esos conteendores también puedo tener variables: En este caso VARIABLES DE ENTORNO, definidas con la palabra ENV
---

Si quiero distribuir el poder crear una imagen de contenedor que ejecute dentro programas de selenium...
Que distribuyo? Dockerfile (+docker-compose... paraque lo puedan probar) -> repo git
                Esto permitiria a terceros crear sus propias imagenes de contenedor que:
                            - ejecutar localmente
                            - dueran distribuidas a través de un registry de repos de imagenes de contenedor
Si quiero distribuir mi propio programa:
    La imagen que he generado yo localmente, la subo a un registry de repos de imagenes de contenedor
    Y que la gente la use
    
---

Markdown: formato para escribir documentación.
Estos ficheros son procesados por programas que generan HTML
    
    
--- 

Kubernetes: orquestador de contenedores

Gestor de gestores de contenedores

Esto esta pensado para entornos de producción.

Dentro de un kubernetes hablamos de:
    Balanceadores de carga
    Escaladores
    Volumenes persistentes en red
    Clusters

No obstante, existe: 
    minikube

k8s - Kubernetes de producción OpenSource que montamos habitualmante
minikube - Para jugar en entornos locales
k3s - distro de kubernetes muy ligera. (sofware emebido)
openshift - Redhat
tamzu VMWare

No configuramos contenedores 
Se trabaja con PODS..... podman
Un pod es un conjunto de contenedores

Cluster de maquinas gestionado por Kubernetes
    Maquina 1
        Container.d CRIO
    Maquina 2
        Container.d CRIO Docker
        Pod
            Contenedor: nginx (desde una imagen)
    Maquina 3
        Container.d CRIO
        
Tu, a kubernetes le pides que quieres tener un POD desplegado dentro del cluster
POD: Conjunto de contenedores.

