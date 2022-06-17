from tkinter import *
import sqlite3
from tkinter import messagebox
root=Tk()
root.title("facebook")
con=sqlite3.connect("facebook.db")
root.iconbitmap("facebook.ico")
root.config(bg="blue")
c=con.cursor()
# c.execute("""CREATE TABLE facebook(
#     first_name text,
#     last_name text,
#     address text,
#     age text,
#     password text,
#     father_name text,        
#     city text,
#     zipcode integer
# )""")
# print("tabel created sucessfully")
def submit():
    con=sqlite3.connect("facebook.db")
    c=con.cursor()
    c.execute("INSERT INTO facebook VALUES(:f_name,:l_name,:address,:age,:password,:father_name,:city,:zipcode)",{
    'f_name':f_name.get(),
    'l_name':l_name.get(),
    'address':address.get(),
    'age':age.get(),
    'password':password.get(),
    'father_name':father_name.get(),
    'city':city.get(),
    'zipcode':zipcode.get()
    })
    messagebox.showinfo("facebook","Inserted Sucessfully")
    con.commit()
    con.close() 

def query():
    con = sqlite3.connect("facebook.db")  
    c = con.cursor()
    c.execute("SELECT * , oid FROM facebook")
    records = c.fetchall()
    print(records)
    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[8]) + "\n"
    query_label = Label(root, text = print_record,bg="green",fg="black")
    query_label.grid(row=10, column = 0, columnspan=2)
    con.commit()
    con.close() 

def delete():
    conn = sqlite3.connect("facebook.db")
    c = conn.cursor()
    c.execute("DELETE from facebook WHERE oid = " + delete_box.get())
    print("DELETED SUCESSFULLY")
    delete_box.delete(0,END)
    conn.commit()
    conn.close()

def update():
    con = sqlite3.connect("facebook.db")
    c = con.cursor()
    record_id = update_box.get()
    c.execute("""UPDATE facebook SET
    first_name=:first,
    last_name=:last,
    address=:address,
    age=:age,
    password=:password,
    father_name=:father_name,
    city=:city,
    zipcode=:zipcode
    WHERE oid  = :oid""",
    {'first': f_name_editor.get(),
    'last': l_name_editor.get(),
    'address': address_editor.get(),
    'age': age_editor.get(),
    'password':password_editor.get(),
    'father_name':father_name_editor.get(),
    'city':city_editor.get(),
    'zipcode': zip_code_editor.get(),
    'oid' : record_id
        }
    )
    con.commit()
    con.close()
    editor.destroy()

