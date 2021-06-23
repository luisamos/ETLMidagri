import psycopg2

class Postgresql():
    p_usuario = None
    p_contrasena = None
    p_servidor = None
    p_base_datos = None    
    p_conexion = None

    def __init__(self, usuario, contrasena, servidor, base_datos):
        
        self.p_usuario = usuario
        self.p_contrasena = contrasena
        self.p_servidor = servidor
        self.p_base_datos = base_datos

        try:
          self.p_conexion = psycopg2.connect(user=self.p_usuario
                                      , password=self.p_contrasena
                                      , host=self.p_servidor
                                      , database=self.p_base_datos)          
          self.p_conexion.autocommit = False
          
          print("\n1. Conectado a la base de datos PostgreSQL: {0}/[{1}]".format(self.p_servidor, self.p_base_datos))
          
        except psycopg2.Error as error:            
            print("\nError: "+str(error))

    def Ejecutar(self, consulta):
        try:
            cursor = self.p_conexion.cursor()
            cursor.execute(consulta)
            #self.p_conexion.commit()
            return cursor.fetchall()
        except psycopg2.Error as error:
            print("\nError: "+str(error))
            return None
        
    def EjecutarParametros(self, consulta, parametros):
        cursor = self.p_conexion.cursor()
        cursor.execute(consulta, parametros)
    
    def EjecutarArreglo( self, consulta, arreglo):
        cursor = self.p_conexion.cursor()
        cursor.executemany(consulta, arreglo)
    
    def Confirmar(self):        
        self.p_conexion.commit()

    def Cerrar(self):
        self.p_conexion.close()