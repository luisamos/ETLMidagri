import os, json
from progress.bar import Bar
from entidades.GDAL import GDAL
from entidades.Oracle import Oracle
from entidades.Postgresql import Postgresql

class ETL():
	gdal = None
	configuracion= None
	objeto= None

	def __init__(self):
		self.gdal = GDAL()
		with open('./ConfiguracionGDB.json', 'r', encoding="utf-8") as file1:
			self.configuracion = json.load(file1)

		with open('./ObjetosGeograficos.json', 'r', encoding="utf-8") as file2:
			self.objeto = json.load(file2)
	
	def ListarDrivers(self):
		print("Listado de Driver GDAL:\n")
		for driver in self.gdal.ListarDrivers():
			print(driver)

	def PostgreSQL2ShapeFile(self, opcion):
		print("\n███ INICIANDO PROCESO DE TRANSFERENCIA DE DATOS DE POSTGRESQL A SHAPEFILE ███")
		self.gdal.PostgreSQL2ShapeFile(opcion, 'POSTGRESQL')

	def PostgreSQL2Oracle(self, opcion):
		print("\n███ INICIANDO PROCESO DE TRANSFERENCIA DE DATOS DE POSTGRESQL A ORACLE ███")
		datos =self.gdal.PostgreSQL2SqlOracle(opcion, 'POSTGRESQL')
		
		conexion_oracle = Oracle(usuario = self.configuracion["INTEROPERABILIDAD"]['usuario']
			                        , contrasena = self.configuracion["INTEROPERABILIDAD"]['contrasena']
			                        , servidor = self.configuracion["INTEROPERABILIDAD"]['servidor']
			                        , puerto = self.configuracion["INTEROPERABILIDAD"]['puerto']
			                        , sid = self.configuracion["INTEROPERABILIDAD"]['sid']
			                        , numero= 4)
		o_tabla = self.objeto[opcion]['o_tabla']
		try:
			with Bar("5. Insertando datos al objeto geográfico : {0}".format(o_tabla), max=len(datos), fill='█') as bar:
				for i in datos:
					conexion_oracle.Ejecutar(i)
					bar.next()

				conexion_oracle.Confirmar()
		except Exception as e:
			print("\nError: "+e)
		finally:
			conexion_oracle.Cerrar()
			print("\nFinalizado...")		

	def PostGIS2ShapeFile(self, opcion):
		print("\n███ INICIANDO PROCESO DE TRANSFERENCIA DE DATOS DE POSTGIS A SHAPEFILE ███")
		self.gdal.PostGIS2ShapeFile(opcion, 'POSTGIS')

	def PostGIS2Oracle(self, opcion):
		print("\n███ INICIANDO PROCESO DE TRANSFERENCIA DE DATOS DE POSTGIS A ORACLE ███")
		
		conexion_oracle = Oracle(usuario = self.configuracion["INTEROPERABILIDAD"]['usuario']
			                        , contrasena = self.configuracion["INTEROPERABILIDAD"]['contrasena']
			                        , servidor = self.configuracion["INTEROPERABILIDAD"]['servidor']
			                        , puerto = self.configuracion["INTEROPERABILIDAD"]['puerto']
			                        , sid = self.configuracion["INTEROPERABILIDAD"]['sid']
			                        , numero= 1)
		o_esquema= self.objeto[opcion]['o_esquema']
		o_tabla = self.objeto[opcion]['o_tabla']
		existe_tabla = conexion_oracle.ExisteTabla(o_esquema, o_tabla)[0][0]
		conexion_oracle.Cerrar()

		if existe_tabla == 0:
			print("2. No existe el objeto: {0} en la base de datos de Oracle.".format(o_tabla))
		else:
			datos =self.gdal.PostGIS2SqlOracle(opcion, 'POSTGIS')
			conexion_oracle = Oracle(usuario = self.configuracion["INTEROPERABILIDAD"]['usuario']
			                        , contrasena = self.configuracion["INTEROPERABILIDAD"]['contrasena']
			                        , servidor = self.configuracion["INTEROPERABILIDAD"]['servidor']
			                        , puerto = self.configuracion["INTEROPERABILIDAD"]['puerto']
			                        , sid = self.configuracion["INTEROPERABILIDAD"]['sid']
			                        , numero= 4)
		
			try:
				with Bar("5. Insertando datos al objeto geográfico : {0}".format(o_tabla), max=len(datos), fill='█') as bar:
					for i in datos:
						conexion_oracle.Ejecutar(i)
						bar.next()

					conexion_oracle.Confirmar()
			except Exception as e:
				print("\nError: "+e)
			finally:
				conexion_oracle.Cerrar()
				print("\nFinalizado...")

	def WFS2ShapeFile(self, opcion):
		print("\n███ INICIANDO PROCESO DE TRANSFERENCIA DE DATOS DE OGC:WFS A SHAPEFILE ███")
		self.gdal.WFS2ShapeFile(opcion)