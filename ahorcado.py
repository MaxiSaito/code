#JUEGO DEL AHORCADO
#by Maximiliano Saito
#El usuario ingresa la dificultad(que hace variar la longitud de la palabra), se genera un numero random que se utiliza para traer la palabra de la lista
#Por defecto son 7 intentos para adivinar la palabra

import random
import os


facil = ['arena','arbol','vacio','lapiz','gorra','pincel','imagen','sonido','flauta','mesa']
medio = ['libertad','teclado','avioneta','lenguaje','telefono','heladera','impresora','universo','salida','felino']
dificil = ['astronauta','madagascar','infraestructura','computadora','programacion','lenguaje','constelacion','aeroplano','aislamiento','interpretacion']


def lista(dif):
    """
    Genera un numero random del 0 al 9 y retorna una palabra de la lista segun la dificultad
    """
    num=random.randint(0,9)
    if dif == 1:
        return facil[num]
    elif dif == 2:
        return medio[num]
    elif dif == 3:
        return dificil[num]
    
def hombre(intento):
    """
    Imprime por pantalla el stickman dependiendo del parametro dado
    """
    if intento == 0:
        print('___________\n|\n|\n|\n|')
    elif intento == 1:
        print('___________\n|\n|      (o.o)\n|\n|')
    elif intento == 2:
        print('___________\n|\n|      (o.o)\n|       ( ) \n|')
    elif intento == 3:
        print('___________\n|\n|      (o.o)\n|      /( )\n|')
    elif intento == 4:
        print('___________\n|\n|      (u.u)\n|      /( )\ \n|')
    elif intento == 5:
        print('___________\n|\n|      (T.T)\n|      /( )\ \n|       /')
    elif intento == 6:
        print('___________\n|\n|      (T.T)\n|      /( )\ \n|       / \ ')
    elif intento == 7:
        print('___________\n|        |\n|      (x_x)\n|      /( )\ \n|       / \ ')

def control(word,vacio,letra):
    """
    Recibe la lista con los caracteres de la palabra, la lista vacia con la misma cantidad de "_", y la letra a buscar
    """
    y = "" #defino la string que me muestra mi progreso
    global intentos 
    global flag
    flag = 0 #reinicio de bandera
    for x in range(len(word)): #recorro la palabra en busca de coincidencias y si las encuentra reemplaza ese caracter en la lista "vacio"
        if letra.lower() == word[x]:
            vacio[x]=letra.lower()
            flag = 1
    for x in vacio: #pasa los caracteres de la  lista "vacio" a la string para imprimirla
        y += x
    if list(y)==word: #Si el contenido de "vacio" es igual a la palabra. Condicion de victoria
        flag = 3
    elif flag == 1: #cuando se encuentra una coincidencia
        print('Bien!')    
        print(y)
    else:           #cuando no se encuentra una coincidencia
        print('Incorrecto...')
        print(y)
        intentos+=1


def juego():
    """
    Bucle central donde sucede la magia
    """
    vacio = [] 
    print('**** Juego del Ahorcado ****')
    while True:
        try:
            print('Seleccione una dificultad! \n1. Facil\n2. Medio\n3. Dificil')
            x = int(input('>'))
            if x>0 and x<4:
                break
            os.system('cls')
            print('Opcion invalida. Ingrese nuevamente')
        except:
            os.system('cls')
            print('Opcion invalida. Ingrese nuevamente')
    palabra = lista(x)    #llamo a la funcion que me trae una palabra aleatoria de la lista dependiendod de la difucultad
    word = list(palabra)   #convierto la palabra en una lista que contiene todos los caracteres por separados
    for x in range(len(word)): #relleno la lista "vacio" de "_" con la cantidad de caracteres que tiene la palabra a adivinar
        vacio.append('_')
    largo=len(palabra)  #guardo el largo de la palabra para mostrarlo como ayuda 
    os.system('cls')  #limpio pantalla
    while True:
        print(f'\nLa palabra tiene {largo} letras') #muestro la ayuda
        hombre(intentos)    #imprimo al stickman dependiendo de los intentos fallidos que llevo
        letra = input('\nIngrese Letra: ')
        os.system('cls')
        control(word,vacio,letra) #llamo a la funcion de control
        if intentos == 7: #condicion derrota
            os.system('cls')
            print('Perdiste!! :C')
            print(f'La palabra era -> {palabra}')
            hombre(intentos)
            break
        if flag==3: #condicion victoria
            os.system('cls')
            print(palabra)
            print('Ganaste!! C:\n___________\n|        ❤\n|      (OuO)\n|      \( )/ \n|       / \ ') 
            break
        
        
seguir='s'
intentos=0
flag=0
while seguir.lower()=='si' or seguir.lower()=='s':
    juego()
    print('\nDesea seguir jugando? si/no')
    seguir = input('>')
    intentos = 0 #reinicio los intentos a 0
    while seguir.lower()!='si' and seguir.lower()!='s' and seguir.lower()!='no' and seguir.lower()!='n':
        print('Opcion invalida.')
        seguir = input('>')
    if seguir.lower()=='no' or seguir.lower()=='n':
        break