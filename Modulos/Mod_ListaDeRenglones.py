#!/usr/bin/env python
# -*- coding: utf-8 -*-
#v1.01

#LIBRERÍAS-----------------------------------------------------------------------
import os

#CLASE PRINCIPAL-----------------------------------------------------------------
class ListaDeRenglones():

 def __init__(self):
  self.lineas=[]
  self.modo='predeterminado'

#La lista "lineas" es el dato más importante para definir en éste módulo.
#A partir de ésta lista podemos exportar.
#Si importarmos, lo hacemos en ésta misma lista.
#Si queremos utilizar una lista generada dentro del programa
#bastará con asignarla como valor de "lineas".
#Ej:
#MiObjetoRenglon.lineas=miLista

#MÉTODO: IMPORTAR LISTA DESDE ARCHIVO TXT------------------------------------------------------
 def importar(self, carpeta, archivo):
  self.cargarArchivo(carpeta, archivo)


#MÉTODO: CARGAR ARCHIVO EN MEMORIA----------------------------------------------------------
 def cargarArchivo(self, carpeta, archivo):

#principal-----------------------------------------------------------------------

  barra=b'/'

  ruta_archivo = carpeta+'/'+archivo+'.txt'



  f=open(ruta_archivo,"r")
  posicion=0

  for renglon in f:

   if renglon=="":    #Éste es un arreglo para las líneas que están vacías
    self.lineas[posicion:posicion]=["\n"]
   else: 
    self.lineas[posicion:posicion]=[renglon] #Copia el renglon incluyendo el salto de línea
   posicion=posicion+1

  f.close()

#arreglo------------------------------------------------------------------------

  if self.modo=='predeterminado' or self.modo=='Excel':

   ultimoIndice=len(self.lineas)-1
   copia=self.lineas
   indice=0

   while indice<ultimoIndice: # Éste arreglo elimina los saltos de todas las líneas, exceptuando la última

    if copia[indice][-1:]=="\n":
     self.lineas[indice]=(self.lineas[indice][:-1])
    indice=indice+1

  if self.modo=="Excel":
   self.lineas[indice]=(self.lineas[indice][:-1]) # Quita el último salto de línea para archivos Excel(si se indice en el modo)

# NOTA: Si para volcar se utillisa un ScrollText (en lugar de Excel o Txt) basta con indicarlo en el modo. Así salteará las funciones predeterminadas.

#MÉTODO: EXPORTAR LA LISTA COMO ARCHIVO TXT------------------------------------------------------
 def exportar(self, carpeta, archivo):
  barra=b'/'

  ruta_archivo = carpeta+'/'+archivo+'.py'



  f=open(ruta_archivo,"w")

  ultimoIndice=len(self.lineas)-1
  indice=0

  while indice<ultimoIndice:

   f.write(str(self.lineas[indice])+"\n") # Añade salto de líneas hasta la anteúltima linea...,
   indice=indice+1

  f.write(str(self.lineas[indice])) # A la última línea la deja con el salto original
  f.close()


#-------------------------------------------------------------------------------
