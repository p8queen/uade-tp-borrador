tupla = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
matriz = [] # como en gastos.csv
diccionario = {} # como en modelo-diccionario.json

def cargarDatos(archivo):
    with open(archivo) as data:
        primeraLinea = True
        for line in data:
            gastos = line.strip('\n').split(',')
            if not primeraLinea:
                gastos[1] = round(float(gastos[1]), 2) # redondea el importe
            else:
                primeraLinea = False
            gastos[2] = gastos[2].strip() # elimina espacios en blanco
            matriz.append(gastos)
        matriz.pop(0) # elimina cabecera


def generarMenu():
opcion=0
print("""
    Menú de opciones:
    1. Cargar nuevo gasto
    2. Ver gastos por mes
    3. Ver gastos por mes y categoría
    4. Ver gastos por categoría
    5. Ver lista de categorías
    6. Editar lista de categorías
    7. Editar gasto
    8. Eliminar gasto
    9. Salir""")

opcion=int(input('Ingrese la opción deseada: '))

while opcion!=9:
    if opcion==1:
        cargarNuevoGasto()
    elif opcion==2: 
        gastosPorMes()
    elif opcion==3:
        gastosPorMesCategoria()
    elif opcion==4:
        gastosPorCategoria()
    elif opcion==5:
        listaDeCategorias()
    elif opcion==6:
        editarListaDeCategorias()
    elif opcion==7:
        editarGasto()
    elif opcion==8:
        eliminarGasto()
    elif opcion==9:
        print(f'¡Gracias por elejirnos!\n')
    else:
        print('El valor ingresado no es un menú válido. Por favor ingrese nuevamente.')
        

def crearDiccionario():
    diccionario = {}
    # desarrolla pablo 
    # leer gastos.csv y crear como en modelo-diccionario.json
    return diccionario

def mostrarGastos(mes):
    # desarrolla gustavo
    pass

def gastosPorMes(mes):
    # desarrolla gustavo
    pass

def gastosPorCategoria(mes):
    # desarrolla gustavo
    pass

def gastosPorCategoria(categoria):
    # desarrolla gustavo
    # return lista de gastos
    pass

def gastosPorMesCategoria(mes, categoria):
    # desarrolla gustavo
    # return lista de gastos
    pass

def totalMes(mes):
    # desarrolla gustavo
    # return total de gastos
    pass

def totalMesCategoria(mes, categoria):
    # desarrolla gustavo
    # return total de gastos mes y categoria
    pass

def listaDeCategorias():
    # desarrolla gustavo
    categorias = [x[2] for x in matriz]
    return list(set(categorias)) # elimina duplicados
    
# CRUD Gastos
# crear, recuperar, actualizar, borrar


#MAIN

cargarDatos('gastos.csv')
for linea in matriz:
    print(linea)

