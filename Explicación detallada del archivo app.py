1. Importación de librerías

from flask import Flask, render_template, request
import json
import os
from tabulate import tabulate

-Flask: framework ligero para aplicaciones web en Python.
-render_template: permite renderizar archivos HTML usando Jinja2.
-request: accede a parámetros enviados por el navegador.
-json: carga datos estructurados tipo JSON.
-os: gestiona rutas de archivos.
-tabulate: convierte listas en tablas HTML con formato limpio.

2. Configuración inicial

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FACTBOOK_DIR = os.path.join(BASE_DIR, 'factbook')

-Se define BASE_DIR como la ruta raíz del proyecto y FACTBOOK_DIR como la carpeta donde se almacenan los JSON por región.

3. Diccionario de regiones

REGIONES = {
  'africa': 'África',
  ...
  'south-asia': 'Sur de Asia'
}

-Mapea las carpetas del sistema (códigos internos) con sus nombres legibles para el usuario.

4. Función safe_get

def safe_get(data, keys, default="N/A"):

-Permite acceder de forma segura a campos anidados de un JSON.
-Si en algún punto la clave no existe, retorna "N/A" en vez de lanzar un error.

5. Función get_countries_by_region

def get_countries_by_region(region=''):

-Devuelve todos los países de una región (o de todas si region='').
-Busca archivos .json, extrae el nombre del país desde su estructura anidada y lo retorna como lista de diccionarios: {'codigo': ..., 'nombre': ...}.
-Ordena los países alfabéticamente.

6. Función extraer_datos

def extraer_datos(codigo_pais):

-Busca el archivo JSON del país correspondiente (por código ISO).
-Extrae campos clave como:
-PIB (PPA)
-Población
-Crecimiento económico
-Usuarios de internet
-Expectativa de vida
-Alfabetización
-Tasa de desempleo
-Aeropuertos
-Puertos
-Sitios de Patrimonio Mundial
-También construye el URL para mostrar su bandera (flag_url).

7. Ruta /

@app.route('/')
def home():
    return render_template('index.html', regiones=REGIONES)

-Página principal donde se muestran las regiones disponibles.

8. Ruta /seleccionar-paises

@app.route('/seleccionar-paises', methods=['GET'])

-Se accede tras elegir una región.
-Renderiza seleccion_paises.html con los países de esa región.

9. Ruta /comparar

@app.route('/comparar', methods=['GET'])

-Recibe los códigos de dos países (pais1, pais2) desde la URL.
-Llama a extraer_datos para cada uno.
-Construye una tabla comparativa de indicadores.
-Usa tabulate(..., tablefmt="html") para generar HTML limpio.
-Muestra el resultado con resultado.html.

10. Inicio de la aplicación

if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG', 'False') == 'True'
    app.run(debug=debug, host="0.0.0.0", port=80)

-Activa el modo debug si la variable de entorno FLASK_DEBUG=True.
-Corre el servidor Flask en el puerto 80, accesible desde cualquier IP (0.0.0.0), útil para despliegue en Docker o la nube.
