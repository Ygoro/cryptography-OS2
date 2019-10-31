from imports import *
Builder.load_file('main.kv')
Window.size = (500, 500)

class KeyCreationScreen(Screen):

    def createSecretKey(self):
        secretKey = get_random_bytes(32)
        file_out = open("files/secretKey.txt", "wb")
        file_out.write(secretKey)
        file_out.close()
        print("Tajni ključ uspješno upisan u datoteku secretKey.txt")

    def createPublicKey(self):
        privateKey = RsaKeypair(2048)
        publicKey = privateKey.publickey
        file_out = open("files/publicKey.txt", "wb")
        file_out.write(publicKey.serialize())
        file_out.close()
        print("Javni ključ uspješno upisan u datoteku publicKey.txt")

    def createPrivateKey(self):
        privateKey = RsaKeypair(2048)
        file_out = open("files/privateKey.txt", "wb")
        file_out.write(privateKey.serialize())
        file_out.close()
        print("Privatni ključ uspješno upisan u datoteku privateKey.txt")

class InputEncryptionScreen(Screen):

    def encryptTextInput(self):
         input = self.ids.my_textinput.text
         file_out = open("files/message.txt", "w")
         file_out.write(input)
         file_out.close()
         print("Poruka uspješno upisana u datoteku message.txt")

class EncryptionScreen(Screen):

    def encryptAES(self):
        file_in_text = open("files/message.txt", "r")
        rawText = file_in_text.read()
        file_in_text.close()

        file_in_key = open("files/secretKey.txt", "rb")
        rawKey = file_in_key.read().decode("utf8")
        file_in_key.close()

        #tu kod

        file_out = open("files/encryptedAES.txt", "wb")

        print("Uspješno kriptirana poruka pohranjena u encryptedAES.txt")
        print(citext)

class DecryptionScreen(Screen):
    pass

class MessageHashCalculationScreen(Screen):
    pass

class DigitalSignatureScreen(Screen):
    pass

sm = ScreenManager(transition=NoTransition())
sm.add_widget(KeyCreationScreen(name='kljucevi'))
sm.add_widget(InputEncryptionScreen(name='tekst'))
sm.add_widget(EncryptionScreen(name='kriptiranje'))
sm.add_widget(DecryptionScreen(name='dekriptiranje'))
sm.add_widget(MessageHashCalculationScreen(name='sazetak'))
sm.add_widget(DigitalSignatureScreen(name='potpis'))

class OS2CryptographyProject(App):
    def build(self):
        return sm

if __name__ == '__main__':
    OS2CryptographyProject().run()
