from tkinter import *
import time
import mysql.connector
from tkinter import ttk,messagebox,filedialog
#import panda
def clock():
    date=time.strftime('%d/%m/%Y')
    newtime=time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'   date:{date}\ntime:{newtime}')
    datetimelabel.after(1000,clock)

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['admission no','Name','EMIS no','date of birth','house','Gender','new or old','Added Date','Added father occupation'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')


def toplevel_data(title,button_text,command):
    global nameEntry,emisnoEntry,emailEntry,genderEntry,fathernameEntry,fatheroccupation,EntryfatherannualincomeEntry,officeadressEntry,fatherphonenoEntry,mothernameEntry,motherphonenoEntry,motheroccupationEntry,motherannualincomeEntry
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    
    idLabel = Label(screen, text='admission no', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=6, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=2)
    
    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=6, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=2)

    emisnoLabel = Label(screen, text='emis no', font=('times new roman', 20, 'bold'))
    emisnoLabel.grid(row=2, column=0, padx=6, pady=15, sticky=W)
    emisnoEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emisnoEntry.grid(row=2, column=1, pady=15, padx=2)

    emailLabel = Label(screen, text='date of birth', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=6, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=2)

    genderLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=4, column=0, padx=6, pady=15, sticky=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=4, column=1, pady=15, padx=2)

    
    fathernameLabel = Label(screen, text='fathername', font=('times new roman', 20, 'bold'))
    fathernameLabel.grid(row=5, column=0, padx=6, pady=15, sticky=W)
    fathernameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    fathernameEntry.grid(row=5, column=1, pady=15, padx=2)

    fatheroccupationLabel = Label(screen, text='fatheroccupation', font=('times new roman', 20, 'bold'))
    fatheroccupationLabel.grid(row=6, column=0, padx=6, pady=15, sticky=W)
    fatheroccupationEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    fatheroccupationEntry.grid(row=6, column=1, pady=15, padx=2)

    fatherannualincomeLabel = Label(screen, text='fatherannualincome', font=('times new roman', 20, 'bold'))
    fatherannualincomeLabel.grid(row=7, column=0, padx=6, pady=15, sticky=W)
    fatherannualincomeEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    fatherannualincomeEntry.grid(row=7, column=1, pady=15, padx=2)

    fatherphoneLabel = Label(screen, text='father phone no', font=('times new roman', 20, 'bold'))
    fatherphoneLabel.grid(row=8, column=0, padx=6, pady=15, sticky=W)
    fatherphoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    fatherphoneEntry.grid(row=8, column=1, pady=15, padx=2)

    mothernameLabel = Label(screen, text='mothername', font=('times new roman', 20, 'bold'))
    mothernameLabel.grid(row=9, column=0, padx=6, pady=15, sticky=W)
    mothernameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    mothernameEntry.grid(row=9, column=1, pady=15, padx=2)

    motherphoneLabel = Label(screen, text='mother  phone no', font=('times new roman', 20, 'bold'))
    motherphoneLabel.grid(row=10, column=0, padx=6, pady=15, sticky=W)
    motherphoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    motherphoneEntry.grid(row=10, column=1, pady=15, padx=2)

    motheroccupationLabel = Label(screen, text='mother occupation', font=('times new roman', 20, 'bold'))
    motheroccupationLabel.grid(row=11, column=0, padx=6, pady=15, sticky=W)
    motheroccupationEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    motheroccupationEntry.grid(row=11, column=1, pady=15, padx=2)

    motherannualincomeLabel = Label(screen, text='mother annual income', font=('times new roman', 20, 'bold'))
    motherannualincomeLabel.grid(row=12, column=0, padx=6, pady=15, sticky=W)
    motherannualincomeEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    motherannualincomeEntry.grid(row=12, column=1, pady=15, padx=2)

    scrollbarx=Scrollbar(screen,orient='horizontal')
    scrollbary=Scrollbar(screen,orient='vertical')

    
    scrollbary.grid(row=0,column=3,sticky='ns')


    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=7, columnspan=2, pady=15)
    if title=='Update Student':
        indexing = studentTable.focus()

        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        emisnoEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        
        genderEntry.insert(0, listdata[5])
        
        fathernameEntry.insert(0, listdata[7])
        fatheroccupationEntry.insert(0, listdata[8])
        fatherannualincomeEntry.insert(0, listdata[9])
        officeadressEntry.insert(0, listdata[10])
        fatherphonenoEntry.insert(0, listdata[11])
        mothernameEntry.insert(0, listdata[12])
        motherphonenoEntry.insert(0, listdata[13])
        motheroccupationEntry.insert(0, listdata[14])
        motherannualincomeEntry.insert(0,listdata[15])

