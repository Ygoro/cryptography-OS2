from imports import *
Builder.load_file('main.kv')
Window.size = (500, 500)

class KeyCreationScreen(Screen):
    def secretKeyCreation(self):
        secretKey = get_random_bytes(32)
        print(secretKey)
    def publicKeyCreation(self):
        publicKey = get_random_bytes(32)
        print(publicKey)
    def privateKeyCreation(self):
        privateKey = get_random_bytes(32)
        print(privateKey)

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
