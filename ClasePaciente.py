import urllib, json
from urllib.request import urlopen

class Paciente():
    __nombre = ""
    __apellido = ""
    __telefono = 0
    __altura = 0
    __peso = 0

    def __init__(self, nombre, apellido, telefono, altura, peso):
        self.__nombre = self.requerido(nombre, "Se necesita el nombre")
        self.__apellido = self.requerido(apellido, "Se necesita el apellido")
        self.__telefono = self.requerido(telefono, "Se necesita el telefono")
        self.__altura = self.requerido(altura, "Se necesita la altura")
        self.__peso = self.requerido(peso, "Se necesita el peso")

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    def getIMC(self):
        return self.__peso / (self.__altura * 2)
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.__nombre,
                apellido = self.__apellido,
                altura = self.__altura,
                peso = self.__peso,
            )
        )
        return d