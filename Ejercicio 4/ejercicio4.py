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
        pass
    def ingresar(self, saldo):
        pass
    def transferir(self, saldo):
        pass


    
