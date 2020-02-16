# This file will contain the UI that is used to demonstrate the lugnut 
import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
sm = ScreenManager()

def switchScreen(instance):
    sm.transition.direction = 'left'
    if instance.id == 'menu':
        sm.transition.direction = 'right'
    sm.current = instance.id

def runDemo(instance):
    sourcestr = "/home/seniordesign/Desktop/SeniorDesign/lugnutDetection/images/" + instance.id
    

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        optionGrid = GridLayout()
        optionGrid.cols = 1
        optionGrid.padding = 10
        optionGrid.spacing = 10
        optionGrid.size_hint = (0.5, 1)
        optionGrid.pos_hint = {'x':0.25, 'y':0}
        optionGrid.row_force_default = True
        optionGrid.row_default_height = 150


        btn = Button(text="Lab Demo", id='labDemo')
        btn.bind(on_press=switchScreen)
        optionGrid.add_widget(btn)

        self.add_widget(optionGrid)

class LabDemoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        backBtn = Button(text="Back", id='menu', size_hint=(0.25, 0.105), pos=(10, 10))
        backBtn.bind(on_press=switchScreen)
        self.add_widget(backBtn)

        self.scroller = ScrollView()
        self.scroller.size_hint = (0.25, 0.85)
        self.scroller.pos_x = 10
        self.scroller.pos_hint = {'x':0, 'y':0.15}

        self.imageGrid = GridLayout()
        self.imageGrid.cols = 1
        self.imageGrid.spacing = 10
        self.imageGrid.padding = 10
        self.imageGrid.size_hint = (1, None)
        self.imageGrid.row_force_default = True
        self.imageGrid.row_default_height = 150

        size = self.initPictureButtons()

        self.imageGrid.height = (size*160)+10

        self.scroller.add_widget(self.imageGrid)
        self.add_widget(self.scroller)



    def initPictureButtons(self):
        images = os.listdir('/home/seniordesign/Desktop/SeniorDesign/lugnutDetection/images/')
        images.sort()
        for file in images:
            btn = Button(text=file, id=file)
            btn.bind(on_press=runDemo)
            self.imageGrid.add_widget(btn)
        return len(images)





sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LabDemoScreen(name='labDemo'))
sm.current='menu'

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()
