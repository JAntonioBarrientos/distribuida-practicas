import queue


grafica = {
  'A' : ['B','C', 'D', 'E'],
  'B' : ['A', 'C', 'G'],
  'C' : ['A', 'B', 'D'],
  'D' : ['H', 'E', 'A', 'C'],
  'E' : ['A', 'D', 'F'],
  'F' : ['G', 'E', 'H', 'I'],
  'G' : ['F', 'B'],
  'H' : ['F', 'D'],
  'I' : ['F']
}  

def bfs(grafica, nodo_inicio):
    """
    Realiza un recorrido de Búsqueda en Amplitud (BFS) en un grafica.

    Args:
        grafica (dict): Un diccionario que representa el grafica. 
        nodo_inicio (str): El nodo desde el cual comenzará el recorrido.

    Returns:
        list: Una lista de nodos en el orden en que fueron visitados.
    """
    # Usamos un conjunto (set) para la comprobación de si un nodo ya fue
    # visitado sea  eficiente (tiempo O(1) en promedio).
    visitados = set()

    # Empezamos la cola con el nodo de inicio.
    cola = queue.Queue()
    cola.put(nodo_inicio)

    # 'orden_visita' es la lista que almacenará el resultado final
    orden_visita = []

    visitados.add(nodo_inicio)

    while not cola.empty():
        # Se saca el primer nodo de la cola (el más antiguo). lo que
        # es la clave del bfs para el FIFO (First-In, First-Out)
        nodo_actual = cola.get()
        orden_visita.append(nodo_actual)

        for vecino in grafica[nodo_actual]:
            # Si un vecino no ha sido visitado, se procesa.
            if vecino not in visitados:
                # Se marca como visitado para no volver a procesarlo.
                visitados.add(vecino)
                # Se añade a la cola para visitar a sus propios vecinos más tarde.
                cola.put(vecino)
    
    return orden_visita


# Se llama a la función bfs para iniciar el recorrido desde el nodo 'A'.
recorrido_bfs = bfs(grafica, 'A')

print("El recorrido BFS desde el nodo 'A' es:")
print(recorrido_bfs)

# Ejemplo para el punto extra: iniciar desde otro nodo
recorrido_desde_F = bfs(grafica, 'F')
print("\nEjemplo (Punto extra): Recorrido BFS desde el nodo 'F':")
print(recorrido_desde_F)




import collections

def leer_grafica_desde_archivo(nombre_archivo):
    grafica = collections.defaultdict(list)
    
    try:
        with open(nombre_archivo, 'r') as archivo:

            linea_nodos = next(archivo).strip()
            for nodo in linea_nodos.split(','):
                grafica[nodo]
            for linea in archivo:
                linea = linea.strip()
                if not linea: 
                    continue

                # Usamos un bloque try-except para manejar líneas mal escritas.
                try:
                    nodo1, nodo2 = linea.split(',')
                    grafica[nodo1].append(nodo2)
                    grafica[nodo2].append(nodo1)
                except ValueError:
                    print(f"Advertencia: Se omitió la línea con formato incorrecto: '{linea}'")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return None
    
    return dict(grafica)

# --- Ejemplo de uso ---
# Tener el archivo 'input.txt' en la misma carpeta.
grafica_leida = leer_grafica_desde_archivo('input.txt')

if grafica_leida:
    print("Grafica leída exitosamente")
    print(grafica_leida)

