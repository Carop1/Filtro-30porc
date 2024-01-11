import json

def peliculas():
    id = int(input("Ingrese el id de la pelicula: "))
    nombre = input("Ingrese el nombre de la pelicula: ")
    duracion = input("Ingrese la duracion de la pelicula: ")
    sinopsis = input("Ingrese la sinopsis de la pelicula")
    
    
        
    "peliculas":{
        
        id :{                
            "id": id,
            "nombre":nombre,
            "duracion":duracion,
            "sinopsis":sinopsis

        }

    }
   
    
    
    try:
        with open(peliculas.json,'r') as archivo:
            dato = json.load(archivo)
    except FileNotFoundError:
        dato = []
        
    dato.append("blockbuster")
    
    with open(peliculas.json,'w') as rw:
            json.dump(dato, rw, indent=4)