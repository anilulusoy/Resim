from tkinter import filedialog
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from PIL import Image

from PIL import ImageFilter

import glob,os

import string
import random

x= Image.ANTIALIAS
dir_path = os.path.dirname(os.path.realpath(__file__))


liste=[]
gecmis_adres=" "


foldername = (dir_path.split('\duzelt'))[0]

liste=os.listdir()
a=os.getcwd()



def resim_istedigimi_ayarla_alttan():
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    pencere.filename = filedialog.askopenfilename(initialdir="/", title="Dosya Sec", filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
    global c
    (c,d)=os.path.split(pencere.filename)
    print(pencere.filename)
    print(c)
    print(d)

    global foldername2
    os.chdir(c)
    foldername2="kayit alani"





    liste_resim = os.listdir(c)

    for i in liste_resim:
        if os.path.isdir(m):
            continue
        (m,n)=os.path.splitext(i)
        if i.endswith(n):
            dosya_adi = (c+'/'+i)
            img = Image.open(dosya_adi)
 
            global data_width
            global  data_height
            data = img.size
            data_width=data[0]
            data_height=data[1]

            resim_istenilen_width_deger = int(Int_Input_width.get())
            resim_istenilen_height_deger = int(Int_Input_height.get())
            resim_ilk_width_deger = data_width
            resim_ilk_height_deger = data_height
            a = resim_ilk_width_deger/resim_istenilen_width_deger
            b = resim_ilk_height_deger/resim_istenilen_height_deger
            print(a)
            print(b)
            if b > a:
                resim_final_width_deger = resim_istenilen_width_deger
                percent = float(Int_Input_width.get()) / float(resim_ilk_width_deger)
                resim_final_height_deger = float(percent) * float(resim_ilk_height_deger)
            else:
                resim_final_height_deger = resim_istenilen_height_deger
                percent = float(Int_Input_height.get()) / float(resim_ilk_height_deger)
                resim_final_width_deger = float(percent) * float(resim_ilk_width_deger)
                print(percent)
                print(resim_final_width_deger)
                print(resim_final_height_deger)
            global newImage
            newImage = img.resize((int(resim_final_width_deger), int(resim_final_height_deger)), x)
            newImage.save("newImage"+n)
            newImage.show()

            global left
            global right
            global top
            global bottom

            left = (resim_istenilen_width_deger-resim_final_width_deger)/2
            right = (resim_istenilen_width_deger + resim_final_width_deger) / 2
            top = (resim_istenilen_height_deger - resim_final_height_deger)/2
            bottom = (resim_istenilen_height_deger + resim_final_height_deger) / 2





            left_deger.set(left)
            right_deger.set(right)
            top_deger.set(top)
            bottom_deger.set(bottom)
            ilk_width_deger.set(resim_ilk_width_deger)
            ilk_height_deger.set(resim_ilk_height_deger)
            son_height_deger.set(resim_final_height_deger)
            son_width_deger.set(resim_final_width_deger)
            son_adres_deger.set(c)

            cropped_img_first = newImage.crop((int(abs(resim_final_width_deger-resim_istenilen_width_deger)), int(abs(resim_final_height_deger-resim_istenilen_height_deger)), int(abs(resim_final_width_deger)), int(abs(resim_final_height_deger))))
            data_first = cropped_img_first.size
            son_istenilen_height_deger.set(data_first[1])
            son_istenilen_width_deger.set(data_first[0])

            yeni_resim_first = cropped_img_first.resize( (int(data_first[0]) , int(data_first[1])),x)
            yeni_resim_adi = (id_generator()+n)
            if not os.path.exists(foldername2):
                os.mkdir(foldername2)
                yeni_resim_first.save(foldername2+'/'+yeni_resim_adi)
                yeni_resim_first.show()
            else:
                yeni_resim_first.save(foldername2 + '/' + yeni_resim_adi)
                yeni_resim_first.show()



def resim_istedigimi_ayarla_ustten():
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    pencere.filename = filedialog.askopenfilename(initialdir="/", title="Dosya Se?", filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
    global c
    (c,d)=os.path.split(pencere.filename)
    print(pencere.filename)
    print(c)
    print(d)


    global foldername2
    os.chdir(c)
    foldername2="kayit alani"






    liste_resim = os.listdir(c)

    for i in liste_resim:
        (m,n)=os.path.splitext(i)
        if os.path.isdir(m):
            continue
        if i.endswith(n):
            dosya_adi = (c+'/'+i)
            img = Image.open(dosya_adi)

            global data_width
            global  data_height
            data = img.size
            data_width=data[0]
            data_height=data[1]
 
            resim_istenilen_width_deger = int(Int_Input_width.get())
            resim_istenilen_height_deger = int(Int_Input_height.get())
            resim_ilk_width_deger = data_width
            resim_ilk_height_deger = data_height
            a = resim_ilk_width_deger/resim_istenilen_width_deger
            b = resim_ilk_height_deger/resim_istenilen_height_deger
            print(a)
            print(b)
            if b > a:
                resim_final_width_deger = resim_istenilen_width_deger
                percent = float(Int_Input_width.get()) / float(resim_ilk_width_deger)
                resim_final_height_deger = float(percent) * float(resim_ilk_height_deger)
            else:
                resim_final_height_deger = resim_istenilen_height_deger
                percent = float(Int_Input_height.get()) / float(resim_ilk_height_deger)
                resim_final_width_deger = float(percent) * float(resim_ilk_width_deger)
                print(percent)
                print(resim_final_width_deger)
                print(resim_final_height_deger)
            global newImage
            newImage = img.resize((int(resim_final_width_deger), int(resim_final_height_deger)), x)
            newImage.save("newImage"+n)
            newImage.show()

            global left
            global right
            global top
            global bottom

            left = (resim_istenilen_width_deger-resim_final_width_deger)/2
            right = (resim_istenilen_width_deger + resim_final_width_deger) / 2
            top = (resim_istenilen_height_deger - resim_final_height_deger)/2
            bottom = (resim_istenilen_height_deger + resim_final_height_deger) / 2





            left_deger.set(left)
            right_deger.set(right)
            top_deger.set(top)
            bottom_deger.set(bottom)
            ilk_width_deger.set(resim_ilk_width_deger)
            ilk_height_deger.set(resim_ilk_height_deger)
            son_height_deger.set(resim_final_height_deger)
            son_width_deger.set(resim_final_width_deger)
            son_adres_deger.set(c)

            cropped_img_first = newImage.crop((int(abs(0)), int(abs(0)), int(abs(resim_istenilen_width_deger)), int(abs(resim_istenilen_height_deger))))
            data_first = cropped_img_first.size
            son_istenilen_height_deger.set(data_first[1])
            son_istenilen_width_deger.set(data_first[0])

            yeni_resim_first = cropped_img_first.resize( (int(data_first[0]) , int(data_first[1])),x)
            yeni_resim_adi = (id_generator()+n)
            if not os.path.exists(foldername2):
                os.mkdir(foldername2)
                yeni_resim_first.save(foldername2+'/'+yeni_resim_adi)
                yeni_resim_first.show()
            else:
                yeni_resim_first.save(foldername2 + '/' + yeni_resim_adi)
                yeni_resim_first.show()

def resim_sec():
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    global c
    global gecmis_adres
    pencere.filename = filedialog.askopenfilename(initialdir="/", title="Dosya Se?", filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
    (c,d)=os.path.split(pencere.filename)
    (m,n)=os.path.splitext(d)
    print(m)
    print(n)

    gecmis_adres=c
    (k,l)=os.path.splitext(d)


    global liste_resim
    liste_resim=os.listdir(c)

    img = Image.open(pencere.filename)
    global data_width
    global  data_height
    data = img.size
    data_width=data[0]
    data_height=data[1]

    resim_istenilen_width_deger = int(Int_Input_width.get())
    resim_istenilen_height_deger = int(Int_Input_height.get())
    resim_ilk_width_deger = data_width
    resim_ilk_height_deger = data_height
    a = resim_ilk_width_deger/resim_istenilen_width_deger
    b = resim_ilk_height_deger/resim_istenilen_height_deger

    if b>a:
        resim_final_width_deger = resim_istenilen_width_deger
        percent = float(Int_Input_width.get())/float(resim_ilk_width_deger)
        resim_final_height_deger = float(percent) * float(resim_ilk_height_deger)
    else:
        resim_final_height_deger = resim_istenilen_height_deger
        percent = float(Int_Input_height.get()) / float(resim_ilk_height_deger)
        resim_final_width_deger = float(percent) * float(resim_ilk_width_deger)
    global newImage
    newImage = img.resize((int(resim_final_width_deger), int(resim_final_height_deger)), Image.NEAREST)
    newImage.save("newImage"+n)
    newImage.show()

    global left
    global right
    global top
    global bottom

    left = (resim_istenilen_width_deger-resim_final_width_deger)/2
    right = (resim_istenilen_width_deger + resim_final_width_deger) / 2
    top = (resim_istenilen_height_deger - resim_final_height_deger)/2
    bottom = (resim_istenilen_height_deger + resim_final_height_deger) / 2

    cropped_img = newImage.crop((int(left), int(top), int(right),int(bottom)))
    data2 = cropped_img.size

    imageWidth2 = data2[0]
    imageHeight2 = data2[1]



    newImage2 = cropped_img.resize((int(imageWidth2), int(imageHeight2)), Image.NEAREST)
    new_resim_name = (id_generator() +n)

    newImage2.save(new_resim_name)
    newImage2.show()

    left_deger.set(left)
    right_deger.set(right)
    top_deger.set(top)
    bottom_deger.set(bottom)
    ilk_width_deger.set(resim_ilk_width_deger)
    ilk_height_deger.set(resim_ilk_height_deger)
    son_height_deger.set(resim_final_height_deger)
    son_width_deger.set(resim_final_width_deger)
    son_istenilen_height_deger.set(resim_istenilen_height_deger)
    son_istenilen_width_deger.set(resim_istenilen_width_deger)



def resim_istedigimi_ayarla():
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    pencere.filename = filedialog.askopenfilename(initialdir="/", title="Dosya Se?", filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
    global c
    (c,d)=os.path.split(pencere.filename)
    print(pencere.filename)
    print(c)
    print(d)


    global foldername2
    os.chdir(c)
    foldername2="kayit alani"





    liste_resim = os.listdir(c)

    for i in liste_resim:
        print(i)
        (m,n)=os.path.splitext(i)
        print(m)
        print(n)
        if os.path.isdir(m):
            continue
        if i.endswith(n):
            dosya_adi = (c+'/'+i)
            img = Image.open(dosya_adi)

            global data_width
            global  data_height
            data = img.size
            data_width=data[0]
            data_height=data[1]
            
            resim_istenilen_width_deger = int(Int_Input_width.get())
            resim_istenilen_height_deger = int(Int_Input_height.get())
            resim_ilk_width_deger = data_width
            resim_ilk_height_deger = data_height
            a = resim_ilk_width_deger/int(resim_istenilen_width_deger)
            b = resim_ilk_height_deger/int(resim_istenilen_height_deger)
            print(a)
            print(b)
            if b > a:
                resim_final_width_deger = int(resim_istenilen_width_deger)
                percent = float(Int_Input_width.get()) / float(resim_ilk_width_deger)
                resim_final_height_deger = float(percent) * float(resim_ilk_height_deger)
            else:
                resim_final_height_deger = resim_istenilen_height_deger
                percent = float(Int_Input_height.get()) / float(resim_ilk_height_deger)
                resim_final_width_deger = float(percent) * float(resim_ilk_width_deger)
                print(percent)
                print(resim_final_width_deger)
                print(resim_final_height_deger)
            global newImage
            newImage = img.resize((int(resim_final_width_deger), int(resim_final_height_deger)), x)
            newImage.save("newImage"+n)
            newImage.show()

            global left
            global right
            global top
            global bottom

            left = (int(resim_istenilen_width_deger)-int(resim_final_width_deger))/2
            right = (int(resim_istenilen_width_deger) + int(resim_final_width_deger)) / 2
            top = (int(resim_istenilen_height_deger) - int(resim_final_height_deger))/2
            bottom = (int(resim_istenilen_height_deger) + int(resim_final_height_deger)) / 2





            left_deger.set(left)
            right_deger.set(right)
            top_deger.set(top)
            bottom_deger.set(bottom)
            ilk_width_deger.set(resim_ilk_width_deger)
            ilk_height_deger.set(resim_ilk_height_deger)
            son_height_deger.set(resim_final_height_deger)
            son_width_deger.set(resim_final_width_deger)
            son_adres_deger.set(c)

            cropped_img_first = newImage.crop((int(abs(left)), int(abs(top)), int(abs(right)), int(abs(bottom))))
            data_first = cropped_img_first.size
            son_istenilen_height_deger.set(data_first[1])
            son_istenilen_width_deger.set(data_first[0])

            yeni_resim_first = cropped_img_first.resize( (int(data_first[0]) , int(data_first[1])),x)
            yeni_resim_adi = (id_generator()+n)
            if not os.path.exists(foldername2):
                os.mkdir(foldername2)
                yeni_resim_first.save(foldername2+'/'+yeni_resim_adi)
                yeni_resim_first.show()
            else:
                yeni_resim_first.save(foldername2 + '/' + yeni_resim_adi)
                yeni_resim_first.show()


def resim_istedigimi_ayarla_elle():
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    adres_elle=son_adres_deger.get()

    pencere.filename = filedialog.askopenfilename(initialdir="adres/", title="Dosya Sec",filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
    global c
    (c,d)=os.path.split(pencere.filename)
    global foldername3
    (m,n)=os.path.splitext(d)
    os.chdir(c)
    foldername3="kayit alani"
    img = Image.open(pencere.filename)
    global data_width
    global data_height
    data = img.size
    data_width = data[0]
    data_height = data[1]

    resim_istenilen_width_deger = int(Int_Input_width.get())
    resim_istenilen_height_deger = int(Int_Input_height.get())
    resim_ilk_width_deger = data_width
    resim_ilk_height_deger = data_height
    a = resim_ilk_width_deger / resim_istenilen_width_deger
    b = resim_ilk_height_deger / resim_istenilen_height_deger
    if b > a:
        resim_final_width_deger = resim_istenilen_width_deger
        percent = float(Int_Input_width.get()) / float(resim_ilk_width_deger)
        resim_final_height_deger = float(percent) * float(resim_ilk_height_deger)
    else:
        resim_final_height_deger = resim_istenilen_height_deger
        percent = float(Int_Input_height.get()) / float(resim_ilk_height_deger)
        resim_final_width_deger = float(percent) * float(resim_ilk_width_deger)
    global newImage
    newImage = img.resize((int(resim_final_width_deger), int(resim_final_height_deger)), Image.NEAREST)
    newImage.save("newImage"+n)
    newImage.show()


    left = int(son_istenilen_left_deger.get())
    right = int(son_istenilen_right_deger.get())
    top= int(son_istenilen_top_deger.get())
    bottom = int(son_istenilen_bottom_deger.get())

    if (int(bottom) < int(top)):
        messagebox.showinfo("hata","top bottom de?erlerinize dikkat edin")
        top = int(son_istenilen_top_deger.get())
        bottom = int(son_istenilen_bottom_deger.get())

    if (int(right) < int(left)):
        messagebox.showinfo("hata","left right de?erlerini kontrol et")
        left = int(son_istenilen_left_deger.get())
        right = int(son_istenilen_right_deger.get())




    cropped_img_first = newImage.crop((int(abs(left)), int(abs(top)), int(abs(right)), int(abs(bottom))))
    data_first = cropped_img_first.size
    son_istenilen_height_deger.set(data_first[1])
    son_istenilen_width_deger.set(data_first[0])

    yeni_resim_first = cropped_img_first.resize( (int(data_first[0]) , int(data_first[1])) , x)
    yeni_resim_adi = (id_generator()+n)


    if not os.path.exists(foldername3):
        os.mkdir(foldername3)
        yeni_resim_first.save(foldername3 + '/' + yeni_resim_adi)
        yeni_resim_first.show()
    else:
        yeni_resim_first.save(foldername3 + '/' + yeni_resim_adi)
        yeni_resim_first.show()

def son_pencereden_resmi_ayarla():
        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        adres=son_adres_deger.get()

        pencere.filename = filedialog.askopenfilename(initialdir="adres/", title="Dosya Se?",filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))

        global c
        (c, d) = os.path.split(pencere.filename)



        global foldername2
        os.chdir(c)
        foldername2 = "kayit alani"
        global liste_gecmis

        liste_resim = os.listdir(c)

        for i in liste_resim:
            (m,n)=os.path.splitext(i)
            if os.path.isdir(m):
                continue            

            if i.endswith(n):
                dosya_adi = (c + '/' + i)
                img = Image.open(dosya_adi)
                print(img.mode)
                global data_width
                global data_height
                data = img.size
                data_width = data[0]
                data_height = data[1]
                print("1" + dosya_adi)  
                resim_istenilen_width_deger = int(Int_Input_width.get())
                resim_istenilen_height_deger = int(Int_Input_height.get())
                resim_ilk_width_deger = data_width
                resim_ilk_height_deger = data_height
                a = resim_ilk_width_deger / resim_istenilen_width_deger
                b = resim_ilk_height_deger / resim_istenilen_height_deger
                if b > a:
                    resim_final_width_deger = resim_istenilen_width_deger
                    percent = float(Int_Input_width.get()) / float(resim_ilk_width_deger)
                    resim_final_height_deger = float(percent) * float(resim_ilk_height_deger)
                else:
                    resim_final_height_deger = resim_istenilen_height_deger
                    percent = float(Int_Input_height.get()) / float(resim_ilk_height_deger)
                    resim_final_width_deger = float(percent) * float(resim_ilk_width_deger)
                global newImage
                newImage = img.resize((int(resim_final_width_deger), int(resim_final_height_deger)), x)
                newImage.save("newImage"+n)
                newImage.show()

                global left
                global right
                global top
                global bottom

                left = (resim_istenilen_width_deger - resim_final_width_deger) / 2
                right = (resim_istenilen_width_deger + resim_final_width_deger) / 2
                top = (resim_istenilen_height_deger - resim_final_height_deger) / 2
                bottom = (resim_istenilen_height_deger + resim_final_height_deger) / 2

                left_deger.set(left)
                right_deger.set(right)
                top_deger.set(top)
                bottom_deger.set(bottom)
                ilk_width_deger.set(resim_ilk_width_deger)
                ilk_height_deger.set(resim_ilk_height_deger)
                son_height_deger.set(resim_final_height_deger)
                son_width_deger.set(resim_final_width_deger)

                cropped_img_first = newImage.crop((int(abs(left)), int(abs(top)), int(abs(right)), int(abs(bottom))))
                data_first = cropped_img_first.size
                son_istenilen_height_deger.set(data_first[1])
                son_istenilen_width_deger.set(data_first[0])

                yeni_resim_first = cropped_img_first.resize((int(data_first[0]), int(data_first[1])), x)
                yeni_resim_adi = (id_generator() + n)
                if not os.path.exists(foldername2):
                    os.mkdir(foldername2)
                    yeni_resim_first.save(foldername2 + '/' + yeni_resim_adi)
                    yeni_resim_first.show()
                else:
                    yeni_resim_first.save(foldername2 + '/' + yeni_resim_adi)
                    yeni_resim_first.show()



pencere = Tk()
pencere.geometry("1600x1600+0+0")
pencere.title("Foto Kesimi")

Int_Input_width = StringVar()
Int_Input_height = StringVar()
ilk_width_deger = StringVar()
ilk_height_deger = StringVar()
son_width_deger = StringVar()
son_height_deger = StringVar()
left_deger = StringVar()
right_deger= StringVar()
top_deger = StringVar()
bottom_deger = StringVar()
son_istenilen_width_deger = StringVar()
son_istenilen_height_deger = StringVar()
son_istenilen_left_deger = StringVar()
son_istenilen_right_deger = StringVar()
son_istenilen_top_deger = StringVar()
son_istenilen_bottom_deger = StringVar()
son_adres_deger = StringVar()

tops = Frame(pencere,width=1600,height=10,bg="powder blue",relief=SUNKEN)
tops.pack(side=TOP)

Bilgi_alma_pencere = Frame(pencere,width=800,height=500,bg="white",relief=SUNKEN)
Bilgi_alma_pencere.pack(side=LEFT)


Foto_ayarlama_Elle = Frame(pencere,width=800,height=500,bg="white",relief=SUNKEN)
Foto_ayarlama_Elle.pack(side=RIGHT)

#Foto_ayarlama_Auto = Frame(pencere,width=600,height=700,bg="red",relief=SUNKEN)
#Foto_ayarlama_Auto.pack(side=BOTTOM)

topsbaslik = Label(tops,font=('arial',50,'bold'),text="ANİL",fg="green",bd=10,anchor='w')
topsbaslik.grid(row=0,column=0)


############################################# bilgi alma  #############################3
istenilen_width = Label(Bilgi_alma_pencere,font=('arial',20,'bold'),text="istenilen width de?eri:",fg="black",bd=16,anchor='w')
istenilen_width.grid(row=0,column=0)
istenilen_width_deger = Entry(Bilgi_alma_pencere,font=('arial',20,'bold'),textvariable=Int_Input_width,bd=10,insertwidth=8,bg="white",justify='left')
istenilen_width_deger.grid(row=0,column=1)


istenilen_height = Label(Bilgi_alma_pencere,font=('arial',20,'bold'),text="istenilen height de?eri:",fg="black",bd=16,anchor='w')
istenilen_height.grid(row=1,column=0)
istenilen_height_deger = Entry(Bilgi_alma_pencere,font=('arial',20,'bold'),textvariable=Int_Input_height,bd=10,insertwidth=8,bg="white",justify='left')
istenilen_height_deger.grid(row=1,column=1)


buton_resim_secme=Button(Bilgi_alma_pencere,padx=16,pady=8,fg="black",font=('arial',20,'bold'),text="resim se? elle",bg="red",command=lambda :resim_sec()).grid(row=2,column=0)
########################################################2.sayfa######################33
resim_ilk_width = Label(Foto_ayarlama_Elle,font=('arial',20,'bold'),text="ilk width de?eri:",fg="black",bd=16,anchor='w')
resim_ilk_width.grid(row=0,column=0)

resim_ilk_width_deger = Entry(Foto_ayarlama_Elle,font=('arial',20,'bold'),textvariable=ilk_width_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_ilk_width_deger.grid(row=0,column=1)
#####################3
resim_ilk_height = Label(Foto_ayarlama_Elle,font=('arial',20,'bold'),text="ilk height de?eri:",fg="black",bd=16,anchor='w')
resim_ilk_height.grid(row=1,column=0)

resim_ilk_height_deger = Entry(Foto_ayarlama_Elle,font=('arial',20,'bold'),textvariable=ilk_height_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_ilk_height_deger.grid(row=1,column=1)
#########################3
resim_son_width = Label(Foto_ayarlama_Elle,font=('arial',20,'bold'),text="son width de?eri:",fg="black",bd=16,anchor='w')
resim_son_width.grid(row=2,column=0)

resim_son_width_deger = Entry(Foto_ayarlama_Elle,font=('arial',20,'bold'),textvariable=son_width_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_son_width_deger.grid(row=2,column=1)
#########################
resim_son_height = Label(Foto_ayarlama_Elle,font=('arial',20,'bold'),text="son height de?eri:",fg="black",bd=16,anchor='w')
resim_son_height.grid(row=3,column=0)

resim_son_height_deger = Entry(Foto_ayarlama_Elle,font=('arial',20,'bold'),textvariable=son_height_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_son_height_deger.grid(row=3,column=1)
####################3
resim_left = Label(Foto_ayarlama_Elle,font=('arial',20,'bold'),text="left de?eri :",fg="black",bd=16,anchor='w')
resim_left.grid(row=4,column=0)

resim_left_deger =  Entry(Foto_ayarlama_Elle,font=('arial',20,'bold'),textvariable=left_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_left_deger.grid(row=4,column=1)
############################33
resim_right = Label(Foto_ayarlama_Elle,font=('arial',20,'bold'),text="right de?eri:",fg="black",bd=16,anchor='w')
resim_right.grid(row=5,column=0)

resim_right_deger =  Entry(Foto_ayarlama_Elle,font=('arial',20,'bold'),textvariable=right_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_right_deger.grid(row=5,column=1)
#########################################
resim_top = Label(Foto_ayarlama_Elle,font=('arial',20,'bold'),text="top de?eri:",fg="black",bd=16,anchor='w')
resim_top.grid(row=6,column=0)

resim_top_deger =  Entry(Foto_ayarlama_Elle,font=('arial',20,'bold'),textvariable=top_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_top_deger.grid(row=6,column=1)
###################################
resim_bottom = Label(Foto_ayarlama_Elle,font=('arial',20,'bold'),text="bottom de?eri:",fg="black",bd=16,anchor='w')
resim_bottom.grid(row=7,column=0)

resim_bottom_deger =  Entry(Foto_ayarlama_Elle,font=('arial',20,'bold'),textvariable=bottom_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_bottom_deger.grid(row=7,column=1)
################################
resim_son_istenilen_width = Label(Bilgi_alma_pencere,font=('arial',20,'bold'),text="istenilen son width de?eri:",fg="black",bd=16,anchor='w')
resim_son_istenilen_width.grid(row=5,column=0)

resim_son_istenilen_width_deger = Entry(Bilgi_alma_pencere,font=('arial',20,'bold'),textvariable=son_istenilen_width_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_son_istenilen_width_deger.grid(row=5,column=1)
###############################
resim_son_istenilen_height = Label(Bilgi_alma_pencere,font=('arial',20,'bold'),text="istenilen son height de?eri:",fg="black",bd=16,anchor='w')
resim_son_istenilen_height.grid(row=6,column=0)

resim_son_istenilen_height_deger = Entry(Bilgi_alma_pencere,font=('arial',20,'bold'),textvariable=son_istenilen_height_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_son_istenilen_height_deger.grid(row=6,column=1)

###############################
resim_son_istenilen_left = Label(Bilgi_alma_pencere,font=('arial',20,'bold'),text="istenilen son left de?eri:",fg="black",bd=16,anchor='w')
resim_son_istenilen_left.grid(row=7,column=0)

resim_son_istenilen_left_deger = Entry(Bilgi_alma_pencere,font=('arial',20,'bold'),textvariable=son_istenilen_left_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_son_istenilen_left_deger.grid(row=7,column=1)

###############################
resim_son_istenilen_right = Label(Bilgi_alma_pencere,font=('arial',20,'bold'),text="istenilen son right de?eri:",fg="black",bd=16,anchor='w')
resim_son_istenilen_right.grid(row=8,column=0)

resim_son_istenilen_right_deger = Entry(Bilgi_alma_pencere,font=('arial',20,'bold'),textvariable=son_istenilen_right_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_son_istenilen_right_deger.grid(row=8,column=1)
###############################
resim_son_istenilen_top = Label(Bilgi_alma_pencere,font=('arial',20,'bold'),text="istenilen son top de?eri:",fg="black",bd=16,anchor='w')
resim_son_istenilen_top.grid(row=9,column=0)

resim_son_istenilen_top_deger = Entry(Bilgi_alma_pencere,font=('arial',20,'bold'),textvariable=son_istenilen_top_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_son_istenilen_top_deger.grid(row=9,column=1)
###############################
resim_son_istenilen_bottom = Label(Bilgi_alma_pencere,font=('arial',20,'bold'),text="istenilen son bottom de?eri:",fg="black",bd=16,anchor='w')
resim_son_istenilen_bottom.grid(row=10,column=0)

resim_son_istenilen_bottom_deger = Entry(Bilgi_alma_pencere,font=('arial',20,'bold'),textvariable=son_istenilen_bottom_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_son_istenilen_bottom_deger.grid(row=10,column=1)

########################sayfa1 hesapla ??k?? reset butonlar?#######################
buton_resim_ayarlama = Button(Bilgi_alma_pencere,padx=16,pady=8,fg="black",font=('arial',20,'bold'),text="resim ayarla otomatik",bg="red",command=lambda :resim_istedigimi_ayarla()).grid(row=3,column=0)
buton_resim_ayarlama_elle = Button(Bilgi_alma_pencere,padx=16,pady=8,fg="black",font=('arial',20,'bold'),text="resim ayarla elle",bg="red",command=lambda :resim_istedigimi_ayarla_elle()).grid(row=4,column=0)
buton_resim_ayarlama_ustten = Button(Bilgi_alma_pencere,padx=16,pady=8,fg="black",font=('arial',20,'bold'),text="rao?st",bg="red",command=lambda :resim_istedigimi_ayarla_ustten()).grid(row=2,column=1)
buton_resim_ayarlama_alttan = Button(Bilgi_alma_pencere,padx=16,pady=8,fg="black",font=('arial',20,'bold'),text="raoAlt",bg="red",command=lambda :resim_istedigimi_ayarla_alttan()).grid(row=2,column=2)

##############################3
resim_son_adres_deger = Entry(Bilgi_alma_pencere,font=('arial',20,'bold'),textvariable=son_adres_deger,bd=10,insertwidth=8,bg="white",justify='left')
resim_son_adres_deger.grid(row=3,column=1)

liste_gecmis_button = Button(Bilgi_alma_pencere,padx=16,pady=8,fg="black",font=('arial',20,'bold'),text="se?",bg="red",command=lambda:son_pencereden_resmi_ayarla()).grid(row=4,column=1)

pencere.mainloop()
