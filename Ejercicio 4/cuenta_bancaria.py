class cuenta_bnc:
    def __init__(self, id, nombre, fecha_ap, num_cuenta, saldo):
        self.id = id
        self.nombre = nombre
        self.fecha_ap = fecha_ap
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_fecha(self):
        return self.fecha_ap

    def get_numcuenta(self):
        return self.num_cuenta

    def get_saldo(self):
        return self.saldo

    def retirar(self, saldo):
        print("¿Que cantidad de dinero quieres retirar?")
        respuesta = int(input())
        if respuesta > saldo:
            print("No es posible.")
        else: 
            saldo = saldo - respuesta
        return saldo

    def ingresar(self, saldo):
        print("¿Que cantidad de dinero quiere ingresar?")
        respuesta = int(input())
        saldo = saldo + respuesta
        return saldo
    
    def transferir(self, saldo, saldo_recibe, num_recibe, num_retira):
        print("A que numero de cuenta quiere realizar latransaccion?")
        print("Introduzca el num de cuenta")
        num_recibe = int(input())
        print("¿Cuanto dinero quiere transferir?")
        respuesta = int(input())
        if respuesta > saldo:
            print("No es posible realizar la transferencia")
        else:
            cuenta_bnc.retirar(saldo, num_retira)
            cuenta_bnc.ingresar(saldo_recibe, num_recibe)
        return saldo, saldo_recibe

