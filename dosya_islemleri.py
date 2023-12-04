"""dosya1=open("ilkDosya.txt","r")
dosya2=open("ilkDosyaTasi.txt","w")

icerik=dosya1.read()
icerik=icerik.upper()
dosya2.write(icerik)

dosya1.close()
dosya2.close()"""
dosya1=open("ilkDosya.txt","r")
dosya2=open("ilkDosyaTasi.txt","w")
icerik=dosya1.readlines()
istenen="yuzuklerin efendisi"
sayac=0
for x in icerik:
    isim,tarih,puan=x.split(",")
    if istenen==isim:
        sayac=1
        print("film: {} tarih: {} puan: {}".format(isim,tarih,puan))
if sayac==0:
    print("aradiginiz film bulunamadi")

dosya2.close()
dosya1.close()