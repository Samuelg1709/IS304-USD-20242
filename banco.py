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

def consignar(self, monto):
    if monto > 0:
        self.__saldo += monto
        print(f"consignacion exitosa Su saldo actual es : {self.__saldo} ")
    else:
        print("el monto debe ser positivo")

def retirar(self,monto):
    if  0 < monto <= self.__saldo:
        print(f"Retiro exitoso. Su saldo actual es : {self.__saldo}")
    else: print("monto no permitido")

def aperturaCuenta(self, saldoInicial):
    if saldoInicial >= 100000:
        self.__saldo = saldoInicial
        print(f"creacion de la cuenta exitosa")
    else: print(f"el monto minimo para crear su cuenta es de 100000 pesos.")    