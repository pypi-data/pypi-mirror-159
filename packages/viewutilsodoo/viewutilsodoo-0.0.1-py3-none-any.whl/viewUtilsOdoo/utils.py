import datetime
from tabulate import tabulate


def imprimir(arreglo):
    keys = arreglo[0].keys()
    data = arreglo[0]
    tbody = []
    for key in keys:
        valor = ''
        if str(type(data[key])) in ["<class 'str'>", "<class 'datetime.datetime'>", "<class 'bool'>", "<class 'int'>", "<class 'tuple'>"]:
            valor = data[key]
        else:
            valor = str(type(data[key]))
        tbody.append([key, valor])
    print(tabulate(tbody, headers=['KEY', 'VALUES']))


def compare(arreglo1, arreglo2):
    keys = arreglo1[0].keys()
    data1 = arreglo1[0]
    data2 = arreglo2[0]
    similar = []
    diferencias = []
    tbody = []
    for key in keys:
        v1 = ''
        v2 = ''
        tbody = []
        if str(type(data1[key])) in ["<class 'float'>","<class 'str'>", "<class 'datetime.datetime'>", "<class 'bool'>", "<class 'int'>", "<class 'tuple'>"]:
            v1 = data1[key]
            v2 = data2[key]
        else:
            v1 = str(type(data1[key]))
            v2 = str(type(data2[key]))
        if data1[key] == data2[key]:
            similar.append(['EQUAL', key, v1, v2])
        else:
            diferencias.append(['DIFFERENT', key, v1, v2])
    tbody = tbody + similar
    tbody = tbody + diferencias
    print(tabulate(tbody, headers=['COMPARE', 'KEY', 'A', 'B']))


def test():
    print("Prueba")