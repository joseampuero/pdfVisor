Pasos a seguir:

- Instalamos virtualenv (si ya lo tenes no es necesario)

- Activamos el ambiente para instalar los paquetes necesarios para el proyecto.

- Instalamos django.

- Corremos los siguientes comandos:
django-admin startproject 'nombre_proyecto' . 
python manage.py runserver

Hasta ahora lo que hicimos fue crear el proyecto con un nombre especifico. Luego, levantamos el servidor y nos redirecciona a una pagina que nos avisa que la instalacion fue exitosa.

- Corremos los siguientes comandos:
python manage.py startapp 'nombre_componente'

En este paso creamos uno de los modulos/app que componen la aplicacion en si. 

- Agregar el nombre del/os modulo/s a la seccion INSTALLED_APP de nombre_proyecto/settings.py

- Si agregas modelos nuevos hay que correr migraciones 
python manage.py makemigrations


Para instalar pdfMiner tire dos comandos:
pip install pdfminer3k
pip3 install pdfminer.six

- Para correr el proyecto 
source env/bin/activate
python manage.py runserver