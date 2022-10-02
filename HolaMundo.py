import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.button import Label

class MiAplicacion(App):
    def build(self):
        return Label(text='Hola Mundo')
if __name__ == '__main__':
   MiAplicacion().run()