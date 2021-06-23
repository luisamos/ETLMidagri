import cx_Oracle

class Oracle():
    
    p_usuario = None
    p_contrasena = None
    p_servidor = None
    p_sid = None
    p_puerto = None
    p_conexion = None
    p_numero = None

    def __init__(self, usuario, contrasena, servidor, puerto, sid, numero):
        
        self.p_usuario = usuario
        self.p_contrasena = contrasena
        self.p_servidor = servidor
        self.p_sid = sid
        self.p_puerto = puerto
        self.p_numero = numero

        #cadena_conexion = self.p_usuario + "/" + self.p_contrasena + "@" + self.p_servidor + ":" + self.p_puerto + "/" + self.p_sid
        dsn_tns = cx_Oracle.makedsn(self.p_servidor, self.p_puerto, self.p_sid)
        
        try:
          conexion = cx_Oracle.connect(self.p_usuario, self.p_contrasena, dsn_tns)          
          conexion.autocommit = False    
          
          print("{0}. Conectado a la base de datos Oracle versión ({1}): {2}/{3}".format(self.p_numero, conexion.version, self.p_servidor, self.p_sid))
          self.p_conexion = conexion          
          
        except cx_Oracle.Error as error:
            print("\nError: "+error.message)

    def Ejecutar(self, consulta):
        try:
            cursor = self.p_conexion.cursor()
            cursor.execute(consulta)

        except cx_Oracle.Error as error:
            print("\nError: "+str(error))
            print("\n"+consulta)
        
    def EjecutarParametros(self, consulta, parametros):
        cursor = self.p_conexion.cursor()
        cursor.execute(consulta, parametros)

    def EjecutarArreglo( self, consulta, datos):
        cursor = self.p_conexion.cursor()
        cursor.executemany(consulta, datos)

    def ExisteTabla(self, esquema, tabla):
        cursor = self.p_conexion.cursor()
        consulta = "SELECT count(*) FROM all_tables WHERE owner = '{0}' AND table_name='{1}'".format(esquema, tabla.upper())
        datos = cursor.execute(consulta)
        return cursor.fetchall()

    def Confirmar(self):        
        self.p_conexion.commit()

    def Cerrar(self):
        self.p_conexion.close()