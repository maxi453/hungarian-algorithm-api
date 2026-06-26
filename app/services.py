from fastapi import HTTPException
import app.schemas as schemas


def validar_matriz(entrada: schemas.matriz_entrada):
    if len(entrada.matriz) == 0:
        raise HTTPException(
            status_code = 400,
            detail="matriz vacia/invalida"
        )
    if not all(len(fila) == len(entrada.matriz[0]) for fila in entrada.matriz):
        raise HTTPException(
            status_code = 400,
            detail="matriz invalida(Filas de diferente tamaño)"
        )


def procesar_resolver(entrada: schemas.matriz_entrada): # no entiendoque queres q haga esta 
    validar_matriz(entrada)
    return entrada.matriz
