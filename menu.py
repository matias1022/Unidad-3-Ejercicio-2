from ClaseSabor import Sabor
from ClaseHelado import Helado
import os

from ManejaSabor import ManejadorSabor

class Menu:
    __op = 0

    def __init__(self,opcion=0):
        self.__op = opcion

    def Ejecutar(self,unManejador,listaSaboresDisponibles):
        salir = False
        print('\n')
        while salir == False:
                print('\n')
                print('1-\tRegistrar un helado vendido.')
                print('2-\tMostrar el nombre de los 5 sabores de helado más pedidos.')
                print('3-\tIngresar un número de sabor y estimar el total de gramos vendidos.')
                print('4-\tIngresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos.')

                print('0-\tSalir')
                self.__op = int(input('Ingrese el numero de opcion: '))
                if self.__op == 1:
                    unManejador.cargarVentas(listaSaboresDisponibles)
                    print(unManejador)
                    
        
                elif self.__op == 2:
                    print('             TOP 5 Sabores de helados más pedidos.')
                    sabores = listaSaboresDisponibles.getListaSabores()  # creamos un diccionario para almacenar como clave: nombreSabor, valor: cantidad
                    unManejador.saboresMasPedidos(sabores)
                    #unManejador.saboresMasPedidos(listaSaboresDisponibles)
                elif self.__op == 3:
                    print('             Estimación de cantidad de gramos vendida por cada sabor.')
                    print ('\n',listaSaboresDisponibles)
                    numeroSabor=int(input('Ingrese el número de sabor: '))
                    if numeroSabor in listaSaboresDisponibles.getListaNumeroSabores():
                            gramos = unManejador.calcularGramos(numeroSabor)
                            print('Se vendió: {:.2f} gramos.'.format(gramos))
                    else:
                            print ('El número ingresado es incorrecto.')
                
                elif self.__op == 4:   
                    print('             Ventas según un tamaño de helado.')
                    gramos = int(input('Ingrese el tamaño del envase de helado: '))
                    gramosLista=[100,150,250,500,1000]
                    if gramos in gramosLista:
                        unManejador.saboresPorKg(gramos)
                    else:    print('La cantidad es invalida.') 
                elif self.__op == 0:
                    print('Cerrando programa....')
                    salir = True    
                else:
                    print('Invalida')    