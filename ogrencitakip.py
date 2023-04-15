import pandas as pd
import matplotlib.pyplot as plt
import time
student_list = {"İsim":["Murat","Ebru","Ayşe","Yiğit","Berkay","Elif","Emir"],

                  "Soyisim":["Yıldız","Kaya","Destan","Çelik","Horozoğlu","Aydın","Özkan"],

                  "Sınıf":[1,2,"H",3,2,"H",4],

                   "Cinsiyet":["Erkek","Kadın","Kadın","Erkek","Erkek","Kadın","Erkek"]}

dataframe = pd.DataFrame(student_list)


class Student():

    def __init__(self,name,surname,classes,gender):

        self.name = name

        self.surname = surname

        self.classes= classes

        self.gender = gender

    def addStudent():

            x = 0

            while True:

                try:

                    x += 1

                    print("Lütfen Öğrenci Bilgilerini Giriniz!!")

                    name = input("İsim: ").lower().capitalize()

                    surname = input("Soyisim: ").lower().capitalize()

                    classes = input("Sınıf: ").capitalize()

                    gender = input("Cinsiyet: ").capitalize()

                    student_list["İsim"].append(name)

                    student_list["Soyisim"].append(surname)

                    student_list["Sınıf"].append(classes)

                    student_list["Cinsiyet"].append(gender)

                    dataframe = pd.DataFrame(student_list)

                    dataframe.head()

                    if x == 3:
                        a = int(input(" Toplam 3 İsim Girdiniz  Listeyi Görmek İçin Herhangi Bir Şey Tuşlayınız: "))

                        if a == 99998887776665551:

                            pass

                        else:

                            print(dataframe)

                            time.sleep(3)

                            print("Öğrenciler İle İlgili Grafiklere Yönlendiriliyorsunuz....")

                            time.sleep(1)

                            print("Öğrenciler İle İlgili Grafiklere Yönlendiriliyorsunuz...")

                            time.sleep(1)

                            print("Öğrenciler İle İlgili Grafiklere Yönlendiriliyorsunuz..")

                            time.sleep(1)

                            print("Öğrenciler İle İlgili Grafiklere Yönlendiriliyorsunuz.")

                            time.sleep(1)

                            print("Öğrenciler İle İlgili Grafiklere Yönlendiriliyorsunuz.")

                            time.sleep(1)

                            womens = list()
                            mens = list()

                            x = 0
                            while True:

                                x += 1
                                a = (student_list["Cinsiyet"][x])

                                if a == "Kadın":
                                    womens.append(a)

                                else:
                                    mens.append(a)

                                    j = len(student_list["Cinsiyet"])

                                    if x == (j-1):
                                        pricewomen = len(womens)
                                        pricemen = len(mens)
                                        plt.bar("Erkekler",pricemen)
                                        plt.bar("Kadınlar",pricewomen)
                                        plt.show()
                                        print(" ")
                                        print(" ")
                                        print(" ")
                                        print("Çıkış Yapılıyor")
                                        print("\a")
                                        time.sleep(10)
                                        quit()

                except ValueError or TypeError():
                    print("Yanlış Giriş Yaptn")
                    continue
Student.addStudent()
