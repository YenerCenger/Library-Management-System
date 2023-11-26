import sqlite3

import time

class Kitap():

    def __init__(self,isim,yazar,yayınevi,tür,baskı,sayfa_sayısı):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı
        self.sayfa_sayısı = sayfa_sayısı

    def __str__(self):

        return "Kitap ismi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\nSayfa Sayısı: {}\n".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı,self.sayfa_sayısı)


class Kütüphane():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kütüphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table IF NOT EXISTS kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT,sayfa_sayısı INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def kitapları_goster(self):

        sorgu = "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Bu kütüphanede herhangi bir kitap bulunmuyor.")

        else:
            for i in kitaplar:

                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Böyle Bir kitap bulunmuyor.")

        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)

    def kitap_ekle(self,kitap):

        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))

        self.baglanti.commit()

    def kitap_sil(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        kitap = self.cursor.fetchall()

        if len(kitap) == 0:
            print("Böyle Bir kitap bulunmuyor.")

        else:
            sorgu = "Delete From kitaplar where isim = ?"

            self.cursor.execute(sorgu, (isim,))

            self.baglanti.commit()


    def baskı_arttır(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Böyle Bir kitap bulunmuyor.")
            False

        else:
            baskı = kitaplar[0][4]
            baskı += 1

            sorgu = "Update kitaplar set baskı = ? where isim = ?"

            self.cursor.execute(sorgu,(baskı,isim))

            self.baglanti.commit()

    def yayınevi_değiştir(self,isim,yeni_yayınevi):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitap = self.cursor.fetchall()

        if len(kitap) == 0:
            print("Böyle Bir kitap bulunmuyor.")

        else:
            sorgu = "Update kitaplar set yayınevi = ? where isim = ?"

            self.cursor.execute(sorgu,(yeni_yayınevi, isim))

            self.baglanti.commit()





