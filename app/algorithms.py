from scipy.optimize import linear_sum_assignment


def restar_filas(matriz):
    matriz_res = [] 
    
    for fila in matriz:
        new_fila = []
        #el minimo de la fila 
        minum = min(fila)
        for x in fila:
            #a cada x de la fila le resto el minimo
            new_fila.append(x-minum)    
        #antes de cambiar de fila guardo 
        matriz_res.append(new_fila)
        
    return matriz_res


def restar_columna(matriz):
    matriz1 = transponer(matriz)
    matriz2 = restar_filas(matriz1)
    matriz_res = transponer(matriz2)
    return matriz_res


def transponer(matriz):
    mantriz_trans= []
    for j in range(len(matriz[0])): 
        new_fila = []
        for fila in matriz:
            new_fila.append(fila[j])
        mantriz_trans.append(new_fila)    
    return mantriz_trans


def es_cuadrada(matriz):
    b = len(matriz) == len(matriz[0])
    return b 

    
def costo(matriz,fila,column):
    costo = 0
    for k in range(len(fila)):
            costo = costo + matriz[fila[k]][column[k]]
    return costo

           
def formatear_matching(filas, columnas):
    # Lista fija bien larga para que aguante matrices grandes sin problemas
    letras = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    matching_lista = []
    for f, c in zip(filas, columnas):
        letra_fila = letras[f]
        num_columna = c + 1
        matching_lista.append(f"{letra_fila}{num_columna}")
    return ", ".join(matching_lista)


def hungaro_resolver(matriz):
    # resuelve el problema de asignacion optima utilizando
    # una implementación del algoritmo hungaro provista por SciPy.
    # Devuelve dos listas:
    # filas[i] esta asignada a columnas[i]
    filas, columnas = linear_sum_assignment(matriz)

    min_suma = costo(matriz, filas, columnas)
    
    matching = formatear_matching(filas, columnas)
    
    return matching, min_suma