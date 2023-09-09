class Funciones:

    def __init__(self, lista_ ):
        if (type(lista_) != list):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')  
        else:
            self.lista = lista_



    def Fprimo(self, nro): #Berificar si un numero es primo
        resp = True
        for i in range(2, nro):
            if nro%i == 0:
                resp=False
                break
        return resp

    def R_numero(self, lista): #Numero maximo en una lista

        elementos = []
        repeticiones = []
        if len(lista) == 0:
            return None
        for num in lista:
          if num in elementos:
            i = elementos.index(num)
            repeticiones[i] += 1
          else:
               elementos.append(num)
               repeticiones.append(1)
          elemt = elementos[0]
          maximo = repeticiones[0]
        for i, ele in enumerate(repeticiones):
         if  ele > maximo:
            maximo = ele
            elemt = elementos[i]
        return elemt, maximo

    def convertir_grados(self, gra, com, grados):
      if gra not in range(1,4) or type(gra) != int:
          raise ValueError("El primer parametro es invalido, debe ser un numero del 1 al 3")
      
      elif com not in range(1,4) or type(gra) != int:
          raise ValueError("El primer parametro es invalido, debe ser un numero del 1 al 3")
      
      resultado = 0
      grado_entrada = ""
      grado_salida = ""
      if int(gra) == 1: #se comprueva que tipo de grado fué introducido
          grado_entrada = "ºC"
          if int(com) == 2: # se comprueva a que tipo de grado se quiere combertir
              grado_salida = "ºF"
              resultado = (int(grados) * 9/5) + 32
          elif int(com) == 3:
              grado_salida = "ºK"
              resultado = (int(grados) + 273.15)
          elif int(com) == 1:
              grado_salida = "ºC"
              resultado = grados
          else:
              print("Opcion invalida")
              return None
      elif int(gra) == 2:
          grado_entrada = "ºF"
          if int(com) == 2: # se comprueva a que tipo de grado se quiere combertir
              grado_salida = "ºF"
              resultado = grados
          elif int(com) == 3:
              grado_salida = "ºK"
              resultado = (int(grados) - 32) * 5/9
              resultado = resultado + 273.15
          elif int(com) == 1:
              grado_salida = "ºC"
              resultado = (int(grados) - 32) * 5/9
          else:
              print("Opcion invalida")
              return None
      elif int(gra) == 3:
          grado_entrada = "ºK"
          if int(com) == 2: # se comprueva a que tipo de grado se quiere combertir
              grado_salida = "ºF"
              resultado = grados - 273.15
              resultado = (resultado * 9/5) + 32
          elif int(com) == 3:
              grado_salida = "ºK"
              resultado = int(grados)
          elif int(com) == 1:
              grado_salida = "ºC"
              resultado = grados - 273.15
          else:
              print("Opcion invalida")
              return None
      else:
          print("Opcion invalida")
          return None
      return resultado

    def Factorial(self, num):
      if num <= 0 or type(num) != int:
          print("Opcion invalida, debe colocar un numero entero mayor a 0")
      else:
        fac = 1
        for i in range(1, num+1):
          fac *= i
        return fac
      
    def L_FPrimos(self):
        for i in self.lista:
            if (self.Fprimo(i)):
                print("El numero" , i , "es primo")
            else:
                print("El numero" , i , "no es primo")

    def L_Cgrados(self, ent, sal):
        for i in self.lista:
            print(self.convertir_grados(ent, sal, i))
        
    def L_Factorial(self):
        for i in range(self.lista):
            print("El factorial de", i , "es", self.Factorial(i))