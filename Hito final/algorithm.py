import json
import random as r
import csv
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
  

def camino(prev, i, route):
    if i >= 0:
        camino(prev, prev[i], route)
        route.append(i)

def MinCam(G, source, target):
    pqueue = [(0, source)]
    n = len(G)
    dist = [math.inf] * n
    dist[source] = 0 
    done = [False] * n
    done[source] = True
    prev = [-1] * n
 
    while pqueue:
 
        g,u = hq.heappop(pqueue)      
 
        for v, weight in G[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:  
                f = g + weight
                if f < dist[v]:
                  dist[v] = f
                  prev[v] = u
                  hq.heappush(pqueue, (f, v))
        done[u] = True
 
    route = []
    camino(prev,target,route)
    print(f'Camino de ({source} —> {target}): Costo = {dist[target]}, Ruta = {route}')
    return route



header = ['Vecinos']
with open('grafo.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    for nodo in G:
      writer.writerow(nodo)

def graph():
    trya = []
    for u in range(len(lista_lats_lon)):
        trya.append(tuple(lista_lats_lon[u]))

   
    response = {"loc": trya, "g": Grafo}


    
    return json.dumps(response)

def paths():
    path1 = MinCam(Grafo,1,2)
    path2 = MinCam(Grafo,10,60)
    path3 = MinCam(Grafo,50,189)
    path4 = MinCam(Grafo,62,129)
    path5 = MinCam(Grafo,85,160)
    path6 = MinCam(Grafo,98,192)
    path7 = MinCam(Grafo,57,98)
    path8 = MinCam(Grafo,12,79)
    path9 = MinCam(Grafo,15,18)
    
    
    response = {"path1": path1, "path2": path2, "path3": path3, "path4": path4, "path5":path5,"path6":path6, "path7": path7, "path8":path8, "path9":path9}

    return json.dumps(response)
