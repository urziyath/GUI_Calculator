from tkinter import *

root = Tk()
root.configure(background = "light blue")
root.title("Simple Calculator")

e = Entry(root,width = 35,borderwidth = 5)
e.grid(row=0,column=0,columnspan = 3,padx = 5,pady = 5)


def click(number):
    num = e.get()
    e.delete(0,END)
    e.insert(0,str(num) + str(number))

def clear():
    e.delete(0,END)

def add():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0,END)

def equal():
    sec_num = e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(sec_num))

def sub():
    return

def multi():
    return

def div():
    return

#define button

button_1 = Button(root,text = '1',padx = 30,pady = 20,command=lambda: click(1))
button_2 = Button(root,text = '2',padx = 30,pady = 20,command=lambda: click(2))
button_3 = Button(root,text = '3',padx = 30,pady = 20,command=lambda: click(3))
button_4 = Button(root,text = '4',padx = 30,pady = 20,command=lambda: click(4))
button_5 = Button(root,text = '5',padx = 30,pady = 20,command=lambda: click(5))
button_6 = Button(root,text = '6',padx = 30,pady = 20,command=lambda: click(6))
button_7 = Button(root,text = '7',padx = 30,pady = 20,command=lambda: click(7))
button_8 = Button(root,text = '8',padx = 30,pady = 20,command=lambda: click(8))
button_9 = Button(root,text = '9',padx = 30,pady = 20,command=lambda: click(9))
button_0 = Button(root,text = '0',padx = 30,pady = 20,command=lambda: click(0))

button_add = Button(root,text = '+',padx = 29,pady = 20,command = add)
button_clear = Button(root,text='C',padx = 29,pady= 20,command=clear)
button_equal = Button(root,text='=',padx = 30,pady= 84,command=equal)

button_sub = Button(root,text='-',padx = 31 ,pady= 20,command=sub)
button_mult = Button(root,text='*',padx = 30,pady= 20,command=multi)
button_div = Button(root,text='/',padx = 30,pady= 20,command=div)

# put the button on screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column = 0)
button_equal.grid(row=4,column = 2,rowspan = 3)
button_clear.grid(row=4,column = 1)

button_sub.grid(row =5 , column =1 )
button_mult.grid(row =6 , column =1 )
button_div.grid(row =6 , column =0 )


root.mainloop()