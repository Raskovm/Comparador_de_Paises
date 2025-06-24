from flask import Flask, render_template, request
import json
import os
from tabulate import tabulate

app = Flask(__name__)

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FACTBOOK_DIR = os.path.join(BASE_DIR, 'factbook')

REGIONES = {
    'africa': 'África', 'antarctica': 'Antártida', 'australia-oceania': 'Australia y Oceanía',
    'central-america-n-caribbean': 'Centroamérica y Caribe', 'central-asia': 'Asia Central',
    'east-n-southeast-asia': 'Este y Sudeste Asiático', 'europe': 'Europa', 'middle-east': 'Medio Oriente',
    'north-america': 'Norteamérica', 'south-america': 'Sudamérica', 'south-asia': 'Sur de Asia'
}

def safe_get(data, keys, default="N/A"):
    """Función para obtener datos de un JSON de forma segura."""
    for key in keys:
        data = data.get(key, default)
        if data == default: break
    return data

def get_countries_by_region(region=''):
    """Obtiene todos los países de una región específica o de todas las regiones."""
    paises = []
    for region_code, region_name in REGIONES.items():
        if region and region != region_code: continue
        region_path = os.path.join(FACTBOOK_DIR, region_code)
        if os.path.isdir(region_path):
            for archivo in os.listdir(region_path):
                if archivo.endswith('.json'):
                    codigo_pais = archivo.split('.')[0].upper()
                    try:
                        with open(os.path.join(region_path, archivo), 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        nombre = safe_get(data, ["Government", "Country name", "conventional short form", "text"], codigo_pais)
                        paises.append({'codigo': codigo_pais, 'nombre': nombre})
                    except Exception as e:
                        print(f"Error procesando {archivo}: {str(e)}")
    return sorted(paises, key=lambda x: x['nombre'])

def extraer_datos(codigo_pais):
    """Extrae datos de un país específico en cualquier región."""
    archivo = f"{codigo_pais.lower()}.json"
    for region in REGIONES:
        region_path = os.path.join(FACTBOOK_DIR, region)
        ruta_archivo = os.path.join(region_path, archivo)
        if os.path.exists(ruta_archivo):
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return {
                    "País": safe_get(data, ["Government", "Country name", "conventional short form", "text"], codigo_pais.upper()),
                    "codigo": codigo_pais,
                    "PIB (PPA)": safe_get(data, ["Economy", "Real GDP (purchasing power parity)", "Real GDP (purchasing power parity) 2023", "text"]),
                    "Población": safe_get(data, ["People and Society", "Population", "total", "text"]),
                    "Crecimiento económico": safe_get(data, ["Economy", "Real GDP growth rate", "Real GDP growth rate 2023", "text"]),
                    "Internet (%)": safe_get(data, ["Communications", "Internet users", "percent of population", "text"]),
                    "Expectativa de vida": safe_get(data, ["People and Society", "Life expectancy at birth", "total population", "text"]),
                    "Alfabetización": safe_get(data, ["People and Society", "Literacy", "total population", "text"]),
                    "Desempleo": safe_get(data, ["Economy", "Unemployment rate", "Unemployment rate 2024", "text"]),
                    "Aeropuertos": safe_get(data, ["Transportation", "Airports", "text"]),
                    "Puertos": safe_get(data, ["Transportation", "Ports", "total ports", "text"]),
                    "Patrimonio Mundial": safe_get(data, ["Government", "National heritage", "total World Heritage Sites", "text"]),
                    "flag_url": f"https://flagcdn.com/w320/{codigo_pais.lower()}.png"
                }
            except Exception as e:
                print(f"Error al procesar {ruta_archivo}: {str(e)}")
    return None

@app.route('/')
def home():
    return render_template('index.html', regiones=REGIONES)

@app.route('/seleccionar-paises', methods=['GET'])
def seleccionar_paises():
    region = request.args.get('region', '')
    paises = get_countries_by_region(region)
    nombre_region = REGIONES.get(region, 'Todas las regiones')
    return render_template('seleccion_paises.html', region=region, nombre_region=nombre_region, paises=paises, todas_regiones=REGIONES)

@app.route('/comparar', methods=['GET'])
def comparar_paises():
    pais1 = request.args.get('pais1')
    pais2 = request.args.get('pais2')
    
    if not pais1 or not pais2:
        return "Debes seleccionar dos países", 400

    datos_pais1 = extraer_datos(pais1)
    datos_pais2 = extraer_datos(pais2)
    
    if not datos_pais1 or not datos_pais2:
        return "No se pudieron obtener los datos de uno o ambos países", 400
    
    tabla = [
        ["Indicador", datos_pais1["País"], datos_pais2["País"]],
        ["PIB (PPA)", datos_pais1["PIB (PPA)"], datos_pais2["PIB (PPA)"]],
        ["Población", datos_pais1["Población"], datos_pais2["Población"]],
        ["Crecimiento económico (%)", datos_pais1["Crecimiento económico"], datos_pais2["Crecimiento económico"]],
        ["Usuarios de internet (%)", datos_pais1["Internet (%)"], datos_pais2["Internet (%)"]],
        ["Expectativa de vida", datos_pais1["Expectativa de vida"], datos_pais2["Expectativa de vida"]],
        ["Alfabetización (%)", datos_pais1["Alfabetización"], datos_pais2["Alfabetización"]],
        ["Tasa de desempleo (%)", datos_pais1["Desempleo"], datos_pais2["Desempleo"]],
        ["Aeropuertos", datos_pais1["Aeropuertos"], datos_pais2["Aeropuertos"]],
        ["Puertos", datos_pais1["Puertos"], datos_pais2["Puertos"]],
        ["Sitios Patrimonio Mundial", datos_pais1["Patrimonio Mundial"], datos_pais2["Patrimonio Mundial"]]
    ]
    
    tabla_html = tabulate(tabla, headers="firstrow", tablefmt="html")
    
    return render_template('resultado.html', tabla_comparativa=tabla_html, pais1=datos_pais1, pais2=datos_pais2)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
