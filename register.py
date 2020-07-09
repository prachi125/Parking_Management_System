from tkinter import*
root=Tk()

l=Label(root,text="INFO",fg="black").grid(row=0,column=2)
l1=Label(root,text="Name")
l1.grid()

Entry(root).grid(row=1,column=2)
l1=Label(root,text="Reg.No")
l1.grid()

Entry(root).grid(row=2,column=2)
l1=Label(root,text="Hostel/Block")
l1.grid()

Entry(root).grid(row=3,column=2)
l1=Label(root,text="Mobile no")
l1.grid()

Entry(root).grid(row=4,column=2)
l1=Label(root,text="Gender")
l1.grid()

R1 = Radiobutton(root, text="Male",value=0)
R1.grid(row=5,column=2)
R2 = Radiobutton(root, text="Female",value=1)
R2.grid(row=5,column=3)

l1=Label(root,text="Email Id")
l1.grid()
Entry(root).grid(row=6,column=2)


b=Button(root,text="Submit").grid(row=7,column=2)

root.mainloop()
