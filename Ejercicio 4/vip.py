import cuenta_bancaria

class cuenta_vip(cuenta_bancaria.cuenta_bnc):
    def __init_subclass__(self, id, nombre, fecha_ap, num_cuenta, saldo, negativo_max):
        self.negativo_max = negativo_max
        return super().__init_subclass__(self, id, nombre, fecha_ap, num_cuenta, saldo)

    def get_negativo_max(self):
        return self.negativo_max
    def set_negativo_max(self, negativo_max):
        self.negativo_max = negativo_max