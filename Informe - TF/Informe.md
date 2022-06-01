
![](https://lh6.googleusercontent.com/k5W_ASQmsUWstuplMVWFIf-OOSgCmHk8nOyVO4fKajIOQxHKF0IWlGd1u0cCIsDnxSiyko1F8c9PjhQ0DofxNID3KamS-IvOEf-v13cGpBoBrnaXo0D-fmuc_U9bALRPObnOC_pZkvKendzalQ)  
  


# TRABAJO COMPLEJIDAD ALGORÍTMICA

 
 - **Integrantes**
	 - Juan Alejandro Benites Díaz - 202010449 - JBenites10 (DumbarXTS)
	 - Ryan Robert Sweden Silva - 202011397 - RyanSweden03
	 - Franco Emmanuel Vasquez Poma - 201920339 - FrancoVasquez

**Docente:** Canaval Sanchez, Luis Martin  

**Sección:** CC41

**Grupo:** 6



#### Lima, 07 de mayo del 2022

# Glosario:

[1.  Resumen ejecutivo](#idx1)
- [1.1 Problema](#idx1.1)
 - [1.2 Solución](#idx1.2)   
 
[2.  Imagen estática de la ciudad o porción de ciudad elegida.](#idx2)
    
[3.  Descripción de los datos consignados por calle.](#idx3)
    
[4.  Descripción de la información consignada por intersección.](#idx4)
    
[5.  Explicación de cómo se elaboró el grafo, qué representan las aristas y los vértices.](#idx5)


  <div id='idx1' />  
  
# 1. Resumen ejecutivo
  <div id='idx1.1' />

### 1.1. Problema:
Hoy en día mucho nos perdemos tratando de encontrar el camino a nuestro destino desde nuestro punto de partida, esto hace que nos retrasemos o incluso se nos sea imposible llegar a nuestro destino, por ende , hemos decidido crear este proyecto para crear una solución a esta problemática.

  <div id='idx1.2' />  

### 1.2. Solución:
Nuestra solución consiste en que se muestre todas las rutas de la ciudad de manera ordenada, y cuando uno coloque una ruta, este le muestre la ruta más óptima para llegar al destino.

Esto lo hemos implementado utilizando un sistema de grafos.
Enlace del [Colab](https://colab.research.google.com/drive/179Uf8RajJxXaaJqkJE2CzCyY2s8xLN2J?usp=sharing)

  <div id='idx2' />  

## 2. Imagen estática de la ciudad o porción de ciudad elegida:

La porción elegida en este proyecto fue en Badalona, Barcelona, Cataluña, España
![](https://lh6.googleusercontent.com/W8JmzNWSiFzOuiQZBZ0ja-DttPVk0nPh6RyercOYcl-MkBJ92idWhVpz4TZwF5i-eGtVnOHtWxtIucGT48L7ewtxi5ZWqIQq7jSkst-k9t1vYTw5Fq3VBDiZacrC2TShHkarQHch1PgJXTos4A)
    <div id='idx3' />  

## 3.  Descripción de los datos consignados por calle.

Los datos que se almacenaron por calle fueron las calles de la zona elegida, contando con **199 calles.**

En el siguiente enlace se puede visualizar cada calle con su número de índice, creado mediante un [diccionario](https://pastebin.com/SzvUNtAh).

  <div id='idx4' />

## 4. Descripción de la información consignada por intersección:

Para la realización de este proyecto, tomamos como puntos de intersección a los cruces que podrían tener dos calles a más simultáneamente.

Ejemplo:

Intersección entre **C de Menorca** y **Carrer de Provencals**


![](https://lh5.googleusercontent.com/GmIu_KuDsx51DlXeRsUlxoMus-0UcV1cSi_bbbcMFXIYowyU3dhkzpSoNywwfB-R51A3XJngk1BefhMW0cHa9-uCHZnalKq3W69J4c2a9vGWIiAbPVnwpXiQg-au_FbPDYgJ9K8GOsk6Rf-3EA)

  <div id='idx5' />  
  
## 5.   Explicación de cómo se elaboró el grafo, qué representan las aristas y los vértices.

El grafo final se realizó mediante la lectura de un archivo de texto donde se encontraban todos los nombres de las calles y sus intersecciones en forma de una lista adyacente. En el caso de las aristas, estas representan la conexión entre dos calles y el sentido hacia donde esta es direccionada. Finalmente, los vértices representan las calles de la zona de Barcelona seleccionada.


![](https://lh3.googleusercontent.com/s0RxibSen3JFakjkhqb_eqzfN9y3HQjKdjkZ5DPNVpOwBnQcDCQ4ucOeOmeG8ydbe4-_L2kDxY_zIU53eGunhlmc9gr3-S0FepLVX7SceTeyq5ZBi3ir2nIGiq2xXjf-EyFIoaEwlAcKYSt9Mw)
