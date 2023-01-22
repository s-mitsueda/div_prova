"""
Crie uma API Rest em Python, que responda à seguinte chamada:

    curl -X POST 'http://localhost:5000/soma' -H 'Content-type: application/json' -d '{"x": 1, "y"; 2}'

A API /soma irá receber o valor x e somar com o valor y e retorná-lo em JSON no seguinte formato:

    {"resultado": <valor do resultado>}

Para o exemplo acima, iremos retornar:

    {"resultado": 3}

Os valores de entrada x e y são obrigatórios e devem ser números.
"""

from fastapi import FastAPI
from pydantic import BaseModel

class RequestModel(BaseModel):
    x: int
    y: int

app = FastAPI()

@app.post("/soma")
def soma(req: RequestModel):
    result = req.x + req.y
    return {"resultado": result}