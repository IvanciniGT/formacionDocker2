# Para qué usamos los contenedores?

- entornos locales:                         docker, docker-compose, podman
        Para instalar mi entorno local
        Montarme un entorno de pruebas en local
- entornos de preproducción/pruebas/test    Integración continua
              certificación, previos
                INTEGRACION
        Para instalar el entorno de integración -> Se malea con el tiempo
            Que cada vez que haga una instalación para pruebas sea en un entorno limpio, partiendo de cero
                -> CONTENEDORES !!!
- entorno producción:                       kubernetes (k8s, k3s, tamzu, openshift)



DEV---->OPS:

Cultura/filosofía de la AUTOMATIZACION, quiero automatizar TODO lo que está 
entre el desarrollo y la opreción de sistemas.

    
    Integración continua:  Continuous integration                  CI
    
    Automatización del ciclo de desarrollo y despliegue de una app
    Mejora continua/detección de problemas
    
    Entrega Continua:         Continuous delivery                  CD
    Despliegue Continuo:      Continuous deployment                CD
    
Plan                            No es muy automatizable
Code                            Tampoco                                         ---> REPO SCM : GIT
Build                           SI automatizamos
                                    JAVA        maven , gradle , sbt
                                    PYTHON      poetry
                                    JS          npm, yarn webpack
                                    C#          msbuild, nuget
--------------------------------------------------------------------------------> Desarrollo agil
Test
    Diseño de la prueba         No es muy automatizable
    Ejecución de la prueba      SI es automatizable
        Estáticas: Las que no requieren poner en marcha el codigo para su comprobación
            Las pruebas de calidad de código: SonarQube
        Dinamicas: Las que SI requieren poner en marcha el codigo para su comprobación
            Funcionales
                Unitarias           JUNIT, TESTNG, MSTEST, UNITTEST
                                    Postman, SOAPUI
                Integración
                Sistema
                                    Selenium , Appium
                Aceptación
            No funcionales
                HA                  
                Rendimiento         JMeter, LoadRunner
                Estres
                UX
                Instalación:        smokeTest
--------------------------------------------------------------------------------> Entorno de pruebas / Integración
Si continuamente tengo la ultima versión que han hecho los desarrolladores del 
codigo en un entorno de integración sometido a pruebas automatizadas              Integración continua: Continuous integration
-------------------------------------------------------------------------------->
Release
    Automatizar la distribución de una release                                    ENTREGA CONTINUA
    Ser capaces de poner en manos de nuestro cliente de forma automatica la ultima version de nuestro proeycto
    Sin mediacion humana
-------------------------------------------------------------------------------->
Deploy
    Crear el propio entorno de producción que no lo está a priori:
        terraform
        vagrant
        ansible
        pupet
        chef
    Automatizar la instalación de aquello en un entorno de produccion             DESPLIEGUE CONTINUO
Operation
    Escalarlo, reiniciarlo, moverlo de un servidor a otro
    Configurar un balanceador de carga
        KUBERNETES
Monitorization
        KUBERNETES / Prometheus / Grafana / ElasticStack



Administrador de sistemas ----> Administrar Sistemas
                                Hacer o configurar programas que administren sistemas
            Ansible
            Puppet
            Chef
            Terraform
            Vagrant
      
--------------------------------------------------------------------------------
Metodologia en cascada -> 
    HITO 1   -> Fecha hay que tener unas funcionalidades implementadas

Metodologias agiles
    Sprint
        SPRINT 1 -> Fecha hay que tener unas funcionalidades implementadas
                    *****
                    10 Julio                 10 funcionalidades
                                              8 funcionalidades
                                              
    Pero, han venido con una serie de problemas inesperados....
        Antes la instalción la hacía al acabar el proyecto
        Las pruebas las hacia al acabar el proyecto
        
            Entrega 1           10% de la funcionalidad de mi sistema - Probar ese 10%
            Entrega 2           15%                                   - Probar el  15%
            
        La unica solución es AUTOMATIZAR <> DEVOPS
    
    Necesito una forma muy cómoda     de distribuir/instalar/ejecutar mi programa.... CONTENEDORES
                       estandarizada


