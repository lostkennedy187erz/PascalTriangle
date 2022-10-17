#İBRAHİM ÇELEN
#B201200014
#SAYISAL ANALİZ
#BİLİŞİM SİSTEMLERİ MÜHENDİSLİĞİ 2.SINIF
#PASCAL ÜÇGENİNDE İSTENİLEN SATIRDAKİ ELEMANLARI BULAN AKIŞ DİYAGRAMI

def kacinci_sira(n):                                        #Sıra fonksiyonu
    ilk_eleman = 1                                          #Pascal üçgeninde her sıra 1 ile başlar.
    row = [ilk_eleman]                                      #Listenin ilk elemanını 1 olarak atadık.
    for i in range(1, n + 1):
        suanki_eleman = (ilk_eleman * (n - i + 1)) // i     #Satırdaki her eleman için sıralı olarak bulma formülü.
        ilk_eleman = suanki_eleman                          #Formülün devamı için gerekli işlem.
        row.append(suanki_eleman)                           #Listeye bulduğumuz elemanı ekliyoruz.
    print(row[:10])                                         #Listeyi Yazdırıyoruz
while True:                 #Kullanım rahatlığı için sonsuz sıra sorma döngüsü.
    satir = input("Pascal üçgeninin hangi satırını yazdırmak istiyorsunuz : ")   #Kullanıcıdan input(satır) alınacak.
    if satir == "çıkış":    #Çıkış inputu string olarak girildiğinde program sonlanacaktır.
        break           #Döngünün ardından programı bitirmek için break komutu.
    satir = int(satir)
    kacinci_sira(satir)     #Fonksiyonumuzu çağırdık.
