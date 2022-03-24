import cuenta_bancaria

class plazo_fijo(cuenta_bancaria.cuenta_bnc):
    def __init_subclass__(self, id, nombre, fecha_ap, num_cuenta, saldo, fecha_vencimiento):
        self.fecha_vencimiento = fecha_vencimiento
        super().__init_subclass__(self, id, nombre, fecha_ap, num_cuenta, saldo)
    
    def get_fecha_vencimiento(self):
        return self.fecha_vencimiento
    def set_fecha_vencimiento(self, fecha_vencimiento):
        self.fecha_vencimiento = fecha_vencimiento
    def penalizador(self, fecha_vencimiento, saldo):
        pass
    