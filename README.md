# Solemne 1: API de hora actual (FastAPI)

Esta aplicación es una API REST desarrollada con FastAPI que entrega la fecha y hora actual del sistema en formato JSON. 

## 🚀 Ejecución Local (usando uvicorn)
1. Activar entorno virtual: `.\.venv\Scripts\activate` 
2. Instalar dependencias: `uv pip install -r requirements.txt` 
3. Iniciar el servidor: `uvicorn main:app --reload` 

## 🐳 Ejecución con Docker
1. Construir la imagen: `docker build -t api-time-solemne .` 
2. Ejecutar el contenedor: `docker run -p 8000:8000 api-time-solemne` 

## 🧪 Cómo testear la API
Puedes verificar el funcionamiento de la API de las siguiente manera:
* **Navegador web:** Ingresa a `http://localhost:8000/time` 
