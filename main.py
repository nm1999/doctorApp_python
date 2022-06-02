from cgitb import text
from tkinter import Widget
from kivy.app import App
from kivy.uix.button import Button 
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (380, 600)
import lib

KV ="""

MDNavigationLayout:

    ScreenManager:
        

        Screen:
            orientation: 'vertical'
            
            MDToolbar:
                title: "BeaconDoctor App"
                elevation: 10
                pos_hint:{"center_y":.95,"center_x":.5}
                left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

            MDIconButton:
                icon:"microphone"                                
                user_font_size: "120sp"
                on_press:root.conserve()                        
                size_hint:(.5, .5)
                pos_hint:{"center_y":.5,"center_x":.5}
            
            MDLabel:
                text:"Contact the hospital"
                pos_hint:{"center_y":.1,"center_x":.8}

                    
                    
    MDNavigationDrawer:
        id: nav_drawer

        ScrollView:
            MDList:
                OneLineAvatarIconListItem:
                    text:"item one"
                    IconLeftWidget:
                        icon: "coffee"

                OneLineAvatarIconListItem:
                    text:"item two"
                    IconLeftWidget:
                        icon: "trash"

                OneLineAvatarIconListItem:
                    text:"item three"
                    IconLeftWidget:
                        icon: "android"

                OneLineAvatarIconListItem:
                    text:"item four"
                    IconLeftWidget:
                        icon: "language-python"

"""
class MDNavigationLayout(BoxLayout):
    # def conserve(self):
    #     print("Welcome")
        # lib.converse()
    pass

class doctorApp(MDApp):

    def build(self):
        screen = Builder.load_string(KV)
        return screen

doctorApp().run()