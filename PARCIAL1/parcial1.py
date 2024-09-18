
class Triangulo:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def lados(self):
        return self.__a, self.__b, self.__c
    
    def es_valido(self):
        return (self.__a + self.__b > self.__c and
                self.__a + self.__c > self.__b and
                self.__b + self.__c > self.__a)

    
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c

class Equilatero(Triangulo):
    def tipo(self):
        if self.es_valido() and self.get_a() == self.get_b() == self.get_c():
            return "Equilátero"
        return None

class Isosceles(Triangulo):
    def tipo(self):
        if self.es_valido() and (self.get_a() == self.get_b() or self.get_b() == self.get_c() or self.get_a() == self.get_c()):
            return "Isósceles"
        return None

class Escaleno(Triangulo):
    def tipo(self):
        if self.es_valido() and self.get_a() != self.get_b() and self.get_b() != self.get_c() and self.get_a() != self.get_c():
            return "Escaleno"
        return None

class Rectangulo(Triangulo):
    def tipo(self):
        if self.es_valido():
            sides = sorted([self.get_a(), self.get_b(), self.get_c()])
            if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9:
                return "Rectángulo"
        return None

def clasificar_triangulo(a, b, c):
    triangulos = [Equilatero(a, b, c), Isosceles(a, b, c), Escaleno(a, b, c), Rectangulo(a, b, c)]
    
    for triangulo in triangulos:
        resultado = triangulo.tipo()
        if resultado is not None:
            return resultado
    return "No se pudo clasificar el triángulo."

def main():
    while True:
        print("Ingrese las longitudes de los lados del triángulo (o 'salir' para terminar):")
        entrada = input("Lado 1: ")
        if entrada.lower() == 'salir':
            break
        
        try:
            a = float(entrada)
            b = float(input("Lado 2: "))
            c = float(input("Lado 3: "))
            
            triangulo = Triangulo(a, b, c)
            
            if not triangulo.es_valido():
                print("Esto no es un triángulo.")
                continue
            
            resultado = clasificar_triangulo(a, b, c)
            print(f"El triángulo es: {resultado}")
        
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
    
    
#el encapsulamiento esta en las lineas 3 4 y 5 herencia en Líneas 10, 16, 22, 28
