import cuenta_bancaria

class cuenta_vip(cuenta_bancaria.cuenta_bnc):
    def __init_subclass__(self, id, nombre, fecha_ap, num_cuenta, saldo, negativo_max):
        self.negativo_max = negativo_max
        return super().__init_subclass__(self, id, nombre, fecha_ap, num_cuenta, saldo)

    def get_negativo_max(self):
        return self.negativo_max
    def set_negativo_max(self, negativo_max):
        self.negativo_max = negativo_max

    def retirar(self, saldo, negativo_max):
        print("¿Que cantidad de dinero quieres retirar?")
        respuesta = int(input())
        if saldo < negativo_max:
            print("No es posible.")
        else: 
            saldo = saldo - respuesta
        return saldo

    def transferir(self, saldo, saldo_recibe, num_recibe, num_retira, negativo_max):
        print("A que numero de cuenta quiere realizar latransaccion?")
        print("Introduzca el num de cuenta")
        num_recibe = int(input())
        if saldo < negativo_max:
            print("No es posible realizar la transferencia")
        else:
            cuenta_vip.retirar(saldo, num_retira)
            cuenta_vip.ingresar(saldo_recibe, num_recibe)
        return saldo, saldo_recibe