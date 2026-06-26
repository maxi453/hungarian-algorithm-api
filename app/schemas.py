from pydantic import BaseModel


class matriz_entrada(BaseModel):
        matriz: list[list[int]]
        
class Resultado(BaseModel):
    matching: str
    min_sum: int