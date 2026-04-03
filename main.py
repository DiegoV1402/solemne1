from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/time")
def get_current_time():
    # Obtenemos la hora del sistema y le damos el formato pedido
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Devolvemos el diccionario con la llave "datetime" para cumplir tu esquema
    return {"datetime": now}