import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.tooltip import MDTooltip


class Inventario(Screen):
    def __init__(self, **kwargs):
        super(Inventario, self).__init__()
        self.app = MDApp.get_running_app()

    def on_pre_enter(self, **args):
        self.app.title = "Inventario"


class Wid_Alfa(GridLayout):
    None


class Wid_Inventario(GridLayout):
    None


class Wid_Alfa2(GridLayout):
    None


class Ala(BoxLayout):
    pass



