
aliveTracker_ws (Back-End)
==========================

## Descripción ##

Proyecto que será integrado como el back-end para la aplicación web de AliveTracker2.0 **(Memoranda)**

## Tecnologías ##
 - Python 
 - MySQL

## Descarga de Proyecto

> $ git clone https://github.com/Alivebox/aliveTracker_ws.git

##Configuración de Ambiente

Por convenciones del proyecto la versión de python que se debe descargar es la ***2.7.6***

 1. Intalar el interprete de python

    Se descarga el instalador de python del siguiente link:

    http://www.python.org/download/releases/2.7.6/
    
    Por lo general se creará la carpeta para el runtime de Python en esta dirección
    
     ***C:\Python27***
    
 2. Configurar variables de entorno e Instalación de PIP
    
    Las variables de entorno de debe descargar para poder ejecutar 
    los comandos de python y pip en la consola de comandos.
    
    - Crear una carpeta llamada Scripts dentro del runtime de Python, en esta carpeta posteriormente se debe agregar el archivo     ***get-pip.py*** (este paso se realizará posteriormente)
        
     ***C:\Python27\Scripts***

    - Configurar las variables de entorno en el sitema operativo(solo se aplica a windows)
        
        en la varible de entorno ***path*** agregar las siguientes rutas
        
       ***C:\Python27\\***
       ***C:\Python27\Scripts\\***
       
    - Descargar el archivo get_pip.py
        
        https://raw.github.com/pypa/pip/master/contrib/get-pip.py
        
        En el anterior url se encuentra el codigo fuente con el que funciona ***pip*** lo copiamos y creamos un archivo ***"get_pip.py"***(El nombre del archivo puede ser cualquiera pero la extensión si debe ser ***.py***) dentro de la siguiente ruta:
        ***C:\Python27\Scripts\\***
        
    - Instalación de pip
        
        Correr el siguiente comando en la linea de comandos.

        > python get_pip.py
        
        Con este comando instalamos pip y automaticamente         nos instalará el setuptools.py que va ser                 necesario para desarrollar.
        
    - Instalar rest-framework via pip 
        
        > pip install djangorestframework
          pip install markdown
          pip install pyyaml
          pip install django-filter
          
    -instalar 
        Ahora a conectar la aplicación con la base de datos, para este proyecto MySQL.

 3. Connectar la aplicación con la base de datos
    
    - descargar MySql-python connector via pip:
        
        > pip install MySQL-python
    
    Para este caso el motor de base dedatos esta corriendo localmente en mi maquina, 
la dirección ip del localhost ya dependerá donde tengan corriendo la base de datos. 

    - Agregar credenciales de conexión al proyecto 
    
        Modificaremos el archivo ***settings_dev.py*** localizado en la siguiente ruta dentro del proyecto:
    

            > aliveTracker_ws / aliveTracker_ws /

     Si entran a este directorio van a notar que hay dos archivos muy parecidos uno llamado ***settings_dev.py*** y                     ***settings.py***
        el segundo es el archivo que es utilizado cuando se esta en ambiente de producción y que lo que va a cambiar son los            parametros de configuración dentro de cada uno de ellos.

        Para este caso solo vamos a necesitar modificar el archivo ***settings_dev.py*** .

     Dentro del archivos vamos a modificar el bloque de: ***DATABASES***

        > DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'NAME': 'alivetrackertest',  # data base name  
         # The following settings are not used with sqlite3:
         'USER': 'root',
         'PASSWORD': 'admin',
         'HOST': '127.0.0.1',
         'PORT': '3307',
      }
    }

        Los parametros (NAME,USER,PASSWORD, HOST, PORT) son especificos para este caso ya que yo tengo la base de datos                 instalada localmente.
        
    Finalmente abrir la linea de comandos en la raíz del proyecto donde se encuentra el archivo **manage_dev.py** y ejecutar el     siguiente comando: 

    > pyhton manage_dev.py runserver

    Les debera aparecer algo como esto para saber que tenemos la aplicación corriendo en el servidor. 
    > 0 errors found
    February 27, 2014 - 16:25:09
    Django version 1.6.2, using settings 'aliveTracker_ws.settings_dev'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

Fin  :)