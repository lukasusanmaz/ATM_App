import database as db


def log_in():
    loop = True
    while loop:
        card_no = input("Kart Numarası: ")
        passw = input("Şifre: ")
        for i in db.data:
            if card_no == i[4] and passw == i[5]:
                global customerInfo
                customerInfo = list(i)
                print("Hoşgeldiniz ", customerInfo[1], customerInfo[2])
                loop = False
                break

        while loop:
            print("Eksik veya Hatalı Giriş Yaptınız, Lütfen Tekrar Deneyiniz")
            break

def log_in2():
    loop = True
    while loop:
        card_no = input("Kart Numarası: ")
        passw = input("Şifre: ")
        for i in db.data:
            if card_no != i[4] and passw != i[5]:
                print("Eksik veya Hatalı Giriş Yaptınız, Lütfen Tekrar Deneyiniz")
                break

            else:
                global customerInfo
                customerInfo = list(i)
                print("Hoşgeldiniz ", customerInfo[1], customerInfo[2])
                loop = False
                break
        continue


def bakiye_sorgula():
    print("Bakiyeniz: ", customerInfo[6])


def para_yatir():
    amount = int(input("Tutar Giriniz: "))
    customerInfo[6]+= amount
    db.update_customer("balance", customerInfo[6], customerInfo[0])
    print("Yeni Bakiyeniz: ", customerInfo[6])


def para_cek():
    amount = int(input("Tutar Giriniz: "))
    customerInfo[6] -= amount
    db.update_customer("balance", customerInfo[6], customerInfo[0])
    print("Yeni Bakiyeniz: ", customerInfo[6])


def sifre_guncelle():
    loop = True
    while loop:
        password = input("Şifre Giriniz: ")

        if password == customerInfo[5]:
            loop2 = True
            while loop2:
                newPassword = input("Yeni Şifre Giriniz: ")
                newPasswordAgain = input("Yeni Şifreyi Tekrar Giriniz: ")

                if newPassword == newPasswordAgain:
                    if len(newPassword) != 4:
                        print("Lütfen 4 Rakamdan Oluşan Bir Şifre Giriniz")
                        continue

                    else:
                        pass

                    db.update_customer("password", newPassword, customerInfo[0])
                    print("Şifreniz Başarıyla Güncellendi")
                    loop = False
                    loop2 = False
                    break

                while loop2:
                    print("Eksik veya Hatalı Giriş Yaptınız, Lütfen Tekrar Deneyiniz")
                    break

        while loop:
            print("Eksik veya Hatalı Giriş Yaptınız, Lütfen Tekrar Deneyiniz")
            break


def havale():
    loop = True
    while loop:
        iban = input("IBAN Numarası Giriniz: ")
        amount = int(input("Tutar Giriniz: "))


        target = list(db.select(iban))
        if len(target) == 0:
            print("Eksik veya Yanlış Bir IBAN Numarası Girdiniz, Lütfen Tekrar Deneyiniz")
            continue
        else:
            loop = False
            pass
        while not loop:
            targetList = list(target[0])

            loop2 = True
            while loop2:
                if iban == targetList[7]:
                    print("""
                    Havale {} Hesabına Yatırılacaktır, Devam Etmek İçin 1'e, Yeni IBAN Girmek İçin 2'ye, Önceki Menüye Dönmek İçin 3'e Basınız
                    """.format(targetList[1][0:2] + "*** " + targetList[2][0:2] + "***"))
                    secim = input("Devam Etmek İstiyor Musunuz?: ")

                    if secim == "1":
                        customerInfo[6] -= amount
                        db.update_customer("balance", customerInfo[6], customerInfo[0])
                        targetList[6] += amount
                        db.update_customer("balance", targetList[6], targetList[0])
                        print("Havale Gerçekleşti\n Yeni Bakiyeniz: ", customerInfo[6])
                        loop2 = False
                        break

                    if secim == "2":
                        loop2 = True
                        break

                    if secim == "3":
                        break
            break
        break