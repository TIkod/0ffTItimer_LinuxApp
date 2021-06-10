from tkinter import *
from tkinter import messagebox
import subprocess
import time

def tick():
    time_now.after(200, tick)
    time_now['text'] = time.strftime('%H:%M:%S')

def get_correct_hour():
    if scale_hour.get() < 10:
        return f'0{scale_hour.get()}'
    elif scale_hour.get() == 24:
        return '00'
    return scale_hour.get()

def get_correct_minute():
    if scale_minute.get() < 10:
        return f'0{scale_minute.get()}'
    elif scale_minute.get() == 60:
        return '59'
    return scale_minute.get()

def check_shutdown_time():
    answer = messagebox.askyesnocancel(title='shutdown', message=f'turn off the system in {get_correct_hour()}:{get_correct_minute()}:00 ?',icon=messagebox.WARNING)
    if answer:
        root.withdraw() 
        shutdown_time()

def shutdown_time():
    time_now.after(30000,shutdown_time)
    if str(scale_hour.get()) == time.strftime('%H') and str(scale_minute.get()) == time.strftime('%M'):
        subprocess.call('shutdown -h now',shell=True)

def get_shutdown_time_lab(root):
    lab_shutdown['text'] = f'Shutdown time: {get_correct_hour()}:{get_correct_minute()}:00'

def btn_about():
    messagebox.showinfo("OFF TI TIMER: ABOUT", "How does it work? \n" +
    "Simply ! Select the hours and minutes at which time you want to turn off the system. \n" +
    "When this time comes, the system will turn off \n" +
    "Attention ! After confirming the time, the application will be hidden. When the switch-off time comes, all programs will be closed. And the system shut down")

def btn_author():
    messagebox.showinfo("OFF TI TIMER: AUTHOR", "Name: TIkod(daniel) \n"+
    "GitHub: https://github.com/TIkod \n" +
    "Telegram: https://t.me/TIkods")

root = Tk()
root.title('OFF TI TIMER')
root['bg'] = '#0e131c'
root.geometry('450x320')
root.resizable(width=False,height=False)

menu = Menu(root)
root.config(menu=menu)
menu.add_command(label="ABOUT", command=btn_about)
menu.add_command(label="AUTHOR", command=btn_author)

time_now = Label(root,font='sans 35',bg='#0e131c',fg='white')
time_now.after_idle(tick)

scale_hour = Scale(root,orient=HORIZONTAL,length=400,from_=1,to=24,tickinterval=2,resolution=1,bg='#0e131c', fg='white', command=get_shutdown_time_lab)
scale_minute = Scale(root,orient=HORIZONTAL,length=400,from_=0,to=60,tickinterval=5,resolution=5, bg='#0e131c', fg='white', command=get_shutdown_time_lab)

lab_shutdown = Label(root,text=f'Shutdown time: 01:00:00',font='sans 14', bg='#0e131c',fg='white')
btn_start_timer = Button(root,text='start timer', bg='#47001e', fg='white', font='sans 14', command=check_shutdown_time)

time_now.place(x=120,y=20)
btn_start_timer.place(x=300,y=265)
lab_shutdown.place(x=20,y=270)
scale_hour.place(x=22,y=100)
scale_minute.place(x=22,y=180)

root.mainloop()