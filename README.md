# Hungarian Algorithm API

Proyecto personal desarrollado para aprender backend con FastAPI.

La aplicacion resuelve problemas de asignacion utilizando el algoritmo Hungaro. Recibe una matriz de costos mediante una API REST y devuelve el matching optimo junto con el costo minimo.

La resolucion del problema utiliza la implementacion del algoritmo Hungaro incluida en SciPy. El objetivo del proyecto es aprender desarrollo backend y construccion de APIs REST por lo que no se implemento manualmente el algoritmo.

## Tecnologias

* Python
* FastAPI
* Pydantic
* SciPy
* Pytest

## Estructura

```text
app/
├── algorithms.py
├── api.py
├── schemas.py
└── services.py

tests/
└── test_api.py


requirements.txt
README.md
```

### algorithms.py

Contiene la logica relacionada con el problema de asignacion. Utiliza SciPy para obtener el matching optimo e incluye funciones auxiliares desarrolladas durante el aprendizaje del algoritmo.

### api.py

Define los endpoints de la API. Recibe las peticiones HTTP llama a la capa de servicios y devuelve la respuesta al cliente.

### schemas.py

Define los modelos de entrada y salida mediante Pydantic. Estos modelos validan automaticamente los datos recibidos y documentan la API.

### services.py

Contiene la logica de validacion de la matriz antes de ejecutar el algoritmo.

### tests

Incluye pruebas automaticas con Pytest para verificar el funcionamiento de la API y los principales casos de error.

### main.py

Pequeño programa de ejemplo para ejecutar el algoritmo desde consola sin utilizar la API.

---

## Endpoint

### POST /resolver

Recibe un JSON con una matriz de costos.

Ejemplo de entrada

```json
{
  "matriz": [
    [4, 1, 3],
    [2, 0, 5],
    [3, 2, 2]
  ]
}
```

Ejemplo de respuesta

```json
{
  "matching": "a2, b1, c3",
  "min_sum": 5
}
```

---

## Ejecutar el proyecto

Instalar las dependencias

```bash
pip install -r requirements.txt
```

Iniciar la API

```bash
uvicorn app.api:app --reload
```

La documentacion interactiva estara disponible en

```
http://127.0.0.1:8000/docs
```

---

## Como usar

1. Ejecuta la API.

2. Abri en el navegador

```
http://127.0.0.1:8000/docs
```

3. Busca el endpoint **POST /resolver**.

4. Presiona **Try it out**.

5. Ingresa una matriz en formato JSON.

Ejemplo

```json
{
  "matriz": [
    [4, 1, 3],
    [2, 0, 5],
    [3, 2, 2]
  ]
}
```

6. Presiona **Execute**.

La API devolvera el matching optimo y el costo minimo.

```json
{
  "matching": "a2, b1, c3",
  "min_sum": 5
}
```

---

## Ejecutar los tests

```bash
python -m pytest -v
```
