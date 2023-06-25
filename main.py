#bmi (body mass index) = m/h**2
from tkinter import *

def calculate():
    bmi=int(mass_entry.get())/(int(height_entry.get())/100)**2
    color=''
    if bmi<18.5: color='Purple'
    elif bmi>25: color='FireBrick'
    else: color='Green'
    result_label.configure(text=round(bmi,1),fg=color)

root=Tk()

height_label=Label(root,text='Height: ',font=(12)); height_label.grid(column=0,row=0)
height_entry=Entry(root); height_entry.grid(column=1,row=0); height_entry.focus()

mass_label=Label(root,text='Body mass: ',font=(12)); mass_label.grid(column=0,row=1)
mass_entry=Entry(root); mass_entry.grid(column=1,row=1)

result_button=Button(root,text='calculate',bg='MidnightBlue',fg='LightSkyBlue',command=calculate); result_button.grid(column=0,row=2)
result_label=Label(root,text='',font=(12),); result_label.grid(column=1,row=2)

root.mainloop()