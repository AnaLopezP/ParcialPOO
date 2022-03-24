import cuenta_bancaria
import plazo_fijo
import vip
import random
from datetime import datetime

inicio = datetime(2022, 1, 1)
final = datetime(2022, 12, 31)
if __name__ == "__main__":
    print("¿Que tipo de cuenta quieres hacer?")
    opciones = ["vip", "normal", "plazo fijo"]
    print(opciones)
    respuesta = input()
    print("¿cual es el nombre del titular?")
    cuenta_bancaria.cuenta_bnc.get_nombre = str(input())
    print(cuenta_bancaria.cuenta_bnc.get_nombre)
    cuenta_bancaria.cuenta_bnc.get_numcuenta = random.randint(100000000000, 999999999999)
    print(cuenta_bancaria.cuenta_bnc.get_numcuenta)
    cuenta_bancaria.cuenta_bnc.get_id = 123456
    cuenta_bancaria.cuenta_bnc.get_fecha = inicio + (final - inicio)*random.random()
    cuenta_bancaria.cuenta_bnc.get_saldo = random.randint(30, 200000)
    if respuesta == "vip":
        vip.cuenta_vip.get_negativo_max = -2000
    elif respuesta == "plazo fijo":
        plazo_fijo.plazo_fijo.get_fecha_vencimiento = inicio + (final - inicio)*random.random()
    elif respuesta == "normal":
        pass
    else:
        print("no es una respuesta valida")