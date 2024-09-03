class  CuentaBancaria:
    def _init_(self,nroCuenta, nombreCliente, FechaApertura,saldo= 10000):
        self.__nroCuenta = nroCuenta
        self.__nombreCliente = nombreCliente
        self.__FechaApertura = FechaApertura
        self.__saldo = saldo

        def get_nroCuenta(self):
            return self.__nroCuenta

        def set_nroCuenta(self, nroCuenta):
            self.__nroCuenta= nroCuenta

        def get_nombreCliente(self):
            return self.__nombreCliente

        def set_nombreCliente(self, nombreCliente):
            self.__nombreCliente= nombreCliente

        def get_FechaApertura(self):
            return self.__FechaApertura

        def set_FechaApertura(self, FechaApertura):
            self.__FechaApertura= FechaApertura
   
            def get_saldo(self):
                return self.__saldo

        def set_saldo(self, saldo):
            self.__saldo= saldo
