import os   # Paquete para las funciones que requieren recursos del OS
import sqlite3 # biblioteca de la base de datos

APP_PATH = os.getcwd() # obtiene la dirección donde se úbican los archivos .py y .kv
DB_PATH = APP_PATH+'/database.db' # crea la base de datos

##******************** Base de datos - Creación ********************##
########### Conexión a la base de Datos ###########
def conexion_database(path):
    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        
        crea_tabla_login(cursor)
        crea_tabla_inventario(cursor)
        crea_tabla_categoria(cursor)        
        crea_tabla_producto(cursor)
        
        connection.commit()
        connection.close()
    except Exception as e:
        print(e)    
#
############# Creamos las tablas en la base de datos #############
#
def crea_tabla_login(cursor):
    cursor.execute(login)
def crea_tabla_inventario(cursor):
    cursor.execute(comando1)
def crea_tabla_categoria(cursor):
    cursor.execute(comando2)
def crea_tabla_producto(cursor):
    cursor.execute(comando3)


        # Tabla login #
login = """ CREATE TABLE IF NOT EXISTS 
LOGIN(
    id          INTEGER     PRIMARY KEY,
    user_L    TEXT                    NOT NULL,
    email_L     TEXT                    NOT NULL,
    password    TEXT                    NOT NULL
)   """

        # Tabla inventario #
comando1 = """ CREATE TABLE IF NOT EXISTS 
INVENTARIOS(
    id        INTEGER    PRIMARY KEY,
    nombre_I    TEXT                    NOT NULL
)   """

        # Tabla categoria #
comando2 = """ CREATE TABLE IF NOT EXISTS
CATEGORIAS(
    id         INTEGER     PRIMARY KEY,
    nombre_C     TEXT,
    idinventario        INTEGER 
    
)   """

        # Tabla productos #
comando3 = """ CREATE TABLE IF NOT EXISTS
PRODUCTOS(
    id          INTEGER     PRIMARY KEY,
    nombre_P    TEXT                NOT NULL,
    precio      FLOAT               NOT NULL,
    cantidad    INTEGER,
    fecha       DATE,
    id_inventario integer REFERENCES INVENTARIOS(id),
    id_categoria integer REFERENCES CATEGORIAS(id)
    
    
)   """

##******************** Termina creación Base de datos ********************##
