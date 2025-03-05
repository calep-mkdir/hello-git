## Clases ##

class Paquito:
  def __init__(self, apellido, edad, altura, peso):
    self.apellido = apellido, 
    self.edad = edad,
    self.altura = altura,
    self.peso = peso

  def decirnombre(self):
    print("Hola mi nombre es Paquito!!")

my_paquito = Paquito("Rodriguez", 43, 1.90, 80)

my_paquito.decirnombre()
