"""
Crie um programa que seja uma API de um contador de números.
Esta API irá manter o número em sua memória, e esta irá iniciar com o valor 0 (zero).

Para o programa teremos as seguinte chamadas:

        POST /contador
        {"numero": <numero>}
    Irá definir um novo número para o nosso contador. O método irá retornar um HTTP 201.

        GET /contador
    Retorna o número que foi guardado na memória, em um JSON no formato:
        {"numero": <numero guardado>}
    E também um HTTP 200.

        PUT /contador/incrementa
    Irá incrementar o valor do número em 1 e retornar um HTTP 202.

        DELETE /contador
    Irá zerar o valor do contador. A API irá retornar um HTTP 202.
"""
"""
Seguem algumas chamadas que fizemos no terminal,
para mostrar o comportamento de nosso programa.
Considere que iniciamos o programa agora
e executamos os testes na ordem apresentada:

    curl -X GET 'http://localhost:5000/contador'
    >>> {"numero": 0}
    curl -X POST 'http://localhost:5000/contador' -d '{"numero": 123}'  # HTTP 201
    curl -X GET 'http://localhost:5000/contador'
    >>> {"numero": 123}
    curl -X PUT 'http://localhost:5000/contador/incrementa'             # HTTP 202
    curl -X GET 'http://localhost:5000/contador'
    >>> {"numero": 124}
    curl -X DELETE 'http://localhost:5000/contador'                     # HTTP 202
    curl -X GET 'http://localhost:5000/contador'
    >>> {"numero": 0}
 """

from fastapi import FastAPI
from pydantic import BaseModel
from uvicorn import run

class NumberModel(BaseModel):
    numero: int

app = FastAPI()
app.counter = 0

@app.get("/contador", status_code=200, response_model=NumberModel)
def get_number():
    return NumberModel(numero=app.counter)

@app.post("/contador", status_code=201)
def post_number(req: NumberModel):
    app.counter = req.numero

@app.put("/contador/incrementa", status_code=202)
def put_number():
    app.counter += 1

@app.delete("/contador", status_code=202)
def delete_number():
    app.counter = 0

if __name__ == "__main__":
    run("questao8_ok:app", reload=True)
