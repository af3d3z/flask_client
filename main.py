import requests
import json

from requests import delete

from Editorial import Editorial
from Libro import Libro

API_URL = "localhost:3000/api/"

def getEditorial():
    id = int(input("Introduce el id: "))
    response = requests.get(API_URL + "/editoriales/" + str(id))
    j = json.loads(response)
    editorial = Editorial(**j)
    return editorial

def postEditorial():
    editorial = nuevaEditorial()
    response = requests.post(API_URL + "/editoriales", json=json.dump(editorial))
    if response.status_code == 200 or response.status_code == 201:
        print("Se ha añadido la editorial correctamente")
    else:
        print("Se ha producido un error al intentar agregar la editorial")

def putEditorial():
    editorial = nuevaEditorial()
    response = requests.put(API_URL + "/editoriales", json=editorial)
    if response.status_code == 200:
        print("Se ha modificado correctamente")
    else:
        print("No se ha podido modificar.")

def deleteEditorial():
    id = int(input("Introduce el id: "))
    response = requests.delete(API_URL + "/editoriales/" + str(id))
    if response.status_code == 200:
        print("Se ha borrado correctamente")
    else:
        print("No se ha podido borrar la editorial")

def nuevaEditorial():
    id = input("Introduzca el id de la editorial: ")
    cif = input("Introduzca el cif de la editorial: ")
    razon = input("Introduzca la razón social de la editorial: ")
    web = input("Introduzca la web de la editorial: ")
    tlf = input("Introduzca el número de teléfono de la editorial: ")
    correo = input("Introduzca el correo electrónico de la editorial: ")
    direccion = input("Introduzca la dirección: ")

    return Editorial(id, cif, razon, direccion, web, correo, tlf)

def getLibro():
    id = int(input("Introduce el id: "))
    response = requests.get(API_URL + "/libros/" + str(id))
    j = json.loads(response)
    libro = Libro(**j)
    return libro

def postLibro():
    libro = nuevoLibro()
    response = requests.post(API_URL + "/libros", json=json.dump(libro))
    if response.status_code == 200 or response.status_code == 201:
        print("Se ha añadido el libro correctamente")
    else:
        print("Se ha producido un error al intentar agregar el libro")

def putLibro():
    libro = nuevoLibro()
    response = requests.put(API_URL + "/libros", json=libro)
    if response.status_code == 200:
        print("Se ha modificado correctamente")
    else:
        print("No se ha podido modificar.")

def deleteLibro():
    id = int(input("Introduce el id: "))
    response = requests.delete(API_URL + "/libros/" + str(id))
    if response.status_code == 200:
        print("Se ha borrado correctamente")
    else:
        print("No se ha podido borrar el libro")

def nuevoLibro():
    id = int(input("Introduce el id del libro: "))
    precio = float(input("Introduce el precio del libro: "))
    isbn = input("Introduce el ISBN: ")
    titulo = input("Introduce el título del libro: ")
    numpag = int(input("Introduce el número de páginas: "))
    tematica = input("Introduce la temática: ")
    id_editorial = int(input("Introduce el id de la editorial: "))
    return Libro(id=id, precio=precio, isbn=isbn, titulo=titulo, numpag=numpag, tematica=tematica, id_editorial=id_editorial)

def mostrar_menu():
    print("MENU:")
    print("Editoriales: ")
    print("\t1. Consultar una editorial.")
    print("\t2. Añadir una editorial.")
    print("\t3. Editar una editorial.")
    print("\t4. Borrar una editorial.")
    print("Libros: ")
    print("\t5. Consultar un libro.")
    print("\t6. Añadir un libro.")
    print("\t7. Editar un libro.")
    print("\t8. Borrar un libro.")
    print("0. Salir")
    opcion = int(input("Introduce la opción: "))
    return opcion

def main():
    opcion = mostrar_menu()
    while opcion != 0:
        match opcion:
            case 1: getEditorial()
            case 2: postEditorial()
            case 3: putEditorial()
            case 4: deleteEditorial()
            case 5: getLibro()
            case 6: postLibro()
            case 7: putLibro()
            case 8: deleteLibro()
            case 0: pass

        opcion = mostrar_menu()




if __name__ == '__main__':
    main()