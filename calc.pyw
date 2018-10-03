import tkinter as tk

from tkinter import ttk    # to be able to use the label widget

#-----------------------------------------------------------------------------------

win=tk.Tk()  # create the instance  of the main window

win.title("simple calc") # add title

win.geometry("600x300") # here i a set the window size
win.resizable(False,False)


#the result and input test box
tbv= tk.StringVar()
tb = ttk.Entry(win, width=47, textvariable=tbv ,state='readonly')
tb.grid(column=0, row=0,pady=16,padx=200,sticky='W')
#-----------------------------------------------------
value=""  # to store the entred values



#button1 "7"
def but1():
    global value
    value=value+"7"
    tbv.set(value)


bt1=ttk.Button(win,text="7",command=but1, width=5)
bt1.grid(column=0, row=1, padx=198,sticky='W')
#------------------------------------------------------------------------


#button2 "8"
def but2():
    global value
    value=value+"8"
    tbv.set(value)


bt2=ttk.Button(win,text="8",command=but2, width=5)
bt2.grid(column=0, row=1,padx=240,sticky='W')
#------------------------------------------------------------------------



#button3 "9"
def but3():
    global value
    value=value+"9"
    tbv.set(value)


bt3=ttk.Button(win,text="9",command=but3, width=5)
bt3.grid(column=0, row=1,padx=282,sticky='W')
#------------------------------------------------------------------------




#button4 "C"
def but4():
    global value
    value=""
    tbv.set(value)


bt4=ttk.Button(win,text="C",command=but4, width=5)
bt4.grid(column=0, row=1,padx=324,sticky='W')
#------------------------------------------------------------------------




#button5 "*"
def but5():
    global value
    value=value+"*"
    tbv.set(value)


bt5=ttk.Button(win,text="*",command=but5, width=5)
bt5.grid(column=0, row=1,padx=366,sticky='W')
#------------------------------------------------------------------------




#button6 "/"
def but6():
    global value
    value=value+"/"
    tbv.set(value)


bt6=ttk.Button(win,text="/",command=but6, width=5)
bt6.grid(column=0, row=1,padx=408,sticky='W')
#------------------------------------------------------------------------




#button7 "+"
def but7():
    global value
    value=value+"+"
    tbv.set(value)


bt7=ttk.Button(win,text="+",command=but7, width=5)
bt7.grid(column=0, row=1,padx=450,sticky='W')

#------------------------------------------------------------------------






#button8 "4"
def but8():
    global value
    value=value+"4"
    tbv.set(value)


bt8=ttk.Button(win,text="4",command=but8, width=5)
bt8.grid(column=0, row=2,padx=198,sticky='W')
#------------------------------------------------------------------------




#button9 "5"
def but9():
    global value
    value=value+"5"
    tbv.set(value)


bt9=ttk.Button(win,text="5",command=but9, width=5)
bt9.grid(column=0, row=2,padx=240,sticky='W')
#------------------------------------------------------------------------




#button10 "6"
def but10():
    global value
    value=value+"6"
    tbv.set(value)


bt10=ttk.Button(win,text="6",command=but10, width=5)
bt10.grid(column=0, row=2,padx=282,sticky='W')
#------------------------------------------------------------------------



#button11 "-"
def but11():
    global value
    value=value+"-"
    tbv.set(value)


bt11=ttk.Button(win,text="-",command=but11, width=15)
bt11.grid(column=0, row=2,padx=344,sticky='W')
#------------------------------------------------------------------------




#button12 "1"
def but12():
    global value
    value=value+"1"
    tbv.set(value)


bt12=ttk.Button(win,text="1",command=but12, width=5)
bt12.grid(column=0, row=3,padx=198,sticky='W')
#------------------------------------------------------------------------




#button13 "2"
def but13():
    global value
    value=value+"2"
    tbv.set(value)


bt13=ttk.Button(win,text="2",command=but13, width=5)
bt13.grid(column=0, row=3,padx=240,sticky='W')
#------------------------------------------------------------------------



#button14 "3"
def but14():
    global value
    value=value+"3"
    tbv.set(value)


bt14=ttk.Button(win,text="3",command=but14, width=5)
bt14.grid(column=0, row=3,padx=282,sticky='W')
#------------------------------------------------------------------------





#button15 "="  printing the result
def but15():
    global value

    tbv.set(eval(value))


bt15=ttk.Button(win,text="=",command=but15, width=15)
bt15.grid(column=0, row=3,padx=344,sticky='W')
#------------------------------------------------------------------------





#button16 "0"
def but16():
    global value
    value=value+"0"
    tbv.set(value)


bt16=ttk.Button(win,text="0",command=but16, width=5)
bt16.grid(column=0, row=4,padx=198,sticky='W')
#------------------------------------------------------------------------




#button17 "."
def but17():
    global value
    value=value+"."
    tbv.set(value)


bt17=ttk.Button(win,text=".",command=but17, width=5)
bt17.grid(column=0, row=4,padx=240,sticky='W')
#------------------------------------------------------------------------




#button18 "("
def but18():
    global value
    value=value+"("
    tbv.set(value)


bt18=ttk.Button(win,text="(",command=but18, width=5)
bt18.grid(column=0, row=4,padx=282,sticky='W')
#------------------------------------------------------------------------





#button19 ")"
def but19():
    global value
    value=value+")"
    tbv.set(value)


bt19=ttk.Button(win,text=")",command=but19, width=5)
bt19.grid(column=0, row=4,padx=344,sticky='W')
#------------------------------------------------------------------------



win.mainloop()