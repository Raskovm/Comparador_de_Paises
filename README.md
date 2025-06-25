# Comparador de Países

![Mundo 3D](https://www.example.com/imagen.png)

**Comparador de Países** es una aplicación web desarrollada en **Flask**, diseñada para facilitar la comparación de países a partir de datos provenientes de diversas fuentes globales, principalmente del **CIA World Factbook**. Esta aplicación permite comparar indicadores clave de desarrollo entre países, como el **PIB (PPA)**, **población**, **crecimiento económico**, **internet**, **alfabetización**, **tasa de desempleo**, **expectativa de vida**, y otros datos relevantes.

### Contexto del Proyecto

Este proyecto ha sido desarrollado en el marco del curso de **Tecnologías de la Información** de la **Facultad de Ciencias**, como parte de un ejercicio académico en el que se busca aplicar conceptos de desarrollo web, manejo de bases de datos, y análisis de datos, al tiempo que se fomenta el uso de tecnologías modernas como **Docker**, **Flask**, y **pytest** para las pruebas automatizadas.

La idea es proporcionar una plataforma intuitiva y funcional que permita al usuario seleccionar países de diferentes regiones del mundo y comparar sus características socioeconómicas, con un enfoque en el análisis de datos en tiempo real. Este tipo de herramientas es útil para estudiantes, investigadores, economistas y cualquier persona interesada en comparar el desarrollo de los países y entender mejor las relaciones globales.

### Objetivos del Proyecto

El proyecto tiene como objetivo proporcionar una herramienta accesible y eficiente para comparar diferentes países. Específicamente, el propósito es:

- **Desarrollar una aplicación web interactiva**: que permita comparar países de manera sencilla y eficiente a través de una interfaz gráfica.
- **Integrar múltiples fuentes de datos**: utilizar la información del **CIA World Factbook**, que es una de las fuentes más completas sobre las características socioeconómicas de los países del mundo.
- **Fomentar el uso de herramientas de desarrollo modernas**: utilizar **Docker** para crear contenedores de la aplicación y garantizar un entorno de desarrollo replicable.
- **Automatizar las pruebas**: mediante **pytest**, para asegurar la calidad del código y la integridad de la aplicación.

### ¿Para qué sirve este proyecto?

Este comparador de países permite realizar análisis socioeconómicos entre diferentes naciones de manera interactiva. Algunos posibles usos de la aplicación incluyen:

- **Estudios comparativos**: Estudiantes y profesionales de la economía, relaciones internacionales y ciencias sociales pueden utilizar la herramienta para comparar el desarrollo de diferentes países a lo largo de varios indicadores.
- **Investigación de políticas públicas**: Analistas pueden usar la plataforma para estudiar las condiciones socioeconómicas de diferentes países y sugerir políticas que puedan mejorar el desarrollo.
- **Toma de decisiones empresariales**: Las empresas globales pueden usar estos datos para analizar mercados potenciales y tomar decisiones informadas sobre expansión internacional.
- **Educación**: Profesores y estudiantes pueden utilizarla para enseñar y aprender sobre el desarrollo de los países de forma visual y dinámica.

### Características Principales

- **Interfaz web interactiva**: Los usuarios pueden seleccionar dos países de diferentes regiones (África, Asia, Europa, América, etc.) y comparar una serie de indicadores clave como el **PIB (PPA)**, **población**, **tasa de desempleo**, **alfabetización**, entre otros.
- **Datos actualizados del CIA World Factbook**: La aplicación utiliza datos actualizados del **CIA World Factbook**, una fuente confiable y bien documentada.
- **Pruebas automatizadas**: El proyecto incluye pruebas automatizadas para verificar que la funcionalidad de la aplicación esté correctamente implementada. Las pruebas utilizan la biblioteca **pytest**.
- **Despliegue en Docker**: La aplicación está dockerizada, lo que permite ejecutar la aplicación y realizar pruebas en entornos aislados, asegurando que funcione de manera consistente en cualquier máquina.

### Tecnologías Utilizadas

Este proyecto hace uso de diversas tecnologías modernas para el desarrollo y despliegue de la aplicación:

- **Flask**: Framework web en Python para construir aplicaciones web de manera rápida y sencilla.
- **Docker**: Utilizado para contenerizar la aplicación y garantizar un entorno de desarrollo consistente.
- **pytest**: Herramienta de pruebas automatizadas que asegura que la funcionalidad del código se mantenga estable durante el desarrollo.
- **CIA World Factbook**: Fuente de datos confiable y ampliamente utilizada para obtener información sobre los países del mundo.
- **HTML, CSS**: Para la creación de la interfaz de usuario, con un diseño limpio y accesible.

### Requisitos

Para ejecutar este proyecto en tu máquina local, necesitarás:

- **Python 3.9 o superior**.
- **Docker** y **Docker Compose** (opcional para uso de contenedores).
- **Git** para clonar el repositorio.

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
