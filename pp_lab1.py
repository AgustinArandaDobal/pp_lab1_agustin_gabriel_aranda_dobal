import json
import re
PATH_ARCHIVO = r'C:\Users\Programación\Desktop\primer_parcial_laboratorio_01\dt.json'

def leer_archivo(path_completo: str) -> list[dict]:
    """
    Recibe la dirección del archivo JSON.
    Utiliza la declaración with para manejar la apertura y el cierre del archivo.
    Retorna una lista de diccionarios con el contenido de la clave "heroes".
    """
    with open(path_completo, "r") as archivo:
        datos_json = json.load(archivo) 
        lista = datos_json["jugadores"]

    return [dict(data) for data in lista]

lista_jugadores = leer_archivo(PATH_ARCHIVO)

copia_lista_jugadores = lista_jugadores.copy()
# print(json.dumps(lista_heroes, indent=4))


def imprimir_dato(cadena: str) -> str:
    """
    Toma un string y lo imprime mediante un print.
    no retorna nada
    """
    print(cadena)
def imprimir_menu_parcial() -> str:
    """
    Lista de opciones a elegir en el menu, a su vez utiliza la funcion imprimir_dato para mostrarlo por consola
    """
    opciones_menu =\
    """
    1- Mostrar la lista de todos los jugadores del Dream Team
    
    """
    imprimir_dato(opciones_menu)

def menu_validado_parcial()->int:
    """
    recibe un str mediante un input que representa la opcion a elegir en el menu de la app
    valida la opcion elegida y en caso de que el usuario ingrese mal un dato retorna -1
    """
    imprimir_menu_parcial()

    respuesta = input("Ingrese una opcion: ")
    if re.match('^[1-9]$|^[1-2][0-9]$', respuesta):
        return int(respuesta)
    return -1

def mostrar_lista_completa_jugadores(lista: dict[list]):
    """
    Muestra la lista de todos los jugadores del Dream Team con el formato Nombre Jugador - Posición.
    No retorna nada.
    """
    for jugador in lista:
        nombre = jugador['nombre']
        posicion = jugador['posicion']
        mensaje = "{0} - {1}".format(nombre, posicion)
        print(mensaje)

def aplicacion_menu_parcial(lista: list[dict]):
    """
    Esta funcion recibe una lista de diccionarios por parametro, y mediante la funcion menu_validado_parcial ejecuta el case del match correspondiente
    
    """
    while True:

        respuesta = menu_validado_parcial()

        match respuesta:
            case 1:
                mostrar_lista_completa_jugadores(copia_lista_jugadores)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 22:
                print("Gracias por utilizar la aplicación, hasta la proxima")
                break
            case _:
                print("Opcion ingresda invalida.")


aplicacion_menu_parcial(copia_lista_jugadores)