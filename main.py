from imports import *

Builder.load_file("main.kv")
Window.size = (500, 500)

def ReadMessageFromFile(self):
    f_text = open("files/message.txt", "r")
    text = f_text.read()
    f_text.close()
    return text

def CalculateHash(self):
    return hash(ReadMessageFromFile(self))

class KeyCreationScreen(Screen):

    def createSecretKey(self):
        secretKey = get_random_bytes(32)
        f = open("files/secretKey.txt", "wb")
        f.write(secretKey)
        f.close()

        print("Tajni ključ uspješno upisan u datoteku secretKey.txt")

    def createRSAKeys(self):
        privateKey = RsaKeypair(2048)
        f = open("files/privateKey.txt", "wb")
        f.write(privateKey.serialize())
        f.close()

        publicKey = privateKey.publickey
        f = open("files/publicKey.txt", "wb")
        f.write(publicKey.serialize())
        f.close()

        print("Javni i privatni ključ uspješno upisani u datoteke publicKey.txt i privateKey.txt")

class InputEncryptionScreen(Screen):

    def encryptTextInput(self):
         input = self.ids.my_textinput.text
         f = open("files/message.txt", "w")
         f.write(input)
         f.close()
         print("Poruka uspješno upisana u datoteku message.txt")

class EncryptionScreen(Screen):

    def encryptAES(self):
        text = ReadMessageFromFile(self)
        f_key = open("files/secretKey.txt", "rb")
        key = AesKey(f_key.read())
        f_key.close()

        encryptedMessage = key.encrypt(text)

        f_aes = open("files/encryptedAES.txt", "w")
        f_aes.write(encryptedMessage)
        f_aes.close()

        print("Uspješno kriptirana poruka pohranjena je u datoteku encryptedAES.txt")

    def encryptRSA(self):
        text = ReadMessageFromFile(self)
        f_key = open("files/publicKey.txt", "rb")
        key = RsaPublicKey(f_key.read())
        f_key.close()

        encryptedMessage = key.encrypt(text)

        f_rsa = open("files/encryptedRSA.txt", "w")
        f_rsa.write(encryptedMessage)
        f_rsa.close()

        print("Uspješno kriptirana poruka pohranjena je u datoteku encryptedRSA.txt")

class DecryptionScreen(Screen):

    def decryptAES(self):
        f_message = open("files/encryptedAES.txt", "r")
        encryptedMessage = f_message.read()
        f_message.close()

        f_key = open("files/secretKey.txt", "rb")
        key = AesKey(f_key.read())
        f_key.close()

        decryptedMessage = key.decrypt(encryptedMessage).decode("utf-8")

        print("Poruka dekriptirana simetričnim algoritmom je: " + str(decryptedMessage))

    def decryptRSA(self):
        f_message = open("files/encryptedRSA.txt", "r")
        encryptedMessage = f_message.read()
        f_message.close()

        f_key = open("files/privateKey.txt", "r")
        key = RsaKeypair(f_key.read())
        f_key.close()

        decryptedMessage = key.decrypt(encryptedMessage).decode("utf-8")

        print("Poruka dekriptirana asimetričnim algoritmom je: " + str(decryptedMessage))

class MessageHashCalculationScreen(Screen):

    def writeHashToFile(self):
        calculatedHash = CalculateHash(self)
        f_hash = open("files/hash.txt", "w")
        f_hash.write(calculatedHash)
        f_hash.close()

        print("Uspješno kreiran sažetak SHA-256 algoritmom nalazi se u datoteci hash.txt")

class DigitalSignatureScreen(Screen):

    def createDigitalSignature(self):
        calculatedHash = CalculateHash(self)
        f_key = open("files/privateKey.txt", "r")
        key = RsaKeypair(f_key.read())
        f_key.close()

        digitalSignature = key.sign(calculatedHash)

        f_signature = open("files/digitalSignature.txt", "wb")
        f_signature.write(digitalSignature)
        f_signature.close()

        print("Uspješno kreiran digitalni potpis nalazi se u datoteci digitalSignature.txt")

    def checkDigitalSignature(self):
        calculatedHash = CalculateHash(self)
        f_key = open("files/publicKey.txt", "rb")
        key = RsaPublicKey(f_key.read())
        f_key.close()

        f_signature = open("files/digitalSignature.txt", "rb")
        digitalSignature = f_signature.read()
        f_signature.close()

        validSignature = key.verify(calculatedHash, digitalSignature)

        if(validSignature == True):
            print("Potpis je valjan.")
        else:
            print("Potpis nije valjan.")

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
