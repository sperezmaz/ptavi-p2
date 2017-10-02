#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

if __name__ == "__main__":
    calculadora = calcoohija.CalculadoraHija()

    diccOperador = {'suma': calculadora.plus, 'resta': calculadora.minus,
                    'multiplica': calculadora.multiplica,
                    'divide': calculadora.divide}

    with open(sys.argv[1]) as fichero:
        reader = csv.reader(fichero)

        for row in reader:
            operador = row[0]
            result = int(row[1])
            row = row[2:]

            for operando in row:
                try:
                    result = diccOperador[operador](result, int(operando))
                except KeyError:
                    sys.exit('Operación sólo puede ser suma, resta, multiplica'
                             ' o divide')
                except ZeroDivisionError:
                    sys.exit("Division by zero is not allowed")

            print(result)
