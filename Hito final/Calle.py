import random

class Calle: 
  def __init__(self, nombre):
    self.nombre = nombre
  def Agregar_vecinos(self,vecinos):
    self.vecinos = vecinos
  def insert_id(self, id):
    self.id = id
  def get_vecinos(self):
    return self.vecinos
  def ingresar_lat_lon(self, lista_coord):
    self.coord = lista_coord
  def CalculoPeso(self,l_pesos):
    self.pesos = l_pesos
  def ingresar_g(self,G):
    self.id_v = G
  def Trafico(self):
    self.lista_trafico = [0]*24
    for i in range(len(self.lista_trafico)):
      if i >= 0 and i <= 9:
        self.lista_trafico[i] = random.randint(5,8)
      elif i>=9 and i <= 11:
        self.lista_trafico[i] = random.randint(8,15)
      elif i>=11 and i<= 15:
        self.lista_trafico[i] = random.randint(15,20)
      elif i>=16 and i<= 21:
        self.lista_trafico[i] = random.randint(20,25)       
      else:
        self.lista_trafico[i] = random.randint(8,16)
  def ConversionGrafoFinal(self):
    #Aca se crea el grafo final que será (id del vecino , peso)
    aux1,aux2,aux3 = self.vecinos, self.pesos, self.id_v
    resultado=zip(aux3,aux2)
    return(list(resultado))

