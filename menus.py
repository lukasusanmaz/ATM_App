import bankaIslemleri as bI


def menus():
    loop = True
    while loop:
        print("""
        Bakiye Sorgula : 1
        Para Yatır     : 2
        Para Çek       : 3
        Havale Yap     : 4
        Şifre Güncelle : 5
        Çıkış Yap      : 6
        """)

        islem = input("İşlem Seçiniz: ")

        if islem == "1":
            bI.bakiye_sorgula()
            loop = menu_sec()

        elif islem == "2":
            bI.para_yatir()
            loop = menu_sec()

        elif islem == "3":
            bI.para_cek()
            loop = menu_sec()

        elif islem == "4":
            bI.havale()
            loop = menu_sec()

        elif islem == "5":
            bI.sifre_guncelle()
            loop = menu_sec()

        elif islem == "6":
            break
def menu_sec():
    print("""
    Menüye Dön: 1
    Çıkış Yap : 2
    """)

    islem = input("İşlem Seçiniz: ")

    if islem == "1":
        loop = True
        return loop

    if islem == "2":
        loop = False
        return loop