Entorno de producción. Características:
-  Alta Disponibilidad.     Intentar garantizar que la app esté funcionando durante un determinado tiempo
                90% Tiempo de servicio: 100 dias 10 off... 36 dias año el sistema off           |   €
                99% Tiempo de servicio: 100 dias 1 off... 3,6 dias al año. Peluqueria de abajo  |   €€
                99,9%                 : 1000 dias 1 off... 8 horas al año.                      |   €€€€€€
                99,99%                : 10000 dias 1 off... minutos al año                      V   €€€€€€€€€€€€€€€€€
                100%
                            Intentar garantizar que no voy a perder información
        REDUNDANCIA/REPLICACION

-  Escalabilidad.           Adaptar la infra a las necesidades de cada momento
    
    App1:   PERFECTAMENTE NORMAL: Cualquier app departamental
        Dia 1       100 usuarios
        Dia 100      98 usuarios            NO HAY ESCALABILIDAD
        Dia 1000    102 usuarios

    App2:   PERFECTAMENTE NORMAL: Un app para un servicio que ofrezco a clientes.. cada vez tengo más clientes
        Dia 1       100 usuarios
        Dia 100     1000 usuarios           SI HAY ESCALABILIDAD            ESCALADO VERTICAL: MAS MAQUINA!!!!
        Dia 500     10000 usuarios 
    
    APP3:   ESTE ES EL MUNDO DE HOY EN DIA
        Dia n:      100 usuarios
        Dia n+1:    100000 usuarios         SI HAY ESCALADO                 ESCALADO HORIZONTAL
        Dia n+2:    2000 usuarios
        Dia n+3     2000000 usuarios
        
    Montamos un Cluster
                    2 maquinas
                    + 4 maquinas            ---> CLOUDs (automatizados)
                    - 3 maquinas
        Como instalo en la maquina nueva mi app??? Contenedor
        Despliego mi app                            Imagen de contenedor: Lleva ya mi app instalada
                                                    Es un zip cutre que descomprimo!
                                                    
                                                    
Entorno de producción
    Maquina 1 LE PETA LA FUENTE DE ALIMENTACION
        Contenedor MariaDB... imagen...
            Donde se guardan los datos de la BBDD??? Los quiero en el contenedor? NO, los perdería al borrar el contenedor
                Volumen -> CABINA
    Maquina 2: 8080-> tomcat
        Contenedor MariaDB... imagen...
            Y donde están los datos?
                Volumen -> CABINA
        Contenedor Tomcat app1
    Maquina N: 8080-> tomcat
        Contenedor Tomcat app1
    Datos en RED
        - NAS
        - iscsi
        - almacenamiento cloud
        - cabina de almacenamiento por fibra optica
        
        
    Cliente que le doy la IP de la maquina 1 o la IP de la maquina 2? Le doy las 2
        Esto es ruina... NECESITO UN BALANCEADOR DE CARGA
        
        
Para terminar de autoamtizar todo el trabajo necesito un orquestador de tareas...
    Servidor de automatización
    Servidor CI/CD
    
    Ejemplos: Jenkins, TravisCI, Bamboo, TeamCity, AzureDevops
    
Instalar un Jenkins < Contenedor < Docker in docker
    Ejecutando las tareas de los procesos de integración continua:
        Compila
        Empaqueta
        Prueba
        
        
        https://servidor
                        /job/basica/
                                    lastSuccessfulBuild/artifact/dockerfile/java/target/webapp.war
                        de la tarea BASICA 
                                    coge el ULTIMO BUILD VERDECITO
                                                        ARTEFACTO
                                                                DOCKERFILE/JAVA/TARGET/WEBAPP.WAR
                                                                
                                                                
App home banking
    Linea ouberta
        Firefox ultima, anterior, anterior de la anterior
            Windows 7 windows 8, windows 10, windows 100, macos, ubuntu desktop
            tablet android... que android ,...........
            ipad
            iphone
            telefono android
        Chrome
        Opera
        Edge
        Safari
        
Jenkins -> Sonarqube
    Analisis del codigo
    Plugin sonarqube + Dirección del sonarqube + credencial
    
Sonarqube hace el análisis de forma asincrona . cuando acaba llama a Jenkins, para decirle que ya lo tiene:
    Dirección del jenkins
    
Jenkins     http://172.31.14.171:8080
SonarQube   http://172.31.14.171:8081
squ_605ae06cd5a7437362d06ddbdb8c71e19be24a6d