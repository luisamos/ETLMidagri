import sys, os, json
from osgeo import gdal, ogr, osr
from progress.bar import Bar
from entidades.Postgresql import Postgresql

class GDAL():
	configuracion= None
	objeto= None
	servicio= None

	def __init__(self):
		with open('./configuracionGDB.json', 'r', encoding="utf-8") as file1:
			self.configuracion = json.load(file1)

		with open('./ObjetosGeograficos.json', 'r', encoding="utf-8") as file2:
			self.objeto = json.load(file2)

		with open('./Servicios.json', 'r', encoding="utf-8") as file3:
			self.servicio = json.load(file3)

	def WKB2WKT(self, shape):
		geom = ogr.CreateGeometryFromWkb(shape)
		wkt = geom.ExportToWkt()
		return wkt

	def ListarDrivers(self):
		listar_nombre = []
		for i in range(gdal.GetDriverCount()):
		    driver = gdal.GetDriver(i)		    
		    listar_nombre.append(gdal.GetDriver(i).ShortName)
		return listar_nombre

	def PostgreSQL2ShapeFile(self, geografico, db):
		try:
			nombre = self.objeto[geografico]['nombre_shp']
			if nombre is not None:
				nombre_shp = "{0}\\{1}".format(self.objeto[geografico]['ruta_shp'], nombre + '.shp')

				if os.path.exists(self.objeto[geografico]['ruta_shp']):
					out_driver = ogr.GetDriverByName('ESRI Shapefile')
					out_ds = out_driver.CreateDataSource(nombre_shp)
					out_srs = osr.SpatialReference()
					out_srs.ImportFromEPSG(self.objeto[geografico]['pg_srid'])					
					
					tipo_geometria = self.objeto[geografico]['pg_tipo_geometria']
					if tipo_geometria is not None:
						if tipo_geometria == 'punto':
							geometrico = ogr.wkbPoint
						elif tipo_geometria == 'linea':
							geometrico = ogr.wkbLineString
						elif tipo_geometria == 'poligono':
							geometrico = ogr.wkbPolygon
						elif tipo_geometria == "multipolygon":
							geometrico = ogr.wkbMultiPolygon

						conexion_postgresql = Postgresql(usuario = self.configuracion[db]['usuario']
				                        , contrasena = self.configuracion[db]['contrasena']
				                        , servidor = self.configuracion[db]['servidor']
				                        , base_datos = self.configuracion[db]['base_datos'])

						columnas = self.objeto[geografico]['pg_columnas']
						if columnas is not None:
							lista_columnas = ""
							for i in columnas:
								lista_columnas = lista_columnas +"'{0}', ".format(i)

							pg_esquema = self.objeto[geografico]['pg_esquema']
							pg_tabla = self.objeto[geografico]['pg_tabla']
							if pg_esquema is not None and pg_tabla is not None:
								
								out_layer = out_ds.CreateLayer("polygon", out_srs, geometrico)
								consulta_sql = "SELECT column_name AS columna, udt_name AS tipo FROM information_schema.columns WHERE table_schema = '{0}' AND column_name IN ({1}) AND table_name= '{2}'".format(pg_esquema, lista_columnas[:-2], pg_tabla)
								lista = conexion_postgresql.Ejecutar(consulta_sql)

								if lista is not None:							
									for columna, tipo  in lista:
										if tipo == 'varchar':
											fd = ogr.FieldDefn(columna[:10], ogr.OFTString)									
										if tipo == "int4" or tipo == "int":
											fd = ogr.FieldDefn(columna[:10], ogr.OFTInteger)									
										if tipo == "timestamp":
											fd = ogr.FieldDefn(columna[:10], ogr.OFTDateTime)									
										if tipo == "float":
											fd = ogr.FieldDefn(columna[:10], ogr.OFTReal)
										out_layer.CreateField(fd)
								
								consulta_sql = "SELECT {0} st_asbinary(shape) AS shape FROM {1}.{2}".format(lista_columnas.replace("'",""), pg_esquema, pg_tabla)
								datos = conexion_postgresql.Ejecutar(consulta_sql)
								print("2. Extraendo datos de la tabla: {0}.{1}".format(pg_esquema,pg_tabla))
								if datos is not None:
									with Bar("3. Insertando al archivo ShapeFile: {0}.shp".format(nombre), max=len(datos), fill='█') as bar:
										for i in datos:
											shp = ogr.Feature(out_layer.GetLayerDefn())
											j=0
											for columna, tipo in lista:
												if tipo == 'varchar':
													shp.SetField(columna[:10], i[j])
													#print("\n{0}: {1}".format(columna[:10], i[j]))
												else:
													shp.SetField(columna[:10], i[j])
													#print("\n{0}: {1}".format(columna[:10], i[j]).encode('UTF-8'))
												j=j+1

											geom = ogr.CreateGeometryFromWkb(i[len(columnas)])
											shp.SetGeometry(geom)
											out_layer.CreateFeature(shp)
											bar.next()

								conexion_postgresql.Cerrar()
								out_ds.Destroy()
								print("\nFinalizado...")
							else:
								print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener los atributos del esquema y/o tabla.")

						else:
							print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener los atributos de la columna.")
	
					else:
						print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener el atributo de tipo de geometría.")
				else:
					print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener el atributo de ruta de SHP.")
			else: print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener el atributo del nombre del archivo ShapeFile.")
		except Exception as e:
			print("Error: "+str(e))	

	def PostgreSQL2SqlOracle(self, geografico, db):
		try:
			srid= self.objeto[geografico]['pg_srid']
			if srid is not None:				
				conexion_postgresql = Postgresql(usuario = self.configuracion[db]['usuario']
			                        , contrasena = self.configuracion[db]['contrasena']
			                        , servidor = self.configuracion[db]['servidor']
			                        , base_datos = self.configuracion[db]['base_datos'])

				columnas = self.objeto[geografico]['pg_columnas']
				if columnas is not None:
					lista_columnas = ""
					for i in columnas:
						lista_columnas = lista_columnas +"'{0}', ".format(i)

					pg_esquema = self.objeto[geografico]['pg_esquema']
					pg_tabla = self.objeto[geografico]['pg_tabla']
					if pg_esquema is not None and pg_tabla is not None:							
						consulta_sql = "SELECT {0} st_asbinary(shape) AS shape FROM {1}.{2} --WHERE objectid IN(3147,4037,4036)".format(lista_columnas.replace("'",""), pg_esquema, pg_tabla)
						datos = conexion_postgresql.Ejecutar(consulta_sql)

						lista_columnas = ""
						for i in columnas:
							lista_columnas = lista_columnas +"'{0}', ".format(i[:10])

						print("2. Extraendo datos de la tabla de PostgreSQL: {0}.{1}".format(pg_esquema,pg_tabla))
						if datos is not None:
							o_esquema = self.objeto[geografico]['o_esquema']
							o_tabla = self.objeto[geografico]['o_tabla']
							objectid= "sde.gdb_util.next_rowid('{0}', '{1}'), ".format(o_esquema,o_tabla)
							
							sql_insert = []
							with Bar("3. Preparando el Script SQL de Oracle: {0}".format(pg_tabla), max=len(datos), fill='█') as bar:
								for i in datos:
									geom = ogr.CreateGeometryFromWkb(i[len(columnas)])
									tipo_geometria =geom.GetGeometryName()
									wkt = geom.ExportToWkt()										
									total_caracteres=len(wkt)
									string_geom=""
									campo_geometrico=""

									if total_caracteres>3200:
										numero_interacciones= int(total_caracteres/3200)+1
										posicion_inicial=0
										posicion_final=0

										for j in range(numero_interacciones):                    
											posicion_inicial= 3200*j
											posicion_final=posicion_final + 3200
											string= wkt[posicion_inicial:posicion_final]
											string_geom = string_geom + "to_clob('" + string + "')||"

										string_geom = string_geom.strip()[:-2]

										if tipo_geometria == 'POINT':
											campo_geometrico ="SDE.ST_POINTFROMTEXT({0}, {1})".format(string_geom.strip(), srid)
										elif tipo_geometria == 'LINE':
											campo_geometrico ="SDE.ST_LINEFROMTEXT({0}, {1})".format(string_geom.strip(), srid)
										elif tipo_geometria == 'MULTILINE':
											campo_geometrico ="SDE.ST_MLINEFROMTEXT({0}, {1})".format(string_geom.strip(), srid)
										elif tipo_geometria == 'POLYGON':
											campo_geometrico ="SDE.ST_POLYFROMTEXT({0}, {1})".format(string_geom.strip(), srid)
										elif tipo_geometria == 'MULTIPOLYGON':
											campo_geometrico ="SDE.ST_MPOLYFROMTEXT({0}, {1})".format(string_geom.strip(), srid)

									else:
										string_geom=wkt
										if tipo_geometria == 'POINT':
											campo_geometrico ="SDE.ST_POINTFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
										elif tipo_geometria == 'LINE':
											campo_geometrico ="SDE.ST_LINEFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
										elif tipo_geometria == 'MULTILINE':
											campo_geometrico ="SDE.ST_MLINEFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
										elif tipo_geometria == 'POLYGON':
											campo_geometrico ="SDE.ST_POLYFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
										elif tipo_geometria == 'MULTIPOLYGON':
											campo_geometrico ="SDE.ST_MPOLYFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
									
									k=0
									script_sql= ""
									for columna in columnas:
										if columna == "objectid":
											script_sql = script_sql + objectid
										else:
											valor= str(i[k])
											if len(valor) == 0:
												script_sql = script_sql + "'None', "
											else:												 
												if valor.find("'") != -1:
													valor = valor.replace("'","''")
													script_sql = script_sql + "'{0}', ".format(valor)													
												else:													
													script_sql = script_sql + "'{0}', ".format(valor)
																								
										k=k+1
									script_sql = script_sql + campo_geometrico
									#sql = tuple(script_sql)										
									consulta = "INSERT INTO {0}.{1} ({2}, shape) VALUES ({3})".format(o_esquema
																		, o_tabla
																		, lista_columnas[:-2].replace("'",""), script_sql)
									sql_insert.append(consulta)										
									bar.next()
							
							return sql_insert					
					else:
						print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener los atributos del esquema y/o tabla.")
				else:
					print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener los atributos de la columna.")
			else:
				print ("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener el atributo SRID.")
		except Exception as e:
			print("Error: "+str(e))

	def PostGIS2ShapeFile(self, geografico, db):
		try:
			nombre = self.objeto[geografico]['nombre_shp']
			if nombre is not None:
				nombre_shp = "{0}\\{1}".format(self.objeto[geografico]['ruta_shp'], nombre + '.shp')

				if os.path.exists(self.objeto[geografico]['ruta_shp']):
					out_shapefile = ogr.GetDriverByName('ESRI Shapefile')
					out_ds = out_shapefile.CreateDataSource(nombre_shp)

					servidor = self.configuracion[db]['servidor']
					base_datos = self.configuracion[db]['base_datos']
					usuario = self.configuracion[db]['usuario']
					contrasena = self.configuracion[db]['contrasena']
					conexion= ogr.Open("PG: host={0} dbname={1} user={2} password={3}".format(servidor, base_datos, usuario, contrasena))
					if conexion is None:
					    print ("Error: No se pudo abrir una base de datos o GDAL no está instalado correctamente.")
					    sys.exit(1)
					else:
						driver = conexion.GetDriver()						
						esquema = self.objeto[geografico]['pg_esquema']
						tabla = self.objeto[geografico]['pg_tabla']
						print("1. Conectando al proveedor: {0}[{1}] Tabla:[{2}.{3}]".format(driver.name, servidor,esquema, tabla))
						capa = conexion.GetLayerByName("{0}.{1}".format(esquema, tabla))
						if capa is not None:
							proyeccion = capa.GetSpatialRef()							
							tipo_geometria = ogr.GeometryTypeToName(capa.GetGeomType())
							if tipo_geometria is not None:
								if tipo_geometria == "Point":
									out_layer = out_ds.CreateLayer(tabla, proyeccion, ogr.wkbPoint)
								if tipo_geometria == "Line":
									out_layer = out_ds.CreateLayer(tabla, proyeccion, ogr.wkbLineString)
								if tipo_geometria == "Polygon":
									out_layer = out_ds.CreateLayer(tabla, proyeccion, ogr.wkbPolygon)
								if tipo_geometria == "Multi Polygon":
									out_layer = out_ds.CreateLayer(tabla, proyeccion, ogr.wkbMultiPolygon)

								propiedades_capa = capa.GetLayerDefn()
								total_columnas = propiedades_capa.GetFieldCount()
								for columna in range(total_columnas):
									nombre_columna = propiedades_capa.GetFieldDefn(columna).GetName()
									if nombre_columna in ('SHAPE.STArea_', 'SHAPE.STLength_'):
										continue
									out_layer.CreateField(propiedades_capa.GetFieldDefn(columna))

								with Bar("2. Insertando datos al archivo Shape File: {0}.shp".format(nombre), max=len(capa), fill='█') as bar:
									for f in capa:
										shp = ogr.Feature(out_layer.GetLayerDefn())
										for i in range(total_columnas):
											nombre_columna = propiedades_capa.GetFieldDefn(i).GetName()
											shp.SetField(nombre_columna, f[i])

										shp.SetGeometry(f.GetGeometryRef())
										out_layer.CreateFeature(shp)
										bar.next()
								
								print("Finalizado")

							else: print("Error: No se tiene identificado el tipo de geometría")
						else: print("Error: No se tiene el tipo de capa identificado revisar archivo de ObjetosGeograficos.json")

					conexion.Destroy()
					out_ds.Destroy()
				else: print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener el atributo de ruta de SHP.")
			else: print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener el atributo del nombre del archivo ShapeFile.")
		except Exception as e:
			print("Error: "+str(e))	

	def PostGIS2SqlOracle(self, geografico, db):
		try:
			servidor = self.configuracion[db]['servidor']
			base_datos = self.configuracion[db]['base_datos']
			usuario = self.configuracion[db]['usuario']
			contrasena = self.configuracion[db]['contrasena']
			conexion= ogr.Open("PG: host={0} dbname={1} user={2} password={3}".format(servidor, base_datos, usuario, contrasena))
			if conexion is None:
				print ("Error: No se pudo abrir una base de datos o GDAL no está instalado correctamente.")
				sys.exit(1)
			else:
				driver = conexion.GetDriver()										
				pg_esquema = self.objeto[geografico]['pg_esquema']
				pg_tabla = self.objeto[geografico]['pg_tabla']
				print("1. Conectando al proveedor: {0}[{1}] Tabla:[{2}.{3}]".format(driver.name, servidor,pg_esquema, pg_tabla))
				capa = conexion.GetLayerByName("{0}.{1}".format(pg_esquema, pg_tabla))
				propiedades_capa = capa.GetLayerDefn()
				total_columnas = propiedades_capa.GetFieldCount()

				if total_columnas > 0:
					lista_columnas = ""
					existe_objectid = False
					for columna in range(total_columnas):
						nombre_columna = propiedades_capa.GetFieldDefn(columna).GetName()
						if nombre_columna == "objectid":
							existe_objectid= True
						lista_columnas = lista_columnas +"{0}, ".format(nombre_columna)

					print("2. Extraendo datos de la tabla de PostGIS: {0}.{1}".format(pg_esquema,pg_tabla))
					if capa is not None:
						o_esquema = self.objeto[geografico]['o_esquema']
						o_tabla = self.objeto[geografico]['o_tabla']
						objectid= "sde.gdb_util.next_rowid('{0}', '{1}'), ".format(o_esquema,o_tabla)
						
						proyeccion = capa.GetSpatialRef()
						srid=proyeccion.GetAuthorityCode("GEOGCS");
						#proyeccion.GetAuthorityName("GEOGCS");							
						tipo_geometria = ogr.GeometryTypeToName(capa.GetGeomType())
						
						sql_insert = []
						with Bar("3. Preparando el Script SQL de Oracle: {0}".format(pg_tabla), max=len(capa), fill='█') as bar:
							for i in capa:
								geom = i.GetGeometryRef()
								wkt = geom.ExportToWkt()										
								total_caracteres=len(wkt)
								string_geom=""
								campo_geometrico=""

								if total_caracteres>3200:
									numero_interacciones= int(total_caracteres/3200)+1
									posicion_inicial=0
									posicion_final=0

									for j in range(numero_interacciones):                    
										posicion_inicial= 3200*j
										posicion_final=posicion_final + 3200
										string= wkt[posicion_inicial:posicion_final]
										string_geom = string_geom + "to_clob('" + string + "')||"

									string_geom = string_geom.strip()[:-2]

									if tipo_geometria == 'Point':
										campo_geometrico ="SDE.ST_POINTFROMTEXT({0}, {1})".format(string_geom.strip(), srid)
									elif tipo_geometria == 'Line':
										campo_geometrico ="SDE.ST_LINEFROMTEXT({0}, {1})".format(string_geom.strip(), srid)
									elif tipo_geometria == 'Multi Line':
										campo_geometrico ="SDE.ST_MLINEFROMTEXT({0}, {1})".format(string_geom.strip(), srid)
									elif tipo_geometria == 'Polygon':
										campo_geometrico ="SDE.ST_POLYFROMTEXT({0}, {1})".format(string_geom.strip(), srid)
									elif tipo_geometria == 'Multi Polygon':
										campo_geometrico ="SDE.ST_MPOLYFROMTEXT({0}, {1})".format(string_geom.strip(), srid)
								else:
									string_geom=wkt
									if tipo_geometria == 'Point':
										campo_geometrico ="SDE.ST_POINTFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
									elif tipo_geometria == 'Line':
										campo_geometrico ="SDE.ST_LINEFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
									elif tipo_geometria == 'Multi Line':
										campo_geometrico ="SDE.ST_MLINEFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
									elif tipo_geometria == 'Polygon':
										campo_geometrico ="SDE.ST_POLYFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
									elif tipo_geometria == 'Multi Polygon':
										campo_geometrico ="SDE.ST_MPOLYFROMTEXT('{0}', {1})".format(string_geom.strip(), srid)
								
								k=0
								script_sql= ""
								for j in range(total_columnas):
									columna= propiedades_capa.GetFieldDefn(j).GetName()
									tipo_columna = ogr.GetFieldTypeName(propiedades_capa.GetFieldDefn(j).GetType())
									if columna == "objectid":
										script_sql = script_sql + objectid
									else:
										valor= str(i[k])
									
										if valor == 'None':											
											script_sql = script_sql + "NULL, "
										else:												 
											if valor.find("'") != -1:
												valor = valor.replace("'","''")
												script_sql = script_sql + "'{0}', ".format(valor)													
											else:
												if tipo_columna == "Integer64" or tipo_columna == "Integer" or tipo_columna == "Real":
													script_sql = script_sql + "{0}, ".format(valor)
												elif tipo_columna == "Date":
													script_sql = script_sql + "TO_DATE('{0}', 'YYYY/MM/DD'), ".format(valor)
												else:	
													script_sql = script_sql + "'{0}', ".format(valor)
																							
									k=k+1
								script_sql = script_sql + campo_geometrico
								#sql = tuple(script_sql)
								if existe_objectid:										
									consulta = "INSERT INTO {0}.{1} ({2}, shape) VALUES ({3})".format(o_esquema
																	, o_tabla
																	, lista_columnas[:-2], script_sql)
								else:
									consulta = "INSERT INTO {0}.{1} (objectid, {2}, shape) VALUES ({3} {4})".format(o_esquema
																	, o_tabla
																	, lista_columnas[:-2], objectid, script_sql)
								sql_insert.append(consulta)										
								bar.next()
						
						return sql_insert					
					else:
						print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener los atributos del esquema y/o tabla.")
				else:
					print("Error: Revisar el archivo de configuracionGDB.json, no se puede obtener los atributos de la columna.")
		except Exception as e:
			print("Error: "+str(e))

	def WFS2ShapeFile(self, tipo):
		try:
			nombre = self.servicio[tipo]['nombre_shp']

			if nombre is not None:
				nombre_shp = "{0}\\{1}".format(self.servicio[tipo]['ruta_shp'], nombre + '.shp')

				if os.path.exists(self.servicio[tipo]['ruta_shp']):
					out_shapefile = ogr.GetDriverByName('ESRI Shapefile')
					out_ds = out_shapefile.CreateDataSource(nombre_shp)

					direccion_web = self.servicio[tipo]['direccion_web']
					driver_wfs = ogr.GetDriverByName('WFS')
					#gdal.SetConfigOption('GML_INVERT_AXIS_ORDER_IF_LAT_LONG', 'NO')
					gdal.SetConfigOption("GDAL_HTTP_UNSAFESSL", "YES")
					gdal.VSICurlClearCache()

					wfs= driver_wfs.Open("WFS:" + direccion_web)
					if wfs is None:
					    print ("Error: No se tiene conexion al servicio: {0}".format(direccion_web))
					    sys.exit(1)
					else:
						driver = wfs.GetDriver()
						nombre_capa = self.servicio[tipo]['nombre_capa']
						print("1. Conectando al servicio {0} [{1}]".format(driver.name, nombre_capa))
						capa = wfs.GetLayerByName("{0}".format(nombre_capa))
						
						if capa is not None:
							proyeccion = capa.GetSpatialRef()
							#tipo_geometria = ogr.GeometryTypeToName(capa.GetGeomType())
							tipo_geometria = self.servicio[tipo]['tipo_geometria']
							geometria= None
							if tipo_geometria is not None:
								if tipo_geometria == "Punto":
									geometria= ogr.wkbPoint									
								if tipo_geometria == "Linea":
									geometria= ogr.wkbLineString
								if tipo_geometria == "MultiLinea":
									geometria= ogr.wkbMultiLineString
								if tipo_geometria == "Polygon":
									geometria = ogr.wkbPolygon
								if tipo_geometria == "MultiPolygon":
									geometria = ogr.wkbMultiPolygon

								if geometria is not None:
									out_layer = out_ds.CreateLayer("ShapeFile", proyeccion, geometria)
									propiedades_capa = capa.GetLayerDefn()
									total_columnas = propiedades_capa.GetFieldCount()
									for columna in range(total_columnas):
										nombre_columna = propiedades_capa.GetFieldDefn(columna).GetName()
										if nombre_columna in ('SHAPE.STArea_', 'SHAPE.STLength_'):
											continue
										elif nombre_columna in ('Shape.STArea__', 'Shape.STLength__'):
											continue
										out_layer.CreateField(propiedades_capa.GetFieldDefn(columna))

									with Bar("2. Insertando datos al archivo Shape File: {0}.shp".format(nombre), max=len(capa), fill='█') as bar:
										for f in capa:
											shp = ogr.Feature(out_layer.GetLayerDefn())
											for i in range(total_columnas):
												nombre_columna = propiedades_capa.GetFieldDefn(i).GetName()
												if nombre_columna in ('SHAPE.STArea_', 'SHAPE.STLength_'):
													continue
												elif nombre_columna in ('Shape.STArea__', 'Shape.STLength__'):
													continue
												shp.SetField(nombre_columna, f[i])

											shp.SetGeometry(f.GetGeometryRef())
											out_layer.CreateFeature(shp)
											bar.next()
								else:
									print("Error: No se tiene identificado el campo geometrico.")
								print("Finalizado")

							else: print("Error: No se tiene identificado el tipo de geometría")
						else: print("Error: No se tiene el tipo de capa identificado revisar archivo de Servicios.json")

					out_ds.Destroy()
				else: print("Error: Revisar el archivo de Servicios.json, no se puede obtener el atributo de ruta de SHP.")
			else: print("Error: Revisar el archivo de Servicios.json, no se puede obtener el atributo del nombre del archivo ShapeFile.")
		except Exception as e:
			print("Error: "+str(e))

	def OgcWFS2SqlOracle(self, tipo):
		pass

	def ArcGISRest2ShapeFile(self, tipo):
		pass

	def ArcGISRest2SqlOracle(self, tipo):
		pass