import cuenta_bancaria
import plazo_fijo
import vip
import random

if __name__ == "__main__":
    print("¿cual es el nombre del titular?")
    cuenta_bancaria.cuenta_bnc.get_nombre = str(input())
    print(cuenta_bancaria.cuenta_bnc.get_nombre)
    cuenta_bancaria.cuenta_bnc.get_numcuenta = random.randint(100000000000, 999999999999)
    print(cuenta_bancaria.cuenta_bnc.get_numcuenta)
    cuenta_bancaria.cuenta_bnc.get_id = 123456
    cuenta_bancaria.cuenta_bnc.get_fecha