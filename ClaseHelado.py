from ClaseSabor import Sabor

class Helado:
    __gramos=0
    __sabores=[]
   
    def __init__(self,gramos=0,sabor=None):
        self.__gramos=gramos
        self.__sabores=[]
        if sabor!=None:
            self.addSabor(sabor)
            self.__cant=len(sabor)

    def getSabor(self):
        return self.__sabores        
    def addSabor(self,sabor):
          for i in range(len(sabor)):
            self.__sabores.append(sabor[i])
        
    def getGramos(self):
        return self.__gramos
    def cargarSabor(self,sabor):
        self.__sabores.append(sabor)
    def __str__(self):
        unSabor=Sabor()
        s="----Datos de la instancia de Helado----\n"
        s+=f'''Los gramos son: {self.__gramos}'''      
        d='\nSabores\n'
        
        for unSabor in self.__sabores:
           d+=unSabor.__str__()
        s+=d
        return s