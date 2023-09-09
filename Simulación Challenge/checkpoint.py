# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):


    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    resultado = 1
    if type(numero) == int and numero > 0:
        for i in range(1, numero+1):
            resultado *= i
        return resultado
    else:
        return 'Funcion incompleta'

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    primo = True
    if type(valor) == int:
        for i in range(2,valor):
            if valor%i == 0:
                primo = False
                break
        return primo
    else:
        return 'Funcion incompleta'
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal():
        def __init__(self, especie, color):
            if type(especie) == str and type(color) == str:
                self.especie = especie
                self.color = color
                self.edad = 0
            else:
                raise ValueError("Parametros incorrectos")
        
        def Cumplir_anios(self):
            self.edad += 1
            print("El " + self.especie , self.color + " tiene " + self.edad + " años de edad")

    return Animal(especie, color)
