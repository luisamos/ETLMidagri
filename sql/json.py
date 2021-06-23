from osgeo import gdal, ogr
import wget

#url = "https://geo.serfor.gob.pe/geoservicios/rest/services/Servicios_OGC/Modalidad_Acceso/MapServer/6/query?where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&having=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&queryByDistance=&returnExtentOnly=false&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&f=geojson"

#wget.download(url, r'C:\Users\luisamos\Downloads\6.json')

#geojson = '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[146.7,-41.9]}}]}'
#ds = gdal.OpenEx(geojson)

ds = ogr.Open("6.geojson")
driver = ds.GetDriver()
capa = ds.GetLayer()
proyeccion = capa.GetSpatialRef()
#feature = layer.GetFeature(0)

#print("\n"+driver.GetName())
print(proyeccion)


#print(feature.GetGeometryRef())

propiedades_capa = capa.GetLayerDefn()
total_columnas = propiedades_capa.GetFieldCount()
#print(total_columnas)