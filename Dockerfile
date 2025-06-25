# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Primero copia solo requirements.txt para cachear dependencias
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install pytest==8.4.1  # Instala pytest directamente

# Copia el resto de los archivos
COPY . .

# Variables de entorno (ajustables desde docker-compose)
ENV FLASK_APP=app.py \
    FLASK_ENV=production \
    PYTHONUNBUFFERED=1

# Expone el puerto
EXPOSE 80

# Comando de ejecución (sobrescribible en docker-compose)
CMD ["python", "app.py"]
