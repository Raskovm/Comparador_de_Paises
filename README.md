# Comparador de Países

## Introducción

**Comparador de Países** es una aplicación web interactiva que permite comparar datos clave de diferentes países del mundo. Utilizando información actualizada del **CIA World Factbook**, los usuarios pueden comparar indicadores económicos, sociales y de infraestructura, como el Producto Interno Bruto (PIB), la población, la tasa de alfabetización, la esperanza de vida, entre otros.

La aplicación está diseñada para ser sencilla de usar, permitiendo seleccionar dos países y visualizar sus datos en una tabla comparativa de manera clara. Este proyecto es ideal para quienes deseen obtener una visión rápida y visual de las diferencias entre países, ya sea para análisis, educación o simplemente por curiosidad.

## Características

- Comparación entre dos países de diferentes regiones.
- Visualización de indicadores clave como PIB, población, esperanza de vida, y más.
- Acceso a datos actualizados del **CIA World Factbook**.
- Interfaz intuitiva que facilita la selección de países y la visualización de las comparaciones.

## Tecnologías Utilizadas

- **Flask**: Framework de Python utilizado para crear la API y la interfaz web.
- **Jinja2**: Motor de plantillas para renderizar las páginas web.
- **Docker**: Contenerización de la aplicación para facilitar su despliegue y distribución.
- **GitHub**: Control de versiones y alojamiento del código fuente.
- **CIA World Factbook**: Fuente de datos utilizada para obtener información detallada sobre los países.

## Requisitos

Antes de comenzar, asegúrate de tener los siguientes programas instalados:

- **Python 3.6+**
- **Docker** (para contenerización)
- **Git** (para clonar el repositorio)

## Instalación y Ejecución

### 1. Clonar el repositorio:

```bash
git clone https://github.com/Raskovm/comparador_de_paises.git
```

### 2. Navegar al directorio del proyecto:
```bash
Copiar
cd comparador_de_paises
```

### 3. Configurar el entorno virtual:
 ```bash
Copiar
python3 -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
 ```
### 4. Instalar las dependencias:

 ```bash
bash
Copiar
pip install -r requirements.txt
 ```

### 5. Instalar las dependencias:
```bash
Copiar
pip install -r requirements.txt
```

### 6. Ejecutar la aplicación:
```bash
bash
Copiar
python app.py
La aplicación se ejecutará en http://127.0.0.1:5000/ por defecto.
 ```
