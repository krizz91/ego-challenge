# EGO Challenge

Esta es una aplicación Django que proporciona una forma de administrar los autos a la venta. Tambien, ofrece varios enpoints para poder obtener de manera publica la informacion.

## Instalación
Sigue estos pasos para configurar y ejecutar la aplicación localmente:

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/krizz91/ego-challenge.git
```

2. Accede al directorio de la aplicación:

```bash
cd ego-challenge
```

3. Crea un entorno virtual para la aplicación (se recomienda utilizar venv):

```bash
python -m venv venv
```

4. Activa el entorno virtual:

- En Windows:

```bash
venv\Scripts\activate
```

- En macOS y Linux:

```bash
source venv/bin/activate
```

5. Instala las dependencias de la aplicación:

```bash
pip install -r requirements.txt
```

6. Aplica las migraciones de la base de datos:

```bash
python manage.py migrate
```

7. Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

La aplicación ahora estará en funcionamiento localmente en `http://127.0.0.1:8000/`.

## Endpoints Disponibles
A continuación se muestra una lista de los endpoints disponibles en esta aplicación:

- `/api/list/` - Lista todos los autos disponibles.
  - Métodos HTTP soportados: GET
  - Parámetros de filtro:
    - `car_type` (espera el id del tipo de vehiculo a filtrar)
  - Parámetros de ordenamiento (`ordering`):
    - `price` o `-price` (ordena por precio)
    - `created` o `-created` (ordena por fecha de creación)
- `/api/type_list/` - Lista todos los tipos de autos disponibles. 
  - Métodos HTTP soportados: GET
- `/api/get/<id>/` - Detalles de un auto en específico.
  - Métodos HTTP soportados: GET

## Administracion
La carga, modificacion y borrado de `autos` y `tipos de autos` se hace desde el Admin de Django

`http://127.0.0.1:8000/admin/`
