from fastapi import FastAPI, Request
import requests

app = FastAPI()

# Ruta para suscripción de Dapr (puede estar vacía si no se usa pub/sub)
@app.get("/dapr/subscribe")
async def dapr_subscribe():
    return []

@app.get("/empleados1")
async def get_empleados(request: Request):
    try:
        # Utilizar la URL correcta para el API empleados2
        empleados2_url = "http://localhost:8001/empleados2"
        response = requests.get(empleados2_url, params=request.query_params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)