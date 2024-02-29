# Excepciones 

Cuando se intenta generar un bloque de código pero salta un error, entonces se procede a detener el script, por lo que en estas situaciones se comienza con un try o "prubeba" y except o "exception" el cual puede ser global (atiene a todos los errores) o delimitado (indicando el tipo de error que nos aparece en consola)

## Try exception
Para saber un poco más acerca de los errores que pueden aparecernos y los motivos, tendríamos que ir al sitio oficial de python
de ahí a documentation, de ahí a Docs --> botón python doc's, seleccionamos la versión que estaríamos manejando y podemos ver todo lo relacionado a documentación 

Se pueden crear los exception "personalizados" con rise --> el tipo de error y lo que va a devolver ese error, esto aplica para hacer validaciones

## Import os 

Importa una librería del sistema operativo y podemos usar alguno de sus métodos para realizar algúna acción en específico, por ejemplo como con el caso de read, en donde se ocupo os.path.exists para saber si un archivo existía para poder leerlo 


## CSV y JSON

Comma separated values

Al momento de hablar de csv estamos hablando de un conjunto de datos separados por comas.

"Nos estamos refiriendo a una forma de escribir los datos y seguir ciertas normas para interpretar esos datos"

en los JSON es prácticamente lo mismo, debemos seguir esas reglas que nos dió JS para entender los objetos

Si seguimos el protocolo de objetos de js cada conjunto de datos va a ser delimitado por llaves y adicionalmente por dentro nos vamos a ayudar de las "" para delimitar valores y propiedades, cada una de las propiedades van a estar separadas por comas.

Básicamente es como una forma de interpretar los objetos JSON a diccionarios en python

Pasa lo mismo con el tema de los arreglos solamente que para python manejando las listas (inclusive si tenemos un arreglo de objetos) siendo para python una lista de diccionarios mientras esto se va a delimitar como conjunto 1 y conjunto 2. 

# JSON

Formato a manejar:
[{'k1':v1}, {'k2':'v2'}]

se pueden crear diccionarios en python --> crear una lista con los diccionarios --> usar json.dumps(lista) --> usar nuestra librería create('nombre del texto' , la lista de los diccionarios ya pasada por json.dumps) y procede a crearnos un .txt que tiene los elementos de nuestra lista ya en string (recuerda que python no puede de forma nativa escribir una lista, diccionarios o X dentro de un archivo .txt)
al usar  los métodos JSON ayuda a convertir los datos a sus string textuales  

