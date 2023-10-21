import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

# Carregar o modelo treinado
model = joblib.load('../../trained_model/Ex_Aula02.pkl')

# Criar instâncias da FastAPI
app = FastAPI()

# Definir o modelo Pydantic para a estrutura de entrada
class ImputData(BaseModel):
    input: list[float]

# Criar a FastAPI com o modelo
@app.post("/predict")
async def predict(input_data: InputData):
    data = np.array(input_data.input)
    prediction = model.predict(data.reshape(1, -1))
    return {'predictioin': prediction.tolist()}

# Rodar no terminal: uvicorn main:app --reload