#librerias para escoger una palabra random y para limpiar pantalla
import random
import os

#diccionario con los dibujos del ahorcado
pics = { 
'9': " ",
'8': '''=========''',
'7': '''
      |
      |
      |
      |
      |
=========''',
'6': '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'5':'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'4':'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'3':'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'2':'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'1':'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
'0':'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''}

#diccionario con temas a escoger
topics = {
    '1': 'colores',
    '2': 'marcas de autos',
    '3': 'futbolistas',
    '4': 'paises'
}

#imprime el menu de temas y retorna el valor ingresado
def menu():
    print('BIENVENIDO AL JUEGO DEL AHORCADO')
    for number, topic in topics.items():
        print(number + ": " + topic)
    topic = int(input('Escoge un tema: '))
    return topic

# consume a menu y según el valor ingresado abre el archivo correspondiente
def read():
    topic = menu()
    assert 1 <= topic <= 4, "opcion invalida"
    words = []
    if topic == 1:
        with open("./colores.txt.","r",encoding="utf-8") as f:
            words = [linea.rstrip() for linea in f]
        f.close()
    elif topic == 2:
        with open("./marcas_autos.txt.","r",encoding="utf-8") as f:
            words = [linea.rstrip() for linea in f]
        f.close()
    elif topic == 3:
        with open("./futbolistas.txt.","r",encoding="utf-8") as f:
            words = [linea.rstrip() for linea in f]
        f.close()
    else :
        with open("./paises.txt.","r",encoding="utf-8") as f:
            words = [linea.rstrip() for linea in f]
        f.close()
    #print(words)
    return random.choice(words)

#crea un string de guiones(-) para dar apoyo visual al usuario
def length(word):
    unknown = '-'
    for letter in enumerate(word):
        unknown +='-'
    unknown=unknown[:-1]
    return unknown

#función de adivinar, usa control de vidas
def guessing(word,unknown, found = False):
    #limpia pantalla
    lifes = 9
    letters = []
    while unknown != word and lifes > 0:
        os.system("cls")
        print(f'{unknown} es diferente de {word}')
        found = False
        print('JUEGO DEL AHORCADO')
        print('letras usadas: ',letters)
        print(unknown)
        print('vidas restantes: ',lifes)
        #recorre el diccionario para dibujar el ahorcado
        for life, pic in pics.items():
            if int(life) == lifes:
                print(pic)
                break
        letter=input('Ingresa Una letra:')
        #valida que se haya ingresado algo correcto
        assert len(letter) >0, "No se ha ingresado letra"
        for i in range(len(word)):
            if word[i]==letter:
                found = True
                unknown = list(unknown)
                unknown[i]=letter
                unknown = "".join(unknown)
        if not letter in letters:
            letters.append(letter)
        if not found:
            lifes -= 1
        if lifes == 0:
            os.system("cls")
            print(pics.get('0'))
            return 'PERDISTE, la palabra era ' + word
    return 'GANASTE, la palabra era '+ word

def run():
    word = read()
    #print(word)
    unknown = length(word)
    print(guessing(word,unknown))
    
if __name__=='__main__':
    run()