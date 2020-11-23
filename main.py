# Importar librerías
import os # Paquete para las funciones que requieren recursos del OS


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

# Importar Pantallas
from baseclass.settingsscreen import SettingsScreen
from baseclass.welcome import Welcome, Wel_Registro, Wel_Login
from baseclass.inventario import Inventario
from baseclass.inventario import *


Builder.load_file('main.kv')

class TTMain_ScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(TTMain_ScreenManager, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()
class Index(Screen):
    def __init__(self, **kwargs):
        super(Index,self).__init__(**kwargs)
        self.app = MDApp.get_running_app()

# Inicialización de la APP
class MyApp(MDApp):

    # Constructor
    def build(self):
        # Ajustes adicionales
        self.title = "TT2 2019-B014"
        self.theme_cls.primary_palette = "Green"
        # Carga del archivo kivy
        return TTMain_ScreenManager()

# Ejecutar App
MyApp().run()