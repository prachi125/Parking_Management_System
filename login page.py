from tkinter import*
root=Tk()

l=Label(root,text="User").grid(row=0,column=2)

l1=Label(root,text="User Name")
l1.grid()
Entry(root).grid(row=1,column=2)

l1=Label(root,text="Password")
l1.grid()
Entry(root).grid(row=2,column=2)

top=Tk()
top.geometry("500x400")
top.title("Login")
username=StringVar()
l1=Label(top,text="Username")
l1.place(x=150,y=150)
e1=Entry(top,bd=5,textvariable=username)
e1.place(x=230,y=150)
password=StringVar()
l2=Label(top,text="Password")
l2.place(x=150,y=200)
e2=Entry(top,bd=5,textvariable=password)
e2.place(x=230,y=200)

b4=Button(top,text="Login",bg="Skyblue",command=lambda:login_user(username.get()))
b4.place(x=150,y=250,height=40,width=70)

b5=Button(top,text="New User",bg="Skyblue",command=new_user)
b5.place(x=250,y=250,height=40,width=70)



b=Button(root,text="Login Now", bg="powder blue").grid(row=3,column=2)
b=Button(root,text="New User",bg="powder blue").grid(row=3,column=3)

root.mainloop()
