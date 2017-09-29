#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():

    def plus(self, op1, op2):
        """ Function to sum the operands. Ops have to be ints """
        return op1 + op2

    def minus(self, op1, op2):
        """ Function to substract the operands """
        return op1 - op2

class CalculadoraHija(Calculadora):

    def multiplica(self, op1, op2):
        return op1 * op2

    def divide(self, op1, op2):
        return op1 / op2

if __name__ == "__main__":
    calculadora = CalculadoraHija()
    
    if len(sys.argv) != 4:
        sys.exit("Úsalo así: Python3 calculadora.py numero1 operador numero2")
	
    diccOperador = {'suma': calculadora.plus, 'resta': calculadora.minus, 
                    'multiplica': calculadora.multiplica, 
                    'divide': calculadora.divide}
    
    operador = sys.argv[2]
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    try:
        result = diccOperador[operador](operando1, operando2)
    except KeyError:
        sys.exit('Operación sólo puede ser suma, resta, multiplica o divide')
    except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

    print(result)
