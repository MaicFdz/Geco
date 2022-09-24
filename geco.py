
from Modulos import Mod_ListaDeRenglones as LdR
import os
import time
import platform # https://parzibyte.me/blog/2019/01/19/detectar-sistema-operativo-python/
import pathlib # https://realpython.com/python-pathlib/#creating-paths
				# https://docs.python.org/3/library/pathlib.html#basic-use
# BIT A STRING : https://stackoverflow.com/questions/9916334/bits-to-string-python

###################################################################################################

class Sistema:

	def __init__(self):
		self.id = platform.system()
		
	def limpiar(self):
		if self.id == 'Linux':
			os.system('clear')
		if self.id == 'Windows':
			os.system('cls')
			
	def pausa(self, texto):
		if self.id == 'Linux':
			input(texto)
		elif self.id == 'Windows':
			print(texto)
			os.system('pause>nul')
		else:
			print('???')

###################################################################################################

class Transpilador:

	def __init__(self):


		directorio_inicial = pathlib.Path.cwd()
		directorio_de_archivos=str(directorio_inicial)+'/Codigos_Geco'

		#print('directorio actual:', directorio_actual)
	
		self.directorio_de_archivos = directorio_de_archivos
		self.texto_geco = LdR.ListaDeRenglones()
		self.texto_python = LdR.ListaDeRenglones()

		self.nombre_archivo = None

		os.system('cd '+self.directorio_de_archivos)
#		print('Carpeta actual:', self.directorio_de_archivos)



	def cargar_txt(self, _nombre_de_archivo):

#		print(self.directorio_de_archivos)
#		print(nombre_de_archivo)
		self.nombre_de_archivo = _nombre_de_archivo

		self.texto_geco.lineas = []
		self.texto_geco.importar(self.directorio_de_archivos, self.nombre_de_archivo)

	def exportar(self):
		self.texto_python.exportar(self.directorio_de_archivos, self.nombre_de_archivo)

	def transpilar(self):

		self.texto_python.lineas = []
		#print('  Transpilando...')
		
		for linea in self.texto_geco.lineas:
	
			linea=linea.replace('importar', 'import')

			linea=linea.replace('__nombre__', '__name__') # "__main__"

			linea=linea.replace('__inic__', '__init__')
			linea=linea.replace('auto', 'self')

			linea=linea.replace('clase', 'class')

			linea=linea.replace(' en ', ' in ')

			linea=linea.replace('imprimir', 'print')
			linea=linea.replace('entrada', 'input')

#			linea=linea.replace('limpiar()', "os.system('cls')")
#			linea=linea.replace('pausa()', "os.system('pause')")

			linea=linea.replace('sino-si', 'elif')
			linea=linea.replace('sino', 'else')
			linea=linea.replace('si ', 'if ')

			linea=linea.replace('input', 'entrada')


			linea=linea.replace('mientras', 'while')
			linea=linea.replace('Verdadero', 'True')
			linea=linea.replace('Falso', 'False')

			linea=linea.replace('para', 'for')

			linea=linea.replace('cortar', 'break')
			linea=linea.replace('retorno', 'return')

			linea=linea.replace('intentar', 'try:')
			linea=linea.replace('excepto', 'except')
			linea=linea.replace('finalmente', 'finally')

			self.texto_python.lineas.append(linea)

		return (self.texto_python)

	def lanzar(self):
		ruta = self.directorio_de_archivos+'/'+self.nombre_de_archivo+'.py'

		print('----- INICIO PROGRAMA ---------------------------------------------------')

		try:
			os.system('python3 '+ruta)
			
		except ModuleNotFoundError:
			print('ERROR: Modulo no encontrado')
		except:
			print('ERROR: Algo fallo')
			sistema.pausa('Pulse ENTER para lanzar nuevamente')	
		
		finally:
			print('-----   FIN PROGRAMA  ---------------------------------------------------')
			print('Lanzamiento: OK')


###################################################################################################

if __name__ == '__main__':

	sistema = Sistema()
	geco = Transpilador()
	
	print('\n¡Bienvenid@ al transpilador de Geco!\n')

	print('El directorio de trabajo es:', geco.directorio_de_archivos)


	print('Sistema operativo:', sistema.id)
	print('Hora del sistema:', 'xx:xx:xx')


	sistema.pausa('\nPulse ENTER para comenzar')
	sistema.limpiar()

	
###################################################################################################


	app = True
	nombre_txt = input('Nombre de archivo .txt:\n')

	while app == True:

		sistema.limpiar()

		geco.cargar_txt(nombre_txt)
		geco.transpilar()
		geco.exportar()
		geco.lanzar()

		sistema.pausa('Pulse ENTER para lanzar nuevamente')


