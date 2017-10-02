#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":
    calculadora = calcoohija.CalculadoraHija()

    diccOperador = {'suma': calculadora.plus, 'resta': calculadora.minus,
                    'multiplica': calculadora.multiplica,
                    'divide': calculadora.divide}

    fichero = open(sys.argv[1], 'r')
    lines = fichero.readlines()

    for line in lines:
        parametros = line.split(',')
        operador = parametros[0]
        operandos = parametros[1:]
        operandos[-1] = operandos[-1][:-1]

        result = int(operandos[0])
        operandos = operandos[1:]

        for operando in operandos:
            try:
                result = diccOperador[operador](result, int(operando))
            except KeyError:
                sys.exit('Operación sólo puede ser suma, resta, multiplica o'
                         ' divide')
            except ZeroDivisionError:
                sys.exit("Division by zero is not allowed")

        print(result)
