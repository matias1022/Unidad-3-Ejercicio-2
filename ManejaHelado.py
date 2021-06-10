from ClaseSabor import Sabor
from ClaseHelado import Helado
from ManejaSabor import ManejadorSabor
import operator
class ManejadorHelado:
    __lista=[]

    def cargarPeso(self,gramos):
         assert isinstance(gramos,int)
         self.__lista.append(gramos)
         print ("Hola")

    def cargarSabores(self,sabores):
         helado=Helado()
         helado.cargarSabor(sabores)

    def cargarVentas(self,listaSaboresDisponibles):
                    print ("Ingresar los datos de el Helado vendido")
                    peso=int(input("Peso(100gr, 150 gr, 250 gr, 500 gr y 1000gr):"))
                    assert peso==100 or peso==150 or  peso==250 or  peso==500 or  peso==1000,"Los Gramos ingresados son incorrectos"
                   # if peso!=100 and peso!=150 and  peso!=250 and  peso!=500 and  peso!=1000:
                       # peso=int(input("Los gramos ingresados son incorrectos intente otra vez"))
                    listaSaboresDeunHelado=[]
                    k=int(input("Ingresar la cantidad de sabores menor a 5\n"))
                    assert k<5,"La cantidad de sabores es invalida"
                    i=0

                    for i in range(k):
                        
                        sabor=int(input("Ingresar sabor(1-7):"))
                        
    
                        if (sabor>0 and sabor<8):  
                           listaSaboresDeunHelado.append(listaSaboresDisponibles.devolverSabor(sabor-1))   
                           unSabor=listaSaboresDisponibles.mostrarSabor(sabor)               
                           print(f"El sabor {i+1} es:{unSabor}")
                           
                        else: print("El sabor seleccionado no existe")

                    unHelado=Helado(peso,listaSaboresDeunHelado)
                           

                    self.__lista.append(unHelado)
           
    def saboresMasPedidos(self,sabores):
        assert isinstance(sabores,dict)

        for unHelado in self.__lista:
            for unSabor in unHelado.getSabor():
                nombre=unSabor.getNombre()
                sabores[nombre]+=1
        sabores_sort = sorted(sabores.items(), key=operator.itemgetter(1), reverse=True)
        for name in enumerate(sabores_sort):
            print(name[1][0], ':', sabores[name[1][0]])

    def calcularGramos(self,numeroSabor):
        gramos = 0.0
        for unHelado in self.__lista:
            for unSabor in unHelado.getSabor():
                if unSabor.getNumero() == numeroSabor:
                    gramos+=unHelado.getGramos()/len(unHelado.getSabor())        
        return gramos

    def saboresPorKg(self,gramos):
        saboresVendidos=[]
        for unHelado in self.__lista:
            if unHelado.getGramos() == gramos:
                for unSabor in unHelado.getSabor():
                    if unSabor.getNombre() not in saboresVendidos:
                        saboresVendidos.append(unSabor.getNombre())
        if len(saboresVendidos)>0:
            print('Sabores: ')
            for i in range(len(saboresVendidos)):
                print(saboresVendidos[i])
        else:
            print(f'No se han vendido helados de {gramos} gramos.')

    def mostrar(self):
        for helado in self.__lista:
            print (helado)     
    def __str__(self):
        a=""
        for Helado in self.__lista:
            a= a+Helado.__str__() + '\n'
        return a