from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

# Importar funciones
from data_inv.db import *
from data_inv.db_signup import *

class Welcome(Screen):
    def __init__(self, **kwargs):
        super(Welcome, self).__init__()

    def crear_database(self):
        conexion_database(DB_PATH)


class Wel_Registro(Screen):
    def __init__(self, **kwargs):
        super(Wel_Registro, self).__init__()

    def regis(self):
        singup(self)


class Wel_Login(Screen):
    def __init__(self, **kwargs):
        super(Wel_Login, self).__init__()