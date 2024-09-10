print("introduccion a clases")
class Animal:
    edad=3
    raza="chihuas"
    comida="croquetas"
    def come(self):
        print("el perro come " +self.comida)
print(Animal)
print("creando el objeto de la clase animal")
perro= Animal()
print(f"edad del perro: {perro.edad}")
print(f"raza del perro: {perro.raza}")
print=perro.come()