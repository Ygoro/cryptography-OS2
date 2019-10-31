from imports import *
Builder.load_file('main.kv')
Window.size = (500, 500)

class KeyCreationScreen(Screen):

    def secretKeyCreation(self):
        secretKey = get_random_bytes(32)
        file_out = open("files/secretKey.txt", "wb")
        file_out.write(secretKey)
        file_out.close()
        #cipher = AES.new(secretKey, AES.MODE_EAX)
        print("Tajni ključ uspješno upisan u datoteku secretKey.txt")

    def publicKeyCreation(self):
        publicKey = RSA.generate(2048)
        file_out = open("files/publicKey.txt", "wb")
        file_out.write(publicKey.publickey().export_key('PEM'))
        file_out.close()
        print("Javni ključ uspješno upisan u datoteku publicKey.txt")

    def privateKeyCreation(self):
        privateKey = RSA.generate(2048)
        file_out = open("files/privateKey.txt", "wb")
        file_out.write(privateKey.export_key('PEM'))
        file_out.close()
        print("Privatni ključ uspješno upisan u datoteku privateKey.txt")

class EncryptionInputScreen(Screen):
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
sm.add_widget(EncryptionInputScreen(name='tekst'))
sm.add_widget(EncryptionScreen(name='kriptiranje'))
sm.add_widget(DecryptionScreen(name='dekriptiranje'))
sm.add_widget(MessageHashCalculationScreen(name='sazetak'))
sm.add_widget(DigitalSignatureScreen(name='potpis'))

class OS2CryptographyProject(App):
    def build(self):
        return sm

if __name__ == '__main__':
    OS2CryptographyProject().run()
