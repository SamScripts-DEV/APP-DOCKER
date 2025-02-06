import requests

# URL del balanceador de carga
LOAD_BALANCER_URL = "http://localhost"

# Número de solicitudes a realizar
NUM_REQUESTS = 100

# Diccionario para contar las respuestas de cada nodo
node_counts = {}

def test_load_balancer():
    for i in range(NUM_REQUESTS):
        try:
            # Realizar una solicitud GET al balanceador de carga
            response = requests.get(LOAD_BALANCER_URL)
            
            # Obtener el nombre del nodo desde la cabecera personalizada
            node = response.headers.get("X-Node-Name", "Unknown")
            
            # Contar las respuestas de cada nodo
            if node in node_counts:
                node_counts[node] += 1
            else:
                node_counts[node] = 1
            
            # Mostrar detalles de la respuesta
            print(f"Solicitud {i + 1}:")
            print(f"  Redirigido a: {node}")
            print(f"  Cabeceras: {response.headers}")
            print("-" * 40)
        except Exception as e:
            print(f"Error en la solicitud {i + 1}: {e}")

    # Mostrar los resultados
    print("\nResultados del balanceo de carga:")
    for node, count in node_counts.items():
        print(f"Nodo {node}: {count} solicitudes")

if __name__ == "__main__":
    test_load_balancer()