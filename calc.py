from tkinter import *
root=Tk()
root.config(width=800,height=600,bg="yellow")
root.title("Calculator")
root.pack_propagate(0)

t=StringVar()
exp=""

def onclick(num):
    global exp
    exp=exp+str(num)
    t.set(exp)
                        #eval function evaluates the “String” like a python expression and returns the result as an integer.

def equalclick():
    global exp
    add=str(eval(exp))
    t.set(add)
    exp=""

def equalclick():
    global exp
    sub=str(eval(exp))
    t.set(sub)
    exp=""

def equalclick():
    global exp
    mul=str(eval(exp))
    t.set(mul)
    exp=""

def equalclick():
    global exp
    div=str(eval(exp))
    t.set(div)
    exp=""

def clearData():
    t.set("")

l=Label(root,text="CALCULATOR",bg="black",fg="white",font="Comic 25 bold")
l.grid(row=0,column=0,padx=20,pady=20,columnspan=4)

txt=Entry(root, width=20, textvariable=t, bg="white", fg="black", font="Consolas 18 bold")
txt.grid(row=1, column=1, padx=20, pady=20, columnspan=2)

b1=Button(root,text="1", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(1))
b1.grid(row=2, column=0, pady=4, padx=0)

b2=Button(root,text="2", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(2))
b2.grid(row=2, column=1, pady=4, padx=0)

b3=Button(root,text="3", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(3))
b3.grid(row=2, column=2, pady=4, padx=0)

b4=Button(root,text="4", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(4))
b4.grid(row=3, column=0, pady=4, padx=0)

b5=Button(root,text="5", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(5))
b5.grid(row=3, column=1, pady=4, padx=0)

b6=Button(root,text="6", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(6))
b6.grid(row=3, column=2, pady=4, padx=0)

b7=Button(root,text="7", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(7))
b7.grid(row=4, column=0, pady=4, padx=0)

b8=Button(root,text="8", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(8))
b8.grid(row=4, column=1, pady=4, padx=0)

b9=Button(root,text="9", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(9))
b9.grid(row=4, column=2, pady=4, padx=0)

b0=Button(root,text="0", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick(0))
b0.grid(row=5, column=0, pady=4, padx=0)

b10=Button(root,text="Clear", fg="red", bg="white", font="Consolas 20 bold", command=clearData)
b10.grid(row=5, column=1, pady=4, padx=0)

equal=Button(root,text="=", fg="red", bg="white", font="Consolas 20 bold", command=equalclick)
equal.grid(row=5, column=2, pady=4, padx=0)

b12=Button(root,text="+", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick("+"))
b12.grid(row=2, column=3, pady=4, padx=0)

b13=Button(root,text="-", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick("-"))
b13.grid(row=3, column=3, pady=4, padx=0)

b14=Button(root,text="*", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick("*"))
b14.grid(row=4, column=3, pady=4, padx=0)

b15=Button(root,text="/", fg="red", bg="white", font="Consolas 20 bold", command=lambda:onclick("/"))
b15.grid(row=5, column=3, pady=4, padx=0)

root.mainloop()
