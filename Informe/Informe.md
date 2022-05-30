![](https://lh6.googleusercontent.com/k5W_ASQmsUWstuplMVWFIf-OOSgCmHk8nOyVO4fKajIOQxHKF0IWlGd1u0cCIsDnxSiyko1F8c9PjhQ0DofxNID3KamS-IvOEf-v13cGpBoBrnaXo0D-fmuc_U9bALRPObnOC_pZkvKendzalQ)  
  

<h1 align=center>
TRABAJO COMPLEJIDAD ALGORÍTMICA
</h1>
 
 - **Integrantes**
	 - Juan Alejandro Benites Díaz - U202010449
	 - Ryan Robert Sweden Silva - U202011397
	 -  Franco Emmanuel Vasquez Poma - U201920339

<b>Docente:</b> Canaval Sanchez, Luis Martin  
<p align=left> 
<b>Sección:</b> CC41
<br>
<b>Grupo:</b> 2 
</p>


<p align=center> 
<b>Lima, 07 de mayo del 2022</b>

# Glosario:

[1.  Resumen ejecutivo](#idx1)
- [1.1 Problema](#idx1.1)
 - [1.2 Solución](#idx1.2)   
 
[2.  Imagen estática de la ciudad o porción de ciudad elegida.](#idx2)
    
[3.  Descripción de los datos consignados por calle.](#idx3)
    
[4.  Descripción de la información consignada por intersección.](#idx4)
    
[5.  Explicación de cómo se elaboró el grafo, qué representan las aristas y los vértices.](#idx5)


  <div id='idx1' />  
<h1 align=left>
1. Resumen ejecutivo
</h1>
  <div id='idx1.1' />

### 1.1. Problema:
<p align=justify>

Hoy en día mucho nos perdemos tratando de encontrar el camino a nuestro destino desde nuestro punto de partida, esto hace que nos retrasemos o incluso se nos sea imposible llegar a nuestro destino, por ende , hemos decidido crear este proyecto para crear una solución a esta problemática.
</p>
  <div id='idx1.2' />  

### 1.2. Solución:
<p align=justify>
Nuestra solución consiste en que se muestre todas las rutas de la ciudad de manera ordenada, y cuando uno coloque una ruta, este le muestre la ruta más óptima para llegar al destino.

Esto lo hemos implementado utilizando un sistema de grafos.
Enlace del [Colab](https://colab.research.google.com/drive/179Uf8RajJxXaaJqkJE2CzCyY2s8xLN2J?usp=sharing)

</p>
  <div id='idx2' />  

<h1 align=left>
2. Imagen estática de la ciudad o porción de ciudad elegida:
</h1>
   <p align=justify>
La porción elegida en este proyecto fue en Badalona, Barcelona, Cataluña, España

  <p align="center">
    <img src="https://lh6.googleusercontent.com/XXFW8-Xzfk17z9dctX8_ICXotVoYL80_oYFH3zL04dlhm1qiq8hulTDPyZg0GE2j3pBiw1uh1smOJ18xF2G5sfXuiwvIyCoT3ICykBzhyzVatqRWtRHPGzjNR1Lgl0raICml_XExfWx_eBPMqg">
      
  </p>
    <div id='idx3' />  
<h1 align=left>
3.  Descripción de los datos consignados por calle.
</h1>
    
   <p align=justify>
Los datos que se almacenaron por calle fueron las calles de la zona elegida, contando con <b>199 </b>calles.<br>

En el siguiente enlace se puede visualizar cada calle con su número de índice, creado mediante un <b>[diccionario](https://pastebin.com/SzvUNtAh).</b>


  <div id='idx4' />
  <h1 align=left>
4. Descripción de la información consignada por intersección:
</h1>
<p align=justify>
Para la realización de este proyecto, tomamos como puntos de intersección a los cruces que podrían tener dos calles a más simultáneamente.

Ejemplo:

Intersección entre <b>C de Menorca</b> y <b>Carrer de Provencals</b>
</p>

<p align="center">
    <img src="https://lh4.googleusercontent.com/Nb5wdgiCLn_spKxU9vz07f1pTGSwzhibDVJNYA8Fos7WSfC_VGt0_MDYcohdZx7BRdZXiKw3wABgsklxaEWJyEaATIp81D_rR4k8zOIzGdMbEDa94joc_XSdnByc3zJ2MWmGK4arEtBVaB5HMg">
    
  <div id='idx5' />  
 <h1 align=left>
5.   Explicación de cómo se elaboró el grafo, qué representan las aristas y los vértices.
</h1>
<p align="justify">
El grafo final se realizó mediante la lectura de un archivo de texto donde se encontraban todos los nombres de las calles y sus intersecciones en forma de una lista adyacente. En el caso de las aristas, estas representan la conexión entre dos calles y el sentido hacia donde esta es direccionada. Finalmente, los vértices representan las calles de la zona de Barcelona seleccionada.


<p align="center">
    <img src="https://lh4.googleusercontent.com/lCV4VWPoQV73-e-eJ4WuuY5FbX9FgqeaelmI-YIKTlVPY8A6xlFQW2hD3RXukFRHSW0HCqv0GORdcJqxBynu2AGtciht1RMx4lfMtbUuBK8YzKjGYh7JH-6Nuai6Ino7WUmq3Sq9KZXZHQUCmw">
