

import json

def genero():
    id = int(input("Ingrese el id del genero de la pelicula: "))
    nombre = input("Ingrese el nombre de la pelicula: ")
    
    id :{
    
    "id": id,
    "nombre":nombre

}
         
    try:
        with open(generos.json,'r') as archivo:
            dato = json.load(archivo)
    except FileNotFoundError:
        dato = []
        
    dato.append("id")
    
    with open(generos.json,'w') as rw:
            json.dump(dato, rw, indent=4)