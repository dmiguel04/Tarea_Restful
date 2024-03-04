import requests
url="http://localhost:8000/"

# mostrar los estudiantes
ruta_estudiantes=url+"estudiantes"
lista_estudiantes=requests.request(method="GET",url=ruta_estudiantes)
print(lista_estudiantes.text,"\n")

# Agregar una ruta para mostrar las carreras
ruta_nombre=url+"carreras"
mostrar_carrera=requests.request(method="GET",url=ruta_nombre)
print(f"Todas las carreras: {mostrar_carrera.text}\n")

# Mostrar las carreras de Economia
ruta_economia=url+"carreras/Economia"
mostrar_carrera_economia=requests.request(method="GET",url=ruta_economia)
print(f"Todos los estudiante que estudian economia: {mostrar_carrera_economia.text}\n")

# Agrega a 2 estudiantes
ruta_post=url+"estudiantes"

nuevo_estudiante1={
    "nombre":"Pablo",
    "apellido":"Ticona",
    "carrera": "Economia",
}

nuevo_estudiante2={
    "nombre":"Alvaro",
    "apellido":"Hurtado",
    "carrera": "Economia",
}
requests.request(method="POST",url=ruta_post,json=nuevo_estudiante1)
post_response = requests.request(method="POST",url=ruta_post,json=nuevo_estudiante2)
print(post_response.text)