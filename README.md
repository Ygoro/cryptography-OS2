# OS2 Python cryptography

Mini aplikacija za kolegij Operacijski sustavi 2, koja korisniku omogućuje osnovne kriptografske radnje.
Sučelje aplikacije izrađeno je python bibliotekom [Kivy](https://pypi.org/project/Kivy/), pri čemu je mnogo pomogla dokumentacija vezana uz [kv jezik za stiliziranje](https://kivy.org/doc/stable/guide/lang.html), dok su bibliotekom [simplecrypto](https://pypi.org/project/simplecrypto/) implementirane kriptografske funkcionalnosti.

## Upute za korištenje
Svaki zaslon u aplikaciji ima implementirane **gumbe za prijelaz iz zaslona u zaslon**. Ti gumbi nalaze se na dnu sučelja te se na njima nalazi tekst _<--_ ili/i _-->_ uz pomoć kojih se kreće kroz zaslone aplikacije.

Sve funkcionalnosti aplikacije u nastavku su označene **ovako**, dok su sve datoteke i tekst iz konzole označeni _ovako_.

1. Aplikacija se u virtualnom okruženju pokreće pozicioniranjem u klonirani direktorij i pokretanjem _**main.py**_.

2. Pokretanjem aplikacije dolazi se do početnog sučelja na kojem je moguće pritiskom na gumbe _Tajni ključ_ i _Javni i privatni ključ_ **stvoriti nove ključeve za kriptiranje** (ključevi će biti smješteni u datoteke _secretKey.txt_, _publicKey.txt_ i _privateKey.txt).

- Generiranjem ključeva u konzoli se ispisuju poruke: _Tajni ključ uspješno upisan u datoteku secretKey.txt_ tj. _Javni i privatni ključ uspješno upisani u datoteke publicKey.txt i privateKey.txt_ ovisno o tome koji ključevi su generirani

3. Nakon kreiranja ključeva pritiskom na gumb _-->_ moguće je doći na sljedeći zaslon aplikacije u kojem **korisnik unosi tekst za kriptiranje**. Pritiskom na gumb _Upiši u datoteku_ uneseni tekst zapisuje se u datoteku _message.txt_.

- Unosom teksta poruke u konzoli se ispisuje: _Poruka uspješno upisana u datoteku message.txt_

4. Sljedeći zaslon je posvećen **kriptiranju unesene poruke generiranim ključevima**. Pritiskom na gumb _Simetričnim algoritmom_ poruka se kriptira AES algoritmom za kriptiranje, dok se pritiskom na gumb _Asimetričnim algoritmom_ poruka kriptira RSA algoritmom (kriptirana poruka određenim algoritmom nalazi se u datotekama _encryptedAES.txt_ i _encryptedDES.txt_).

- Kriptiranjem poruke u konzoli se ispisuje: _Uspješno kriptirana poruka pohranjena je u datoteku encryptedAES.txt_ za simetrično kriptiranje tj. _Uspješno kriptirana poruka pohranjena je u datoteku encryptedRSA.txt_ za asimetrično kriptiranje

5. Slijedi zaslon za **dekriptiranje unesene poruke** na kojem se nalaze isti gumbi kao na prijašnjem zaslonu, a služe za dekriptiranje poruke. Dekriptirana poruka ispisuje se u konzoli u kojoj je pokrenuta aplikacija, npr:

- _Poruka dekriptirana simetričnim algoritmom je: Tekst poruke_ kao primjer za dekriptiranje simetričnim algoritmom
- _Poruka dekriptirana asimetričnim algoritmom je: Tekst poruke_ kao primjer za dekriptiranje asimetričnim algoritmom

6. Sljedeći zaslon daje mogućnost **izračunavanja sažetka na temelju unesene poruke**. Pritiskom na gumb _Izračunaj_ generira se sažetak funkcijom za hashiranje SHA-256 i isti se pohranjuje u datoteku _hash.txt_.

- Generiranjem sažetka u konzolu se ispisuje tekst: _Uspješno kreiran sažetak SHA-256 algoritmom nalazi se u datoteci hash.txt_

7. Posljednji zaslon sadrži implementaciju **digitalnog potpisivanja poruke kreiranim sažetkom**, koji se generira pritiskom na gumb _Potpiši_. Digitalno potpisan tekst sprema se u datoteku _digitalSignature.txt_. Osim toga moguće je **provjeriti generirani potpis** pritiskom na gumb _Provjeri_, pri čemu se provjerava da li je promijenjena poruka ili sam potpis.

- Generiranjem digitalnog potipsa u konzolu se ispisuje: _Uspješno kreiran digitalni potpis nalazi se u datoteci digitalSignature.txt_

- Ispravnim rezultatom provjere digitalno potpisane poruke u konzolu se ispisuje: _Potpis je valjan._

- Neispravnim rezultatom provjere digitalno potpisane poruke u konzolu se ispisuje: _Potpis nije valjan._

