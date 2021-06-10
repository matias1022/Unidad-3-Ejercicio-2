from ClaseSabor import Sabor
import csv

class ManejadorSabor:
    __lista=[]


    def agregar(self,unSabor):
        self.__lista.append(unSabor)
   
    def cargar(self):
        numero=0
        archivo = open('sabores.csv')
        leer = csv.reader(archivo,delimiter=',')
        for fila in leer:
            numero=numero+1
            nombre=fila[0]
            descripcion=fila[1]

            unSabor = Sabor(numero,nombre,descripcion)
            self.agregar(unSabor)
        archivo.close()
    def agregarLista(self,listaSabores,sabor ):
        unSabor=Sabor()      
        for unSabor in self.__lista:
            if unSabor.getNumero()==sabor:
                         listaSabores.append(sabor)   
    def devolverSabor(self,unSabor):      
            return self.__lista[unSabor]
    def __str__(self):
        s=''
        unSabor=Sabor()     
        for unSabor in self.__lista:
               s+=unSabor.__str__() + '\n'
        return s
    def mostrarListaSabores(self):
        unSabor=Sabor()
        for unSabor in self.__lista:
            print (unSabor)
    def mostrarSabor(self,sabor):
        i=0
        band=True
        saborElegido=""
        unSabor=Sabor()
        while band==True and i <len(self.__lista):
            if self.__lista[i].getNumero()==sabor:
                band=False
                saborElegido=self.__lista[i].getNombre()
            i=i+1
        return saborElegido

    def retornaLista(self):
        return self.__lista
    def getListaNumeroSabores(self):
        listaNumeroSabores=[]
        for unSabor in self.__lista:
            listaNumeroSabores.append(unSabor.getNumero())
        return listaNumeroSabores
    def getListaSabores(self):
        sabores = {}
        for unSabor in self.__lista:
            sabores[unSabor.getNombre()] = 0
        return sabores
