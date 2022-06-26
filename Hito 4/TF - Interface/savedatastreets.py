from Calle import *
import codecs

l_streets = []
lista_lats_lon = []
G = []
with codecs.open("Barcelona.csv",'r',encoding='utf-8',errors='ignore') as f:
  nombres = []
  calles = dict()
  info = []

  for line in f:
    Nodo, neigh = (Par.strip() for Par in line.split("-"))
    neigh = neigh.split()
    street = Calle(Nodo)
    calles[Nodo] = len(nombres)
    nombres.append(Nodo)
    info.append(neigh)
    street.Agregar_vecinos(neigh)
    street.insert_id(calles[Nodo])
    l_streets.append(street)

  for v in info:
    G.append([calles[Nodo] for Nodo in v])

  t = 0
  for e in l_streets:
    e.ingresar_g(G[t])
    t = t+1

#La lista se usa para sacar la información de datos.txt

with codecs.open("datos.csv",'r',encoding='utf-8',errors='ignore') as f:
  calles = dict()
  info = []
  for line in f:
    Nodo, coords = (Par.strip() for Par in line.split("-"))
    coords = coords.split(",")
    for i,v in enumerate(coords):
      coords[i]= v.split()
    lista_lats_lon.append(coords)