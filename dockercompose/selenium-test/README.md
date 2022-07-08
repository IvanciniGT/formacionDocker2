# Generación de gráficos: MERMAID-JS

# Imágenes

![Texto alternativo en caso de error](https://www.jenkins.io/images/logos/baturro/baturro.png)

# Enlaces

https://www.google.es/

<https://www.google.es/>

[Yo puedo poner el texto de enlace que quiera](https://www.google.es/)

# Listas 

## Listas no numeradas (desordenadas)

- Item 1
  * otro
  * otro
- Item 2
  + subitem A
  + subitem B
- Item 3
  -  Subitem 1
  -  Subitem 2

## Listas numeradas:

1. Item 1
1. Item 2\
   Si quiero que un item tenga varios párrafos.. 

   Os imaginais lo que hago
1. Item 3
   1) Item 1
   2) Item 2
   3) Item 3
1. Volvemos 

# Bloques de codigo

```py
def test1(self):
    driver = self.driver
    driver.get("http://172.31.14.171:8082/webapp/")
    time.sleep(3)
    #---
    texto=driver.find_element(By.XPATH,"//h2").text
    #---
    self.assertEquals("Hola Jenkins!",texto)
    
    driver.get("https://phoenixnap.com/kb/install-docker-compose-ubuntu")
    driver.save_screenshot("/instantaneas/screenshot.png")

```

# Estilos de texto

## Codigo en linea

Vease la variable `MAIN_PROGRAM`, que permite elegir el programa que debe ejecuatrse en el contenedor.

## Tachado

Este teto aparece ~~tachado~~

## Enfasis (cursiva)

Un texto en enfasis se mete entre *asteriscos*.
También sirven guines bajos... pero no se usa mucho: _no es buena práctica_.

## Enfasis mayor (negrita)

Un texto en enfasis se mete entre **asteriscos**.
También sirven guines bajos... pero no se usa mucho: __no es buena práctica__.

## Super enfasis

Un texto en enfasis se mete entre ***asteriscos***.
También sirven guines bajos... pero no se usa mucho: ___no es buena práctica___.



Titulo de nivel 1. No se usa mucho
==================================

Titulo de nivel 2. No se usa mucho
---

# Titulo de nivel 1 #######################################################

## Titulo de nivel 2

### Titulo de nivel 3

#### Titulo de nivel 4

##### Titulo de nivel 5 ##################################################

###### Titulo de nivel 6

####### Titulo de nivel 7 ##################


Aqui podeis escribir texto. Este sería una frase.
Y esto otra frase del mismo párrafo.

Si dejo 2 saltos de linea (1 linea en blanco), 
Markdown entiende que comienza un nuevo párrafo.
Incluso podria poner una frase dntro de un párrafo, comenzando en una linea nueva.  
Para ello, tendría que acabar la linea anterior con 2 espacios en blanco.
Esto no se hace mucho, lo de los 2 espacios en blanco... 
no se ve a priori en el fichero esos espacios en blanco.\
En su lugar puedo usar una contrabarra.

Esto ya sería otro parrafo.

