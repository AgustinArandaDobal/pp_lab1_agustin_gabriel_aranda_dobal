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
    """ 1- Mostrar la lista de todos los jugadores del Dream Team.\n 2- Ingrese el indice numerico de alguno de los siguientes jugadores para recibir sus estadisticas completas: 1)Michael Jordan,2)Magic Johnson, 3)Larry Bird,4)Charles Barkley, 5)Scottie Pippen,6)David Robinson, 7)Patrick Ewing, 8)Karl Malone, 9)John Stockton, 10)Clyde Drexler, 11)Chris Mullin, 12)Christian Laettner.\n 3-  
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
def mostrar_jugador_segun_input(lista: dict[list]):
    """
    recibe una lista de jugadores, y muestra por print las estadisticas del jugador que requiera el usuario mediante su numero de indice. Retorna una lista con esta informacion.         
    """
    """
    incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples. 
    """
    respuesta = input("Ingrese el indice numerico de el jugador deseado: ")
    if re.match('^[1-9]$|^[1][0-2]$', respuesta):
        indice = int(respuesta) - 1
        jugador = lista[indice]
        datos_mostrados = []
        datos_mostrados.append({
             'nombre': jugador['nombre'],
             'jugador': jugador['posicion'],  
             'estadisticas': {
                    'temporadas': jugador['estadisticas']['temporadas'],
                    'puntos_totales': jugador['estadisticas']['puntos_totales'],
                    'promedio_puntos_por_partido': jugador['estadisticas']['promedio_puntos_por_partido'],
                    'rebotes_totales': jugador['estadisticas']['rebotes_totales'],
                    'promedio_rebotes_por_partido': jugador['estadisticas']['promedio_rebotes_por_partido'],
                    'asistencias_totales': jugador['estadisticas']['asistencias_totales'],
                    'promedio_asistencias_por_partido': jugador['estadisticas']['promedio_asistencias_por_partido'],
                    'robos_totales': jugador['estadisticas']['robos_totales'],
                    'bloqueos_totales': jugador['estadisticas']['bloqueos_totales'],
                    'porcentaje_tiros_de_campo': jugador['estadisticas']['porcentaje_tiros_de_campo'],
                    'porcentaje_tiros_libres': jugador['estadisticas']['porcentaje_tiros_libres'],
                    'porcentaje_tiros_triples': jugador['estadisticas']['porcentaje_tiros_triples']
                }
            })
                                
        mensaje = "{0}".format(json.dumps(datos_mostrados, indent= 4))
        print(mensaje)
        return datos_mostrados
    else:
        print("Solo hay 12 jugadores en el Dream team.")
    



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
                mostrar_jugador_segun_input(copia_lista_jugadores)
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