class CuentaBancaria:
    def __init__(self, nroCuenta, nombreCliente, fechaApertura, saldo=100000):
        self.__nroCuenta = nroCuenta
        self.__nombreCliente = nombreCliente
        self.__fechaApertura = fechaApertura
        self.__saldo = saldo


    def get_nroCuenta(self):
        return self.__nroCuenta

    def set_nroCuenta(self, nroCuenta):
        self.__nroCuenta = nroCuenta

    def get_nombreCliente(self):
        return self.__nombreCliente

    def set_nombreCliente(self, nombreCliente):
        self.__nombreCliente = nombreCliente

    def get_fechaApertura(self):
        return self.__fechaApertura

    def set_fechaApertura(self, fechaApertura):
        self.__fechaApertura = fechaApertura

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def consignar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Consignacion exitosa. Su saldo actual es: {self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Su saldo actual es: {self.__saldo}")
        else:
            print("Monto no permitido para retiro.")

    def aperturaCuenta(self, saldoInicial):
        if saldoInicial >= 100000:
            self.__saldo = saldoInicial
            print("Creacion de la cuenta exitosa.")
        else:
            print("El monto minimo para crear su cuenta es de 100000 pesos.")

def menu():
    cuentas = {}

    while True:
        print("\n--- Menu de operaciones bancarias ---")
        print("1. Aperturar cuenta")
        print("2. Consignar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            numeroCta = input("Numero de cuenta: ")
            nombreCliente = input("Nombre del cliente: ")
            fechaApertura = input("Fecha de apertura (DD/MM/AAAA): ")
            saldoInicial = float(input("Saldo inicial: "))
            cuenta = CuentaBancaria(numeroCta, nombreCliente, fechaApertura)
            cuenta.aperturaCuenta(saldoInicial)
            cuentas[numeroCta] = cuenta

        elif opcion == '2':
            numeroCta = input("Numero de cuenta: ")
            if numeroCta in cuentas:
                monto = float(input("Monto a consignar: "))
                cuentas[numeroCta].consignar(monto)
            else:
                print("Cuenta no encontrada.")

        elif opcion == '3':
            numeroCta = input("Numero de cuenta: ")
            if numeroCta in cuentas:
                monto = float(input("Monto a retirar: "))
                cuentas[numeroCta].retirar(monto)
            else:
                print("Cuenta no encontrada.")

        elif opcion == '4':
            numeroCta = input("Numero de cuenta: ")
            if numeroCta in cuentas:
                saldo = cuentas[numeroCta].get_saldo()
                print(f"Saldo disponible: {saldo}")
            else:
                print("Cuenta no encontrada.")

        elif opcion == '5':
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida, intente nuevamente.")


menu()
