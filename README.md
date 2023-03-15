## Segunda Pre entrega de Python :clipboard:

##### La segunda pre entrega del curso de python de CoderHouse dictado por el prof. Franco Gabriel Di Martino y por el tutor Enzo Martin Zotti tuvo como tema principar crear class y objetos con el eje Cliente. Las consignas fueron las siguientes

#### Objetivo 
##### Practicar el concepto de Clases y Objetos.

#### Consigna

- Crear un programa que permita el modelamiento de Clientes en una página de compras. Se debe utilizar el concepto de Programación Orientada a Objetos y lo aprendido en clase.
- Se evaluará el uso correcto de atributos y métodos.
- Utilizar los conceptos aprendidos en la clase 15 y crear un paquete redistribuible con el programa creado."

#### Formato  

##### El proyecto debe ser un archivo comprimido del paquete. Formatos aceptados: .zip o .tar.gz bajo el nombre “Segunda pre-entrega+Apellido”.

#### Pasos :gear:

 ##### 1. Para la confección de este entregable se realizo un diagrama de clases como guia ([diagrama](https://drive.google.com/file/d/1JxXkR4UDlpRlgr2GgJE28bMgUQhCkTTj/view))

 ##### 2. Para llevarlo a codigo se uso el editor de codigo Visual Studio Code donde se instalo la extension Python que podemos encontrar en la galeria de extensiones

 ##### 3. Con la guia del diagrama se fueron llevando a codigo los anteriormente planteado tratando de usarse la mayor cantidad de conceptos vistos en clase. El fin de esto es poder aprovechar todo lo dictado por los profesores.

 ##### 4. Se realizo la clase Cliente de donde se hereda sus artributos y metodos a sus hijos cliente gold y cliente black y se colocan atributos propios para estos hijos.  Tambien se crea una carpeta de assets donde se coloraca todo el codigo de soporte para un mejor ordenamiento de los componente y cladidad del paquete en si

 ##### 5. En la clase Cliente se crearon atributos sencills (Id, nombre, direccion, telefono) y dos metodos: un carrito super sencillo con funcionalidades basicas como es agregar producto, quitar producto, ver lista y salir del programa. Tambien puede elegirse el tipo de membresia que se quiere adquirir.
 
 ##### 6. para las clases hijas heredaran todos sus componente pero se agregan como son para la clase cliente gold poder elegir la membresia gratuita de una app y para la class black decuento diario en su app favorita de comidas.
 
 ##### 7. Este proghrama tb esta acompañado de un login el cual usa la libreria sys que se usa para crear en la consola argumentos que se usaran enla funcion estos tienen un indice por el cual se identifican los mismos fueron colocados detro de una funcion para retener el dato y asi usarlo para compararlo con el usuario y contraseña, tambien se uso la libreria getpass que esconde al momento de teclear en la consola para ocultar los datos tipeados.
 ##### 8. una vez terminado todo se procede a crear un archivo __init__.py lo que nos da sentido de paquete a los modulos contenidos en la carpeta, luego el archivo setup.py que indica nombre, version, descripcion, y paquetes contenidos para finamlente a traves del comando python setup.py sdist en la consola se procede a comprimir todo para transformaelo en un paquete que puede ser compartido.

 ###### Todo esto y mas podras ver en mi [GitHub](https://github.com/Danisole/) 

