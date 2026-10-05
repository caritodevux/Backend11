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

## Prueba POST sin autenticación
Enviar datos a traves del formulario de la interfaz sin iniciar sesión.
En el Terminal:
```terminal
curl -X POST http://127.0.0.1:8000/api/v1/productos/ -H "Content-Type: application/json" -d "{\"nombre\": \"Figura Goku\", \"categoria\": \"Figuras\", \"precio\": 24990, \"stock\": 8, \"activo\": true}"
```
```terminal
curl.exe -X POST http://127.0.0.1:8000/api/v1/productos/ -H "Content-Type: application/json" -d "{\"nombre\": \"Figura Goku\", \"categoria\": \"Figuras\", \"precio\": 24990, \"stock\": 8, \"activo\": true}"
```
Entrega:
```terminal
Forbidden: /api/v1/productos/
[02/Oct/2026 20:11:37] "POST /api/v1/productos/ HTTP/1.1" 403 58
```

## Prueba POST con autenticación
Acceder como admin
http://127.0.0.1:8000//api-auth/login/

En http://127.0.0.1:8000/api/v1/productos/, se agrega un item:
Si fue correcto, sale:
"POST /api/v1/productos/ HTTP/1.1" 201 10483

## Prueba PATCH y PUT (actualizar el recurso)
Vamos a http://127.0.0.1:8000/api/v1/productos/1/ y alteramos el stock a 
12 con PATCH, en terminal aparece:
```
"PATCH /api/v1/productos/1/ HTTP/1.1" 200 11845
```
Y con PUT, probamos una actualización completa, en terminal:
```
"PUT /api/v1/productos/1/ HTTP/1.1" 200 11855
```

## Probar DELETE
En /api/v1/productos/1/ En la parte superior derecha de la pantalla 
(justo al lado del botón "GET"), verás un botón rojo que dice DELETE.
```
HTTP 404 Not Found
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "No Producto matches the given query."
}
```

## Validar que el servidor no confía en el cliente
- Volver a la ruta principal: http://127.0.0.1:8000/api/v1/productos/
- Intento poner productos y precio negativos
```
IntegrityError at /api/v1/productos/
CHECK constraint failed: precio
```
En terminal:
```terminal
"POST /api/v1/productos/ HTTP/1.1" 500 192770
```

## Analizar autenticación y autorización
- Desloguear como admin
- Recargar http://127.0.0.1:8000/api/v1/productos/
En terminal:
```terminal
"GET /api/v1/productos/ HTTP/1.1" 200 5371
```
- Se ve la lista de productos, pero no puedo agregar nada.

- Meterse a la mala usando curl, en temrinal:
```
curl -X POST http://127.0.0.1:8000/api/v1/productos/ \
-H "Content-Type: application/json" \
-d '{"nombre": "Prueba", "precio": 1000, "stock": 5}'
```
Aparece: curl: (6) Could not resolve host: curl
{"detail":"Las credenciales de autenticación no se proveyeron."}% 

