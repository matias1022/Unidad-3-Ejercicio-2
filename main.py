


from ClaseHelado import Helado
from ClaseSabor import Sabor
from menu import Menu
from ManejaHelado import ManejadorHelado
from ManejaSabor import ManejadorSabor

def test():
   manejadorSabor=ManejadorSabor()
   manejadorHelado=ManejadorHelado()
   unSabor=Sabor(1,"Fresa","Fresas hecho Helado")
   manejadorSabor.cargar()
   print(manejadorSabor)
   listaSabores=[unSabor]
   helado = Helado(1000,listaSabores)
   print(helado)
   
   manejadorHelado.cargarVentas(manejadorSabor)
   print(manejadorHelado)
   print("---------------FIN TEST--------------")
if __name__ == '__main__':

   test()
   input()
   lista=ManejadorSabor()
   lista.cargar()
   helados=ManejadorHelado()
   print (lista)
   menu=Menu()
   menu.Ejecutar(helados,lista)
   print(helados)


  