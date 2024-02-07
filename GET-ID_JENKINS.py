import requests

def obtener_ultimo_id_de_ejecucion(job_url, username, password):
    # Construir la URL para la última ejecución en Jenkins
    last_build_url = f"{job_url}/lastBuild/api/json"
    
    # Realizar la solicitud GET con autenticación básica
    response = requests.get(last_build_url, auth=(username, password))
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener el ID de la última ejecución
        last_build_id = response.json()["id"]
        return last_build_id
    else:
        print(f"Error al obtener el ID de la última ejecución del job en {job_url}")
        return None

# Ejemplo de uso
job_url = "http://9.18.77.59:8080/view/RAS_68/job/GET-accessors%20__RAS_68"
username = "TU_USUARIO"
password = "TU_CONTRASEÑA"

last_build_id = obtener_ultimo_id_de_ejecucion(job_url, username, password)
if last_build_id:
    print(f"ID de la última ejecución del job: {last_build_id}")
