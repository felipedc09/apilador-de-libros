
from pila import Pila
from random import randrange, choice
from entidades import Libro
from utilidades import readFile

def main():
    libros = Pila()
    
    for datos in readFile('libros.csv'):
        libros.apilar(Libro(datos[0], datos[1], datos[2]))
    print(libros.items)
    print(len(libros.items))
    print(buscar(libros, 'Anna Llenas'))
    print(len(libros.items))


def buscar(libros, parametro):
    libroEncontrado = Libro
    librosTemp = []
    for libro in libros.items:
        if libro.titulo == parametro or libro.categoria == parametro or libro.autor == parametro:
            libroEncontrado = libro
            print('lo encontro')
            index = libros.items.index(libro)
            while len(libros.items) >= index:
               librosTemp.append(max(libros.items))
               libros.desapilar()
    librosTemp.pop()
    for libro in librosTemp:
        libros.apilar(libro)
    return libroEncontrado
        



if __name__ == '__main__':
    main()
