from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/time")
def get_current_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    return {"datetime": now}