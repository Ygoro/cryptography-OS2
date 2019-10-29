from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
Builder.load_file('main.kv')
from kivy.core.window import Window
Window.size = (500, 500)

class KeyCreationScreen(Screen):
    pass

class EncryptionScreen(Screen):
    pass

class DecryptionScreen(Screen):
    pass

class MessageHashCalculationScreen(Screen):
    pass

class DigitalSignatureScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(KeyCreationScreen(name='kljucevi'))
sm.add_widget(EncryptionScreen(name='kriptiranje'))
sm.add_widget(DecryptionScreen(name='dekriptiranje'))
sm.add_widget(MessageHashCalculationScreen(name='sazetak'))
sm.add_widget(DigitalSignatureScreen(name='potpis'))

class OS2CryptographyProject(App):
    def build(self):
        return sm

if __name__ == '__main__':
    OS2CryptographyProject().run()