def update_data():
    query='update student set name=%s,emisno=%s,dateofbirth=%s,,gender=%s,,fathername=%s,fatheroccupation=%s,fatherannualincome=%s,officeadress=%s,fatherphoneno=%s,mothername=%s,motherphoneno=%s,motheroccupation=%s,motherannualincome=%s where admissionno=%s'
    mycursor.execute(query,(nameEntry.get(),emisnoEntry.get(),emailEntry.get(),genderEntry.get(),fathernameEntry.get(),fatheroccupationEntry.get(),fatherannualincomeEntry.get(),officeadressEntry.get(),fatherphonenoEntry.get(),mothernameEntry.get(),motherphonenoEntry.get(),motheroccupationEntry.get(),motherannualincomeEntry.get()))

    

    con.commit()
    messagebox.showinfo('Success',f'admission no {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()



def show_student():
    global mycursor
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)



def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where admissionno=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'admissionno {content_id} is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)




def search_data():
    query='select * from student where admission no=%s or name=%s or date of birth=%s or EMIS no=%s or house=%s or gender=%s or new or old=%s'
    mycursor.execute(query,(nameEntry.get(),emisnoEntry.get(),emailEntry.get(),genderEntry.get(),fathernameEntry.get(),fatheroccupationEntry.get(),fatherannualincomeEntry.get(),officeadressEntry.get(),fatherphonenoEntry.get(),mothernameEntry.get(),motherphonenoEntry.get(),motheroccupationEntry.get(),motherannualincomeEntry.get()))

    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)




def add_data():
    global screen
    if nameEntry.get()=='' or emisnoEntry.get()=='' or emailEntry.get()=='' or genderEntry.get()=='' or fathernameEntry.get()=='' or fatheroccupationEntry.get()=='' or fatherannualincomeEntry.get()=='' or officeadressEntry.get()=='' or fatherphonenoEntry.get()=='' or mothernameEntry.get()=='' or motherphonenoEntry.get()=='' or motheroccupationEntry.get()=='' or motherannualincomeEntry.get()=='':

    
        messagebox.showerror('Error','All Feilds are required',parent=screen)

    else:
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(nameEntry.get(),emisnoEntry.get(),emailEntry.get(),genderEntry.get(),fathernameEntry.get(),fatheroccupationEntry.get(),fatherannualincomeEntry.get(),officeadressEntry.get(),fatherphonenoEntry.get(),mothernameEntry.get(),motherphonenoEntry.get(),motheroccupationEntry.get(),motherannualincomeEntry.get()))

            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                nameEntry.delete(0,END)
                emisnoEntry.delete(0,END)
                emailEntry.delete(0,END)
                
                genderEntry.delete(0,END)
                
                fathernameEntry.delete(0,END)
                fatheroccupationEntry.delete(0,END)
                fatherannualincomeEntry.delete(0,END)
                officeadressEntry.delete(0,END)
                fatherphonenoEntry.delete(0,END)
                mothernameEntry.delete(0,END)
                motherphonenoEntry.delete(0,END)
                motheroccupationEntry.delete(0,END)
                motherannualincomeEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','admission no cannot be repeated',parent=screen)
            return


        query='select *from student'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(admissionno int not null primary key,name varchar(30),EMISno varchar(10),dateofbirth varchar(30),' \
                  'house varchar(100),gender varchar(20),neworold varchar(20),fathername varchar(50),fatheroccupation varchar(50),' \
                  'fatherannualincome int,officeadress varchar(100),fatherphoneno int,mothername varchar(50),motherphoneno int,' \
                  'motheroccupation varchar(100),officeaddress varchar(100),motherannualincome int,transportation varchar(50))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addstudentbutton.config(state=NORMAL)
        searchstudentbutton.config(state=NORMAL)
        updatestudentbutton.config(state=NORMAL)
        showstudentbutton.config(state=NORMAL)
        exportstudentbutton.config(state=NORMAL)
        deletestudentbutton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)




count=0
text=""
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderlabel.config(text=text)
    count+=1
    sliderlabel.after(300,slider)
    
