import requests
import json

BASE_URL = "http://localhost:8000/api/v1/usuarios"

def test_crud():
    print("--- 1. Creando usuario ---")
    user_data = {
        "nombre": "Test User",
        "email": "test@example.com",
        "edad": 25,
        "password": "password123"
    }
    response = requests.post(BASE_URL + "/", json=user_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code != 201:
        print("Error creando usuario")
        return

    user_id = response.json()["id"]

    print("\n--- 2. Obteniendo todos los usuarios ---")
    response = requests.get(BASE_URL + "/")
    print(f"Status: {response.status_code}")
    print(f"Count: {len(response.json())}")

    print(f"\n--- 3. Obteniendo usuario por ID ({user_id}) ---")
    response = requests.get(f"{BASE_URL}/{user_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    print("\n--- 4. Actualizando usuario ---")
    update_data = {
        "nombre": "Test User Updated",
        "edad": 30
    }
    response = requests.put(f"{BASE_URL}/{user_id}", json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    print("\n--- 5. Eliminando usuario ---")
    response = requests.delete(f"{BASE_URL}/{user_id}")
    print(f"Status: {response.status_code}")
    
    print("\n--- 6. Verificando eliminación ---")
    response = requests.get(f"{BASE_URL}/{user_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    try:
        test_crud()
    except Exception as e:
        print(f"Error de conexión: {e}. Asegúrate de que el servidor esté corriendo.")
