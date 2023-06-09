from tkinter import *
from speedtest import Speedtest

def check_speed():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download/(10**6),2)
    upload_speed = round(upload/(10**6),2)
    down_label.config(text="Download Speed - "+ str(download_speed)+" Mbps")
    up_label.config(text="Upload Speed - "+ str(upload_speed)+" Mbps")

#check_speed()

root = Tk()
root.title("Speed Of Your Internet")
root.wm_iconbitmap('E:\PythonProjects\InternetSpeedTestApp\Speed Of Your Internet\speederlogo.ico')
root.geometry('300x400')
root.config(bg='black')
root.resizable(False,False)

canvas = Canvas(root, width = 400, height = 400,bg="white")      
canvas.pack()      
img = PhotoImage(file='E:\PythonProjects\InternetSpeedTestApp\Speed Of Your Internet\speeder.png')
canvas.create_image(0,0,anchor=NW, image=img)

Button = Button(root,text="Start Test",width=10,bg="green", borderwidth=10,activebackground="red",command=check_speed)
Button.place(x=110,y=345)

down_label = Label(root,text="",width=25)
down_label.place(x=60,y=275)
up_label = Label(root,text="",width=25)
up_label.place(x=60,y=307)

root.mainloop()