class Libro:
    def __init__(self, paginas, tapa,nombre, autor, genero, isbn):
        self.paginas = paginas
        self.tapa = tapa
        self.nombre= nombre
        self.autor = autor
        self.genero = genero
        self.isbn = isbn

    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_paginas(self,paginas):
        self.paginas = paginas

    def set_tapa(self,tapa):
        self.tapa = tapa

    def set_autor(self,autor):
        self.autor = autor
    
    def set_genero(self,genero):
        self.genero = genero

    def set_isbn(self,isbn):
        self.isbn = isbn
    
    