def edit():
    global editor
    editor = Toplevel()
    editor.title("Update Data")
    editor.iconbitmap('facebook.ico')
    editor.geometry("300x400")
    editor.config(bg="blue")
    conn = sqlite3.connect("facebook.db")
    c = conn.cursor()
    record_id = update_box.get()
    c.execute("SELECT * FROM facebook WHERE oid= " + record_id)
    records = c.fetchall()
    global f_name_editor
    global l_name_editor
    global address_editor
    global age_editor
    global password_editor
    global father_name_editor
    global city_editor
    global zip_code_editor

    f_name_editor = Entry(editor, width = 30)
    f_name_editor.grid(row = 0, column = 1, padx = 20, pady =(10,0))

    l_name_editor = Entry(editor, width = 30)
    l_name_editor.grid(row = 1, column = 1)

    address_editor = Entry(editor, width = 30)
    address_editor.grid(row = 2, column = 1)

    age_editor = Entry(editor, width = 30)
    age_editor.grid(row = 3, column = 1)

    password_editor = Entry(editor, width = 30)
    password_editor.grid(row = 4, column = 1)

    father_name_editor = Entry(editor, width = 30)
    father_name_editor.grid(row = 5, column = 1)

    city_editor = Entry(editor, width = 30)
    city_editor.grid(row = 6, column = 1)

    zip_code_editor = Entry(editor, width = 30)
    zip_code_editor.grid(row = 7, column = 1)

    f_name_label= Label(editor, text = "First Name",bg="blue",fg="white")
    f_name_label.grid(row = 0, column = 0)

    l_name_label= Label(editor, text = "Last Name",bg="blue",fg="white")
    l_name_label.grid(row = 1, column = 0)

    address_label= Label(editor, text = "Address",bg="blue",fg="white")
    address_label.grid(row = 2, column = 0)

    age_label= Label(editor, text = "Age",bg="blue",fg="white")
    age_label.grid(row = 3, column = 0)

    password_label= Label(editor, text = "password",bg="blue",fg="white")
    password_label.grid(row = 4, column = 0)

    father_name_label= Label(editor, text = "fathername",bg="blue",fg="white")
    father_name_label.grid(row = 5, column = 0)

    city_label= Label(editor, text = "City",bg="blue",fg="white")
    city_label.grid(row = 6, column = 0)
    
    zip_code_label= Label(editor, text = "Zip Code",bg="blue",fg="white")
    zip_code_label.grid(row = 7, column = 0)

 

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        age_editor.insert(0,record[3])
        password_editor.insert(0,record[4])
        father_name_editor.insert(0,record[5])
        city_editor.insert(0,record[6])
        zip_code_editor.insert(0,record[7])
    edit_btn = Button(editor, text = "Save",command= update)
    edit_btn.grid(row = 8, column=0, columnspan=2, pady = 10, padx = 10, ipadx=125)
    # conn.commit()
    # conn.close()




f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

 

address=Entry(root,width=30)
address.grid(row=2,column=1)

age=Entry(root,width=30)
age.grid(row=3,column=1)

password=Entry(root,width=30)
password.grid(row=4,column=1)

father_name=Entry(root,width=30)
father_name.grid(row=5,column=1)

city=Entry(root,width=30)
city.grid(row=6,column=1)

 

zipcode=Entry(root,width=30)
zipcode.grid(row=7,column=1)

 

f_name_label=Label(root,text="first name",bg="blue",fg="white")
f_name_label.grid(row=0,column=0)

 

l_name_label=Label(root,text="last name",bg="blue",fg="white")
l_name_label.grid(row=1,column=0)

 

address_label=Label(root,text="address",bg="blue",fg="white")
address_label.grid(row=2,column=0)

age_label=Label(root,text="age",bg="blue",fg="white")
age_label.grid(row=3,column=0)

password_label=Label(root,text="password",bg="blue",fg="white")
password_label.grid(row=4,column=0)

father_name_label=Label(root,text="fathername",bg="blue",fg="white")
father_name_label.grid(row=5,column=0)

city_label=Label(root,text="city",bg="blue",fg="white")
city_label.grid(row=6,column=0)

 
zipcode_label=Label(root,text="zipcode",bg="blue",fg="white")
zipcode_label.grid(row=7,column=0)

 

delete_label = Label(root,text = "Delete ID",bg="blue",fg="white")
delete_label.grid(row=11, column=0)

 

delete_box = Entry(root, width = 30)
delete_box.grid(row = 11, column=1, pady = 5)

 

submit_btn=Button(root,text="add records",command=submit)
submit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

 

query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row = 9, column = 0, columnspan=2, pady=10, padx=10, ipadx= 120)

 

delete_btn = Button(root,text = "Delete", command=delete)
delete_btn.grid(row = 12 , column = 0, columnspan=2, pady=10, padx=10, ipadx=120)


update_label = Label(root,text = "Update ID",bg="blue",fg="white")
update_label.grid(row=13, column=0)

 

update_box = Entry(root, width = 30)
update_box.grid(row = 13, column=1, pady = 5)
 

edit_btn = Button(root, text = "Update", command=edit)
edit_btn.grid(row=14, column=0, columnspan=2, padx=10, pady =10, ipadx = 120)

con.commit()
con.close()

root.mainloop()