from perlin_noise import PerlinNoise
import math
import heapq as hq
from savedatastreets import *

noise = PerlinNoise(octaves=2, seed=503)
y = len(l_streets)
cont = 0
perlin =[]
for e in l_streets:
  cola = len(e.get_vecinos())
  #Para cada nodo , sus pesos serán
  
  xpix, ypix= cola,10 
  pic = [[abs(round(noise([i/xpix, j/ypix])*100)) for j in range(xpix)] for i in range(ypix)]
  perlin.append(pic[2])
  #Para agregar los pesos sería
  e.CalculoPeso(perlin[cont])
  cont = cont+1

i = 0
for e in l_streets:
    if i < len(lista_lats_lon):
        e.ingresar_lat_lon(lista_lats_lon[i])
        i = i+1

Grafo = []
for e in l_streets:
  Grafo.append(e.ConversionGrafoFinal())
  
#ALGORTIMOS DE BUSQUEDA
def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n

  cost[s] = 0
  pqueue = [(0, s)]
  while pqueue:
    g, u = hq.heappop(pqueue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        if not visited[v]:
          f = g + w
          if f < cost[v]:
            cost[v] = f
            path[v] = u
            hq.heappush(pqueue, (f, v))

  return path, cost
def dls(G, s, L):
  n = len(G)
  visited = [False]*n
  path = [-1]*n

  def _dls(u, L):
    if L > 0 and not visited[u]:
      visited[u] = True
      for v in G[u]:
        if not visited[v]:
          path[v] = u
          _dls(v, L - 1)

  _dls(s, L)
  return path
  
def ids(G, start, target):
  camino = []
  n = len(G)
  for limit in range(n):
    path = dls(G, start, limit)
    if path[target] != -1:
      break
  for road in path:         
    if road != -1:
      camino.append(road)
  Spath= list(dict.fromkeys(camino))
  return camino


#Se usa el algoritmo ids para encontrar un camino del punto 1 al 199
path = ids(G,1,199)
print(f"Uno de los caminos del punto 1 al punto 199 es {path}")

#Para abrir un csv con la información del grafo.
import csv
header = ['Vecinos']
with open('grafo.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    for nodo in G:
      writer.writerow(nodo)
      
def CalculoDistancia(p1lat,p1lon,p2lat,p2lon):
  aux1 = math.radians(p1lat), math.radians(p1lon)
  aux2 = math.radians(p2lat), math.radians(p2lon)

  d = math.acos(math.sin(aux1[0])*math.sin(aux2[0]) + math.cos(aux1[0])*math.cos(aux2[0])*math.cos(aux1[1] - aux2[1]))
  d = d * 6371.01
  return d

#Falta implementarlo para que sea entre las lat y lon de todas las intersecciones
prueba =CalculoDistancia(41.39743827219736, 2.1789906446773344,41.39563948893357,2.181340259786508)
prueba = '%.2f' % prueba
print(f"{prueba} kilometros")
