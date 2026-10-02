# Fase entorno e instalación
## 1. Crear el entorno virtual
python3 -m venv venv

## 2. Activar el entorno virtual
### En macOS / Linux:
source venv/bin/activate
### En Windows (PowerShell / CMD):
venv\Scripts\activate

## 3. Instalar las dependencias requeridas
pip install django djangorestframework

## 4. Crear el proyecto Django y la aplicación 'productos'
django-admin startproject nekostore_api .
python manage.py startapp productos

# Fase 2
## Registrar las aplicaciones en settings.py
Abre nekostore_api/settings.py y agrega 'rest_framework' y 'productos' a la lista INSTALLED_APPS

## Crear el modelo Producto
- En el archivo productos/models.py, define el modelo de datos.
- Ejecutamos las migraciones

# Fase 3
## Crear serializer
Crea un nuevo archivo llamado serializers.py dentro de la carpeta productos/ (productos/serializers.py)

# Fase 4
## Crear el viewset con permisos
Edita el archivo productos/views.py para usar ModelViewSet e incorporar la regla de permisos IsAuthenticatedOrReadOnly

# Fase 5
## Configurar routers y URLs
Crea el archivo productos/urls.py
Edita el archivo principal de rutas nekostore_api/urls.py

# Fase 6
## Crear superuser
python manage.py createsuperuser

## Inicia Servidor
python manage.py runserver

## Prueba GET
http://127.0.0.1:8000/api/v1/productos/
Debe salir: HTTP 200 OK

## Prueba POST
Enviar datos a traves del formulario de la interfaz sin iniciar sesión.

## Acceder como admin
http://127.0.0.1:8000//api-auth/login/