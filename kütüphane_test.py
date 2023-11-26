import time

from kütüphane import *

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler:

1-Kitapları Göster

2-Kitap Sorgula

3-Kitap Ekle

4-Kitap Sil

5-Baskı Arttır

6-Yayınevi Değiştirme

çıkış içim 'q' ya basın
***********************************
""")

kütüphane = Kütüphane()

while True:

    işlem = input("Yapacağınız İşlem:")

    if işlem == "q":
        print("Program Sonlandırılıyor")
        print("Yine Bekleriz...")
        kütüphane.baglanti_kes()
        break

    elif işlem == "1":
        kütüphane.kitapları_goster()

    elif işlem == "2":
        isim = input("Hangi Kitabı Arıyorsunuz:")
        print("Kitap Sorgulanıyor..")
        time.sleep(1)

        kütüphane.kitap_sorgula(isim)

    elif işlem == "3":
        isim = input("Kitabın Adı:")
        yazar = input("Kitabın Yazarı:")
        yayınevi = input("Kitabın Yayınevi:")
        tür = input("Kitabın Türü:")
        baskı = int(input("Kitabın Baskısı:"))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Kitap Ekleniyor...")
        time.sleep(1)

        kütüphane.kitap_ekle(yeni_kitap)

        print("Kitap Eklendi.")

    elif işlem == "4":
        isim = input("Silmek İstediğiniz Kitabın Adını Girin:")

        cevap = input("{} adlı kitabı silmek istediğinize emin misiniz? (E/H)".format(isim))

        if (cevap == "E"):
            print("Kitap Siliniyor...")
            time.sleep(1)
            kütüphane.kitap_sil(isim)
            if not kütüphane.kitap_sil(isim):
                print("Lütfen kütüphanede olan bir kitap girin.")
            else:
                print("Kitap Silindi")

    elif işlem == "5":
        isim = input("Hangi Kitabın Baskısını Yükseltmek İstersiniz?")
        print("Baskı Yükseltiliyor..")
        time.sleep(1)
        kütüphane.baskı_arttır(isim)
        print("Baskı Yükseltildi.")

    elif (işlem == "6"):
        isim = input("Yayınevini değiştimek istediğiniz kitabın adını girin:")
        yeni_yayınevi = input("Hangi yayınevi Olarak Değiştireceksiniz:")

        kütüphane.yayınevi_değiştir(isim,yeni_yayınevi)


    else:
        print("Geçersiz işlem...")

