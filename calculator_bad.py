from tkinter import *
root=Tk()
root.title("himanshu kumaR SHArma")

root.configure(background="#222c35")

"""function"""
def click(event):
   text=event.widget.cget('text')

   if text=="=":
       if inp.get().isdigit():
           value = int(inp.get())

       try:
            print(inp.get())

            value=eval(e.get())

       except Exception as f:
           value="Invalid Syntax \U0001F928"
           print(f)
       inp.set(value)
       e.update()



   elif text=="C":
       inp.set("")
       e.update()
   else:
       inp.set(inp.get()+text)

"""variables"""
inp=StringVar()

"""entery widget"""

e=Entry(root, state=NORMAL,bg="white",textvariable=inp,font="lucida 30 bold ",bd=5,relief=SUNKEN)
e.pack(fill=BOTH,padx=20,pady=30)


"""status bar"""

g=Label(root,anchor="s",bg="#a0debf",text="calculating..")
g.pack(side=BOTTOM,fill=X)


"""time for frame"""
k1=Frame(root,bg="#222c35",padx=10)
k1.pack(anchor="w",fill=BOTH)
k2=Frame(root,bg="#222c35",padx=10)
k2.pack(anchor="w",fill=BOTH,)
k3=Frame(root,bg="#222c35",padx=10)
k3.pack(anchor="w",fill=BOTH,)
k4=Frame(root,bg="#222c35")
k4.pack(anchor="w",fill=BOTH,padx=10)
k5=Frame(root,bg="#222c35",padx=10)
k5.pack(anchor="w",fill=BOTH,)



"""button"""

for i in range(9,0,-1):
    if i>6:
        b=Button(k1,text=str(i),font="impact 20 bold ",fg="#ec6d10",padx=22,pady=20)
        b.pack(side=LEFT,fill=BOTH,padx=5,pady=4)
        b.bind("<Button-1>", click)
    elif i>3:

        b = Button(k2, text=str(i), font="impact 20 bold ", fg="#ec6d10",padx=22,pady=20)
        b.pack(side=LEFT, fill=BOTH,padx=5,pady=4)
        b.bind("<Button-1>", click)
    else:
        b = Button(k3, text=str(i), font="impact 20 bold ", fg="#ec6d10",padx=22,pady=20)
        b.pack(side=LEFT, fill=BOTH,padx=5,pady=4)
        b.bind("<Button-1>", click)

b = Button(k4, text="C", font="impact 20 bold ", fg="red", padx=22, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=5, pady=4)
b.bind("<Button-1>", click)
b = Button(k4, text="0", font="impact 20 bold ", fg="#ec6d10", padx=22, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=5, pady=4)
b.bind("<Button-1>", click)
b = Button(k4, text=".", font="impact 20 bold ", fg="blue", padx=25, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=5, pady=4)
b.bind("<Button-1>", click)


b = Button(k1, text="+", font="impact 20 bold ", fg="blue", padx=22, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=5, pady=4)
b.bind("<Button-1>", click)

b = Button(k2, text="-", font="impact 20 bold ", fg="blue", padx=25, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(k3, text="*", font="impact 20 bold ", fg="blue", padx=26, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=6, pady=4)
b.bind("<Button-1>", click)

b = Button(k4, text="/", font="impact 20 bold ", fg="blue", padx=24, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=6, pady=4)
b.bind("<Button-1>", click)




b = Button(k5, text="=", font="impact 20 bold ", fg="green", padx=24, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=6, pady=4)
b.bind("<Button-1>", click)
b = Button(k5, text="00", font="impact 20 bold ", fg="#ec6d10", padx=30, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=6, pady=4)
b.bind("<Button-1>", click)
b = Button(k5, text="%", font="impact 20 bold ", fg="blue", padx=43, pady=20)
b.pack(side=LEFT, fill=BOTH, padx=6, pady=4)
b.bind("<Button-1>", click)



root.mainloop()