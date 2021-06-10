class Sabor:
    __numero=0
    __nombre=''
    __descripcion=''

    def __init__(self,numero=0,nombre='',descripcion=''):
        self.__numero=numero
        self.__nombre=nombre
        self.__descripcion=descripcion

    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def mostrar(self):
        print(f"{self.__numero},{self.__nombre},{self.__descripcion}")
        
    def __str__(self):
        return f"{self.__numero},{self.__nombre},{self.__descripcion}"
        