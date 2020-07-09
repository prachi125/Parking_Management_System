from tkinter import*
root=Tk()


l=Label(root,text="User").grid(row=0,column=2)
l1=Label(root,text="Reg. No")
l1.grid()
Entry(root).grid(row=1,column=2)

l1=Label(root,text="Parking Block")
l1.grid()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text = "34 block",
                 variable = CheckVar1, onvalue = 1, offvalue = 0)
C2 = Checkbutton(root, text = "29 block",
                 variable = CheckVar2, onvalue = 1, offvalue = 0)
C1.grid(row=2,column=2)
C2.grid(row=2,column=3)

l1=Label(root,text="Price")
l1.grid(row=4,column=0)
Entry(root).grid(row=4,column=2)




b=Button(root,text="Order", bg="powder blue").grid(row=5,column=2)


root.mainloop()
