from tkinter import *
from tkinter import messagebox
def login():
    if usernameentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror("error","enter valid password")
    elif usernameentry.get()=='project' or passwordentry.get()=='1234':
        messagebox.showinfo("valid","welcome")
        window.destroy()
        import studsys
        
    else:
        messagebox.showerror("error","please enter correct credentials")
        
window=Tk()
window.geometry("1628x720+0+0")
window.title("login system")
backgroundImage=PhotoImage(file="background.png")

bglabel=Label(window,image=backgroundImage)
bglabel.place(x=0,y=0)

loginframe=Frame(window,bg="white")
loginframe.place(x=500,y=100)

logoimage=PhotoImage(file=r"logo.png")
logolabel=Label(loginframe,image=logoimage)

logolabel.grid(row=0,column=0,columnspan=3,pady=10)

usernameImage=PhotoImage(file=r"user.png")
usernamelabel=Label(loginframe,image=usernameImage,text='username',compound=LEFT,font=('Ubuntu',18,'bold'),bg='white')
usernamelabel.grid(row=1,column=0,pady=10,padx=20)


usernameentry=Entry(loginframe,font=('Ubuntu',18,'bold'),bd=5,fg='green')
usernameentry.grid(row=1,column=1,pady=10,padx=20)



passwordimage=PhotoImage(file=r"password.png")
passwordlabel=Label(loginframe,image=passwordimage,text='password',compound=LEFT,font=('Ubuntu',18,'bold'),bg='white')
passwordlabel.grid(row=2,column=0,pady=10,padx=20)


passwordentry=Entry(loginframe,font=('Ubuntu',18,'bold'),bd=5,fg='royalblue')
passwordentry.grid(row=2,column=1,pady=10,padx=20)

loginbutton=Button(loginframe,text='login',font=('Ubuntu',18,'bold'),width=15,fg="red",bg="cornflowerblue",cursor="hand2",command=login)
loginbutton.grid(row=3,column=1,pady=10,)




window.mainloop()

