import json
import re
import csv
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
    """ 1- Mostrar la lista de todos los jugadores del Dream Team.\n 2- Ingrese el indice numerico de alguno de los siguientes jugadores para recibir sus estadisticas completas: 1)Michael Jordan,2)Magic Johnson, 3)Larry Bird,4)Charles Barkley, 5)Scottie Pippen,6)David Robinson, 7)Patrick Ewing, 8)Karl Malone, 9)John Stockton, 10)Clyde Drexler, 11)Chris Mullin, 12)Christian Laettner. Si desea guardar dichas estadisticas seleccione si luego.\n 3- Ingrese el nombre de algun jugador del Dream Team para ver todos sus logros. \n 4- Mostrar al Dream Team con el promedio de puntos por partidos ordenados alfabeticamente \n 5- Ingrese el nombre de un jugador del Dream Team para saber si forma parte del salon de la fama. \n 6- Mostrar el jugador con la mayor cantidad de rebotes totales. \n 7-Mostrar el jugador con el mayor porcentaje de tiros de campo. \n 8- Mostrar el jugador con la mayor cantidad de asistencias totales.
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
    recibe una lista de jugadores, el usuario ingresa por input el indice del jugador a buscar, y muestra la siguiente info: temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples. Se le da la opcion al usuario de guardar la info en un archivo csv 
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
        guardar_datos = input("Desea guardar las estadisticas de este jugador en un archivo csv? si/no")
        if guardar_datos.lower() == "si":
            guardar_archivo_csv(datos_mostrados, jugador['nombre'],jugador)
        elif guardar_datos.lower() == "no":
            print("NO se ha guardado ningun archivo")
        else:
            print("Por favor ingrese las opciones si o no.")
    else:
        print("Solo hay 12 jugadores en el Dream team.")
    

def guardar_archivo_csv(lista:list, nombre_archivo:str,jugador:dict):
    """
    Se guarda un archivo CSV con el nombre, la posicion y las estadisticas del jugador. Cada vez que se crea un archivo con el mismo nombre se sobreescribe el anterior.
    """
    nombre_archivo = ''.join([nombre_archivo, '.csv'])
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(['Nombre', 'Posición', 'temporadas', 'puntos totales','promedio puntos por partido', 'rebotes totales', 'promedio rebotes por partido', 'asistencias totales', 'promedio asistencias por partido', ' robos totales', 'bloqueos totales', 'porcentaje tiros de campo','porcentaje tiros libres', 'porcentaje tiros triples'])  # Encabezados
            writer.writerow([jugador['nombre'], jugador['posicion'], jugador["estadisticas"]['temporadas'], jugador["estadisticas"]['puntos_totales'],jugador['estadisticas']['promedio_puntos_por_partido'],jugador['estadisticas']['rebotes_totales'], jugador['estadisticas']['promedio_rebotes_por_partido'], jugador['estadisticas']['asistencias_totales'], jugador['estadisticas']['promedio_asistencias_por_partido'], jugador['estadisticas']['robos_totales'],jugador['estadisticas']['bloqueos_totales'], jugador['estadisticas']['porcentaje_tiros_de_campo'], jugador['estadisticas']['porcentaje_tiros_libres'], jugador['estadisticas']['porcentaje_tiros_triples']])

    print("Estadísticas guardadas en el archivo CSV correctamente.")

def buscar_jugadores_por_nombre(lista: list):
    nombre_buscar = input("Ingrese el nombre del jugador que desea buscar: ").lower()
    
    encontrados = []
    
    for jugador in lista:
        jugador_validado =jugador['nombre']
        jugador_validado = jugador_validado.lower()

        if re.search(nombre_buscar, jugador_validado): 
            #re.IGNORECASE para no usar jugador_validado
            encontrados.append(jugador)
    
    if encontrados:
        print("Se encontraron {0} jugador(es) que coinciden con la búsqueda:".format(len(encontrados)))
        for jugador in encontrados:
            print("Nombre:{0} ".format(jugador['nombre']))
            print("Logros:{0}".format(jugador['logros']))
    else:
        print("No hay coincidencias con el nombre ingresado")

def quicksort(lista:list, ascendente: bool = True)->list:
    """
    Se le pasa como parametro la lista, si la lista tiene un solo elemento o esta vacia la retorna como esta, y si no utilizando tres listas vacias va guardando los diferentes resultados de las comparaciones y al final retorna  las listas de manera que queden ordenadas de manera ascendente o descendente segun se requiera.
    """
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]
    menor = []
    igual = []
    mayor = []

    for jugador in lista:
        if (jugador < pivot and ascendente) or (jugador > pivot and not ascendente):
            menor.append(jugador)
        elif jugador == pivot:
            igual.append(jugador)
        else:
            mayor.append(jugador)
    return quicksort(menor, ascendente) + igual + quicksort(mayor, ascendente)

def mostrar_nombres_ordenados_ascendente(lista:list,):
    """
    Guarda los nombres en una lista, para luegos ordenarlos de manera alfabetica con la funcion quicksort, y compara los nombres guardados con la lista que contiene todos los datos para que cuando haya una coincidencia le asigne el promedio correspondiente a ese jugador.
    """
    nombres = []
    for jugador in lista:
        nombres.append(jugador['nombre'])
    nombres_ordenados = quicksort(nombres)
    for nombre in nombres_ordenados:
        for jugador in lista:
            if jugador['nombre'] == nombre:
                promedio = jugador['estadisticas']['promedio_puntos_por_partido']
                print("Nombre: {0}, Promedio: {1}".format(nombre,promedio))
                break
def verificar_logro_salon_fama(lista:list):
    jugador_nombre = input("Ingrese el nombre del jugador:").lower()
    for jugador in lista:
        if jugador['nombre'].lower() == jugador_nombre:
            if "Miembro del Salon de la Fama del Baloncesto" in  jugador['logros']:
                print("El jugador ingresado es miembro del salon de la fama")
            else:
                print("El jugador no es miembro del salon de la fama")
    else:
            print("!!!!!! ESE NOMBRE NO CORRESPONDE A UNO ASOCIADO AL DREAM TEAM !!!!!")
            print("Por favor ingrese el nombre de algun jugador del Dream Team: Michael Jordan,Magic Johnson, Larry Bird,Charles Barkley, Scottie Pippen,David Robinson, Patrick Ewing, Karl Malone, John Stockton, Clyde Drexler, Chris Mullin, Christian Laettner")

def calcular_max(lista:list, clave:str):
    max = 0
    jugador_max = None
    for jugador in lista:
        valor = float(jugador['estadisticas'][clave])
        if valor > max:
            max = valor
            jugador_max = jugador['nombre']
    if jugador_max is None:
        print("No hay datos disponibles.")
    else:
        print("El jugador con la mayor cantidad de {0}, es {1}".format(clave.replace("_"," "), jugador_max))
        print("Cantidad de {0}: {1}".format(clave.replace("_"," "),max))

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
                buscar_jugadores_por_nombre(copia_lista_jugadores)
            case 4:
                mostrar_nombres_ordenados_ascendente(copia_lista_jugadores)
            case 5:
                verificar_logro_salon_fama(copia_lista_jugadores)
            case 6:
                calcular_max(copia_lista_jugadores, 'rebotes_totales')
            case 7:
                calcular_max(copia_lista_jugadores, "porcentaje_tiros_de_campo")
            case 8:
                calcular_max(copia_lista_jugadores, "asistencias_totales")
            case 22:
                print("Gracias por utilizar la aplicación, hasta la proxima")
                break
            case _:
                print("Opcion ingresda invalida.")


aplicacion_menu_parcial(copia_lista_jugadores)