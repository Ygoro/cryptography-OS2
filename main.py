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
        text = file_in_text.read()
        file_in_text.close()

        file_in_key = open("files/secretKey.txt", "rb")
        key = AesKey(file_in_key.read())
        file_in_key.close()

        message = key.encrypt(text)

        file_out = open("files/encryptedAES.txt", "w")
        file_out.write(message)
        file_out.close()

        print("Uspješno kriptirana poruka pohranjena u encryptedAES.txt")

class DecryptionScreen(Screen):
    def decryptAES(self):
        file_in_message = open("files/encryptedAES.txt", "r")
        encryptedMessage = file_in_message.read()
        file_in_message.close()

        file_in_key = open("files/secretKey.txt", "rb")
        key = AesKey(file_in_key.read())
        file_in_key.close()

        decryptedMessage = key.decrypt(encryptedMessage).decode("utf-8")

        print("Poruka dekriptirana simetričnim algoritmom je: " + str(decryptedMessage))

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
