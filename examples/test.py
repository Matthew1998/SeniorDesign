
# import kivy module
import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# A Widget is the base building block
# of GUI interfaces in Kivy.
# It provides a Canvas that
# can be used to draw on screen.
from kivy.uix.widget import Widget

# From graphics module we are importing
# Rectangle and Color as they are
# basic building of canvas.
from kivy.graphics import Rectangle, Color

# class in which we are creating the canvas
class CanvasWidget(Widget):

    def __init__(self, **kwargs):

        super(CanvasWidget, self).__init__(**kwargs)

        # Arranging Canvas
        with self.canvas:

            # Seting the size and position of image
            # image must be in same folder
            self.rect = Rectangle(source ='IMG_1414.jpg',
                                  pos = self.pos, size = self.size)

            # Update the canvas as the screen size change
            # if not use this next 5 line the
            # code will run but not cover the full screen
            self.bind(pos = self.update_rect,
                  size = self.update_rect)

    # update function which makes the canvas adjustable.
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

# Create the App Class
class CanvasApp(App):
    def build(self):
        return CanvasWidget()

# run the App
CanvasApp().run()

