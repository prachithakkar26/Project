import qrcode
from tkinter import *
from tkinter import messagebox

def handle():

    qrcode1=qrcode.QRCode(version=en4.get(),box_size=10,border=10)
    qrcode1.add_data(en1.get())
    qrcode1.best_fit()

    image=qrcode1.make_image()

    fileplace=en2.get()+'//'+en3.get()
    image.save(f'{fileplace}.png')


    messagebox.showinfo("Success!", "\n OR Code generated successfully!")

window=Tk()

window.title('QR CODE GENERATOR')
window.geometry('900x900')
window.configure(background='#7daec2')

fr=Frame(window,height=700,width=700,background='white')
fr.place(x=100,y=70)

head=Label(window,text='QR Code Generator',font=('broadway',32,'italic','bold'),fg='dark blue',background='#7daec2')
head.place(x=300,y=23)

text=Label(fr,text='Enter the text/URL:',font=('times new roman',22),bg='white',fg='dark blue')
text.place(x=50,y=60)

en1=Entry(fr,font=('times new roman',20),bg='#7daec2')
en1.place(x=60,y=110,relwidth=0.8)

location=Label(fr,text='Enter the location to save the QR code:',font=('times new roman',22),bg='white',fg='dark blue')
location.place(x=50,y=170)

en2=Entry(fr,font=('times new roman',20),bg='#7daec2')
en2.place(x=60,y=220,relwidth=0.8)

qrname=Label(fr,text='Enter the QR code name:',font=('times new roman',22),bg='white',fg='dark blue')
qrname.place(x=50,y=280)

en3=Entry(fr,font=('times new roman',20),bg='#7daec2')
en3.place(x=60,y=330,relwidth=0.8)

qrsize=Label(fr,text='Enter the QR code size from 1 to 40 [1 = 21x21]:',font=('times new roman',22),bg='white',fg='dark blue')
qrsize.place(x=50,y=390)

en4=Entry(fr,font=('times new roman',20),bg='#7daec2')
en4.place(x=60,y=440,relwidth=0.8)

btn=Button(fr,text='Get Code',font=('times new roman',20),activebackground='#7daec2',fg='dark blue',width=30,command=handle)
btn.place(x=170,y=550)

window.mainloop()