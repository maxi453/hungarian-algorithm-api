from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)#le paso la matriz? la fun resolver?

def test_matriz_valida():
    #genero una matriz de ejemplo 
    #sirve como el ejemplo de lo q mandaria el usuario 
    datos = {
        "matriz":[
            [12,8,9],
            [24,9,10],
            [25,14,1]
        ]
    }
    
    #simulo la peticion del cliente 
    #cliente llama a resolver y pasaa un json con los datos de arriba
    respuesta = client.post(
        "/resolver",
        json = datos
    )
    #aca es donde esta la logica de verificacion del tests
    #primero verifico q el resultado de llamar a "/resolver" tenga codigo 200
    assert respuesta.status_code == 200
    #en respuesta.json() esta el resultado de llamar a resolver
    cuerpo = respuesta.json()
    #verifico q estos 2 campos esten en cuerpo
    assert "matching" in cuerpo
    assert "min_sum" in cuerpo


def test_matriz_vacia():
    #tendra q verificar q de codigo de error 400 y ademas del mensaje de error
    datos = {
        "matriz":[]
    }
    
    respuesta = client.post(
        "/resolver",
        json = datos
        )
    assert respuesta.status_code == 400
    
    cuerpo = respuesta.json()
    
    assert "detail" in cuerpo
    
    assert not "matching" in cuerpo
    assert not "min_sum" in cuerpo
    
    
def test_matriz_dispareja():
    
    datos = {
        "matriz":[
            [12,5,1,7],
            [12,6,7,9,64],
            [13,1]
        ]
    }
    
    respuesta = client.post(
        "/resolver",
        json = datos
        )
    assert respuesta.status_code == 400
    
    cuerpo = respuesta.json()
    
    assert "detail" in cuerpo
    
    assert not "matching" in cuerpo
    assert not "min_sum" in cuerpo
    

def test_matriz_negativa():

    datos = {
        "matriz":[
            [1,8,-4],
            [14,-9,1],
            [-25,14,1]
        ]
    }
    

    respuesta = client.post(
        "/resolver",
        json = datos
    )

    assert respuesta.status_code == 200

    cuerpo = respuesta.json()

    assert "matching" in cuerpo
    assert "min_sum" in cuerpo