root=Tk()

root.geometry('1366x768+0+0')

root.title("student tracker ")
backgroundImage=PhotoImage(file=r"C:\Users\IdeaPad\AppData\Local\Programs\Python\Python39\background.png.png")

bglabel=Label(root,image=backgroundImage)
bglabel.place(x=0,y=0)


datetimelabel=Label(root,font=('OpenSymbol',16,'italic'))
datetimelabel.place(x=5,y=5,)

clock()

s="student tracker"
sliderlabel=Label(root,text=s,font=('Noto Sans CJK TC',22,"italic bold"),width=30)
sliderlabel.place(x=400,y=1)


slider()

connectbutton=ttk.Button(root,text="access database",command=connect_database)
connectbutton.place(x=1075,y=1)


leftframe=Frame(root,bg="lime green")
leftframe.place(x=35,y=80,width=300,height=1000,)

logoimage=PhotoImage(file=r"C:\Users\IdeaPad\AppData\Local\Programs\Python\Python39\graduates.png")
logolabel=Label(leftframe,image=logoimage)
logolabel.grid(row=0,column=0,pady=10)

addstudentbutton=ttk.Button(leftframe,text="add student details",command=lambda :toplevel_data('Add Student','Add',add_data))
addstudentbutton.grid(row=1,column=0,pady=20,padx=80)

searchstudentbutton=ttk.Button(leftframe,text="search student details",command=lambda :toplevel_data('Search Student','Search',search_data,))
searchstudentbutton.grid(row=2,column=0,pady=20,padx=80)


updatestudentbutton=ttk.Button(leftframe,text="update student details",command=lambda :toplevel_data('Update Student','Update',update_data,))
updatestudentbutton.grid(row=3,column=0,pady=20,padx=80)


deletestudentbutton=ttk.Button(leftframe,text="delete student details",command=delete_student)
deletestudentbutton.grid(row=4,column=0,pady=20,padx=80)


exportstudentbutton=ttk.Button(leftframe,text="export student details",command=export_data)
exportstudentbutton.grid(row=5,column=0,pady=20,padx=80)


showstudentbutton=ttk.Button(leftframe,text=" show  student details",command=show_student,)
showstudentbutton.grid(row=6,column=0,pady=20,padx=80)


markstudentbutton=ttk.Button(leftframe,text="           marks            ",)
markstudentbutton.grid(row=7,column=0,pady=20,padx=80)


exitstudentbutton=ttk.Button(leftframe,text="             exit             ",command=iexit)
exitstudentbutton.grid(row=8,column=0,pady=20,padx=80)


rightframe=Frame(root,bg="gold")
rightframe.place(x=400,y=80,width=950,height=600,)

scrollbarx=Scrollbar(rightframe,orient='horizontal')
scrollbary=Scrollbar(rightframe,orient='vertical')

studenttable=ttk.Treeview(rightframe,column=('admission no','name','EMIS NO ','date of birth','house','gender','new or old','father name','father occupation','father annual income','office adress','father phone no','mother name','mother phone no','mother occupation','office address','mother annual income','transportation'),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)

scrollbarx.config(command=studenttable.xview)
scrollbary.config(command=studenttable.yview)

             
scrollbarx.pack(side=BOTTOM,fill=X)
scrollbary.pack(side=RIGHT,fill=Y)
studenttable.pack(fill=BOTH,expand=1)

studenttable.heading('admission no',text='admission no')
studenttable.heading('name',text='name')
studenttable.heading('EMIS NO ',text='EMIS NO ')
studenttable.heading('date of birth',text='date of birth')
studenttable.heading('house',text='house')
studenttable.heading('gender',text='gender')
studenttable.heading('new or old',text='new or old')

studenttable.heading('father name',text='father name')
studenttable.heading('father occupation',text='father occupation')
studenttable.heading('father annual income',text='father annual income')
studenttable.heading('office address',text='office address')
studenttable.heading('father phone no',text='father phone no')
studenttable.heading('mother name',text='mother name')
studenttable.heading('mother phone no',text='mother phone no')
studenttable.heading('mother occupation',text='mother occupation')
studenttable.heading('office adress',text='office adress')
studenttable.heading('mother annual income',text='mother annual income')
studenttable.heading('transportation',text='transportation')

style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='gold', background='gold',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')
studenttable.config(show='headings')









root.mainloop()
