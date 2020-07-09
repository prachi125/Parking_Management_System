from tkinter import *
from tkinter import messagebox 
import sqlite3
window=Tk()
window.title("PARKING MANAGEMENT SYSTEM")

def login_user(username):
    con=sqlite3.connect("create.db")
    cur=con.cursor()
    cur.execute("select * from user1")
    col=cur.fetchall()
    for i in col:
        if(i[0]==username):
            messagebox.showinfo("Login","You have been successfully logged in")
            available_parking()
            break
def create_order(username,regno,vehicle):
    messagebox.showinfo("top2","amount to be paid 10 ")
    con=sqlite3.connect("pms3.db")
    cur=con.cursor()
    cur.execute("create table if not exists pms3(username varchar(20),regno varchar(20),vehicle varchar(20))")
    cur.execute("insert into pms3 values(?,?,?)",(username,regno,vehicle))
    con.commit()
    con.close()


def create_user(name,gender,email,mobile,hostel):
    con=sqlite3.connect("createuser.db")
    cur=con.cursor()
    cur.execute("create table if not exists user1(name varchar(20),gender number(2),email varchar(20),mobile number(20),hostel varchar(20))")
    if(gender==1):
        cur.execute("insert into user1 values(?,?,?,?,?)",(name,"Male",email,mobile,hostel))
    else:
        cur.execute("insert into user1 values(?,?,?,?,?)",(name,"Female",email,mobile,hostel))
        cur.execute("select * from user1")
    con.commit()
    con.close()



def login():
    top=Tk()
    top.geometry("500x400")
    top.title("Login")
    c1=Canvas(top,bg='grey',width=500,height=400)
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
    c1.pack()

def new_user():
    top2=Tk()
    top2.geometry("400x400")
    top2.title("New User")

    c1=Canvas(top2,bg='grey',width=600,height=700)
    c1.pack()
    e3_value=StringVar()
    l3=Label(top2,text="Name")
    l3.place(x=100,y=100)
    e3=Entry(top2,bd=4,textvariable=e3_value)
    e3.place(x=170,y=100)


    c1_value=IntVar()

    l4=Label(top2,text="Gender")
    l4.place(x=100,y=140)
    c1=Radiobutton(top2,text="Male",value=1,variable=c1_value)
    c1.place(x=170,y=140)
    c2=Radiobutton(top2,text="Female",value=2,variable=c1_value)
    c2.place(x=240,y=140)

    e5_value=StringVar()
    l5=Label(top2,text="Email")
    l5.place(x=100,y=180)
    e5=Entry(top2,bd=4,textvariable=e5_value)
    e5.place(x=170,y=180)

    e6_value=StringVar()
    l6=Label(top2,text="Mobile No")
    l6.place(x=100,y=220)
    e6=Entry(top2,bd=4,textvariable=e6_value)
    e6.place(x=170,y=220)

    e7_value=StringVar()
    l7=Label(top2,text="Hostel/Block")
    l7.place(x=100,y=260)
    e7=Entry(top2,bd=4,textvariable=e7_value)
    e7.place(x=170,y=260)

    b6=Button(top2,text="Submit",bg="Skyblue",command=lambda:create_user(e3_value.get(),c1_value.get(),e5_value.get(),e6_value.get(),e7_value.get()))
    b6.place(x=150,y=300,height=40,width=70)
    

            

def order():
    
    top4=Toplevel()
    top4.geometry("400x400")
    top4.title("Order")
    c1=Canvas(top4,bg='grey',width=600,height=700)
    c1.pack()

    e10_value=StringVar()
    l10=Label(top4,text="Username")
    l10.place(x=100,y=100)
    e10=Entry(top4,bd=4,textvariable=e10_value)
    e10.place(x=170,y=100)
    
    e11_value=StringVar()
    l11=Label(top4,text="Reg.no")
    l11.place(x=100,y=140)
    e11=Entry(top4,bd=4,textvariable=e11_value)
    e11.place(x=170,y=140)


    r_value=IntVar()
    l12=Label(top4,text="Vehicle")
    l12.place(x=100,y=180)
    r1=Radiobutton(top4,text="2-Wheeler",value=2,variable=r_value)
    r1.place(x=170,y=180)
    r2=Radiobutton(top4,text="4-Wheeler",value=4,variable=r_value)
    r2.place(x=260,y=180)
    
    
    b7=Button(top4,text="Submit",bg="Skyblue",command=lambda:create_order(e10_value.get(),e11_value.get(),r_value.get()))
    b7.place(x=195,y=220,height=40,width=70)
    
    

def available_parking():
    top5=Toplevel()
    top5.geometry("500x500")
    top5.title("Available Parking")

    c1=Canvas(top5,bg='grey',width=600,height=700)
    c1.pack()
    
    l=Label(top5,text="PLEASE SELECT THE BLOCK",font=("Arial Bold", 25)).place(x=10,y=0)
    
    b8=Button(top5,text="14 Block",command=order,bg="Skyblue")
    b8.place(x=180,y=50,height=40,width=90)

    b9=Button(top5,text="29 Block",command=order,bg="Skyblue")
    b9.place(x=180,y=110,height=40,width=90)
    
    b10=Button(top5,text="34 Block",command=order,bg="Skyblue")
    b10.place(x=180,y=170,height=40,width=90)

    b11=Button(top5,text="BH-1",command=order,bg="Skyblue")
    b11.place(x=180,y=230,height=40,width=90)

    b12=Button(top5,text="BH-4",command=order,bg="Skyblue")
    b12.place(x=180,y=290,height=40,width=90)

    b13=Button(top5,text="BH-5",command=order,bg="Skyblue")
    b13.place(x=180,y=350,height=40,width=90)

    b14=Button(top5,text="55-56 Block",command=order,bg="Skyblue")
    b14.place(x=180,y=410,height=40,width=90)


window.geometry("500x200")

c1=Canvas(window,bg='grey',width=600,height=700)
c1.pack()
l1=Label(window,text='PARKING MANAGEMENT SYSTEM',font="Times")
l1.place(x=120,y=20)
b1=Button(window,text="Login",bg="Skyblue",command=login)
b1.place(x=70,y=70,height=40,width=70)
b2=Button(window,text="New User",bg="Skyblue",command=new_user)
b2.place(x=175,y=70,height=40,width=80)
b3=Button(window,text="Available Parking",bg="Skyblue",command=available_parking)
b3.place(x=300,y=70,height=40,width=120)


window.mainloop()
