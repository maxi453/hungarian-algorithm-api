from fastapi import FastAPI
import app.algorithms as algorithms
import app.schemas as schemas
import app.services as services

app = FastAPI()

# Configuración de CORS obligatoria para conectar con el frontend


#genero el protocolo a seguir cuando llega un post
@app.post("/resolver", response_model = schemas.Resultado) #porque app.post y no caca.cacona?? de q depende cadacosa 
#llama a la funcion resolver y el resultado tiene q corresponderse a schemas.Resultado

def resolver(entrada: schemas.matriz_entrada):
    #llama a procesar_resolver q se encarga de ver si la entrada es valida o no
    matriz = services.procesar_resolver(entrada)
    #llamo al algoritmo hungaro q devuelve el matching y la suma minima 
    matching, min_suma = algorithms.hungaro_resolver(matriz)
    #devuelvo algo de la clase resultado para asegurar q cumpla los tipos 
    result = schemas.Resultado(matching = matching, min_sum = min_suma)
    return result 