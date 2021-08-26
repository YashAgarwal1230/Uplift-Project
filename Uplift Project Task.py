# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
import time
from time import strftime
from pymysql import *


t=tkinter.Tk()
t.title('Service Management System')
t.geometry('1130x1500')
t.resizable(0, 0)
t.config(bg="powder blue")



#======================================================
# SERVICE CENTER

def wid1():
    top=Toplevel()

    def reset():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)


    def service_center_details():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        a5=e5.get()
        a6=e6.get()
        a7=e7.get()
        cur=db.cursor()
        query="insert into service_cntr_details values('%s','%s','%s','%s','%s','%s','%s')"%(a1,a2,a3,a4,a5,a6,a7)
        cur.execute(query)
        db.commit()
        db.close() 

    def serice_c_delete():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        cur=db.cursor()
        query="delete from service_cntr_details where ServiceID=('%s')"%(a1)
        cur.execute(query)
        db.commit()
        db.close()
   
    
        
       
        
        
    
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7

    top.geometry('500x600')
    l1=Label(top,text='Service ID')
    l1.place(x=20,y=90)
    top.config(bg='orange')
    
    e1=Entry(top,width=30)
    e1.place(x=150,y=90)
    
    l2=Label(top,text='Service Name')
    l2.place(x=20,y=140)
    
    e2=Entry(top,width=30)
    e2.place(x=150,y=140)
    
    l3=Label(top,text='Address')
    l3.place(x=20,y=190)
    
    e3=Entry(top,width=30)
    e3.place(x=150,y=190)
    
    l4=Label(top,text='Owner')
    l4.place(x=20,y=240)
    
    e4=Entry(top,width=30)
    e4.place(x=150,y=240)
    
    l5=Label(top,text='Phone')
    l5.place(x=20,y=290)
    
    e5=Entry(top,width=30)
    e5.place(x=150,y=290)
    
    l6=Label(top,text='City')
    l6.place(x=20,y=340)
    
    e6=Entry(top,width=30)
    e6.place(x=150,y=340)
    
    l7=Label(top,text='State')
    l7.place(x=20,y=390)
    
    e7=Entry(top,width=30)
    e7.place(x=150,y=390)
    
    b1=Button(top,text='Save',width=13,command=service_center_details)
    b1.place(x=70,y=450)
    
    b1=Button(top,text='Reset',width=13,command=reset)
    b1.place(x=190,y=450)

    b1=Button(top,text='delete record',width=13,command=serice_c_delete)
    b1.place(x=190,y=500)

    b1=Button(top,text='Show Data',width=13)
    b1.place(x=70,y=500)
    
    
        




    
#==============================================================
# PRODUCTS
def pr():
    pro=Toplevel()

    def reset():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)

    def pro_add():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        cur=db.cursor()
        query="insert into product_details values('%s','%s','%s')"%(a1,a2,a3)
        cur.execute(query)
        db.commit()
        db.close() 


    def pro_update():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        cur=db.cursor()
        query="update product_details set productName = '%s',VARIANT= '%s' where productID='%s'"%(a2,a3,a1)
        cur.execute(query)
        db.commit()
        db.close() 


    def pro_delete():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        cur=db.cursor()
        query="delete from product_details where productID=('%s')"%(a1)
        cur.execute(query)
        db.commit()
        db.close()
        
   
        
    

  
    pro.geometry('500x600')
    l1=Label(pro,text='product ID')
    l1.place(x=20,y=90)
    pro.config(bg='teal')
    
    e1=Entry(pro,width=30)
    e1.place(x=150,y=90)
    
    l2=Label(pro,text='product Name')
    l2.place(x=20,y=140)
    
    e2=Entry(pro,width=30)
    e2.place(x=150,y=140)
    
    l3=Label(pro,text='Veriant')
    l3.place(x=20,y=190)
    
    e3=Entry(pro,width=30)
    e3.place(x=150,y=190)
    
    b1=Button(pro,text='Add',width=13,command=pro_add)
    b1.place(x=70,y=250)
    
    b1=Button(pro,text='Reset',width=13,command=reset)
    b1.place(x=190,y=250)

    b1=Button(pro,text='delete record',width=13,command=pro_delete)
    b1.place(x=190,y=290)

    b1=Button(pro,text='update record',width=13,command=pro_update)
    b1.place(x=70,y=290)
    
    
    

    

    
    
    
    
    
    
    


  #=============================================================== 
    # SERVICE TYPE
def pj():
    pjk=Toplevel()

    def reset():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
       
    def st_add():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=int(e4.get())
        cur=db.cursor()
        query="insert into service_type_details values('%s','%s','%s',%d)"%(a1,a2,a3,a4)
        cur.execute(query)
        db.commit()
        db.close() 

    def st_update():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        cur=db.cursor()
        query= " update service_type_details set ProductID ='%s', ServiceCharges =%d where ServiceId='%s'"%(a3,a4,a1) 
        cur.execute(query)
        db.commit()
        db.close() 


    def st_delete():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        cur=db.cursor()
        query="delete from service_type_details where ServiceId=('%s')"%(a1)
        cur.execute(query)
        db.commit()
        db.close()

    

  
    pjk.geometry('390x450')
    l1=Label(pjk,text='Service ID')
    l1.place(x=20,y=90)
    pjk.config(bg='GreenYellow')
    
    e1=Entry(pjk,width=30)
    e1.place(x=150,y=90)
    
    l2=Label(pjk,text='Product ID')
    l2.place(x=20,y=140)
    
    e2=Entry(pjk,width=30)
    e2.place(x=150,y=140)
    
    l3=Label(pjk,text='Service Name')
    l3.place(x=20,y=190)
    
    e3=Entry(pjk,width=30)
    e3.place(x=150,y=190)
    
    l4=Label(pjk,text='Charges')
    l4.place(x=20,y=240)
    
    e4=Entry(pjk,width=30)
    e4.place(x=150,y=240)
    
    b1=Button(pjk,text='Add',width=13,command=st_add)
    b1.place(x=70,y=300)
    
    b1=Button(pjk,text='Reset',width=13,command=reset)
    b1.place(x=190,y=300)

    b1=Button(pjk,text='delete',width=13,command=st_delete)
    b1.place(x=190,y=360)

    b1=Button(pjk,text='Update',width=13,command=st_update)
    b1.place(x=70,y=360)
    
 #=============================================================   
   # STAFF
def serv():
    
    ser=Toplevel()

    def reset():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        

    def cc_add():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        cur=db.cursor()
        query="insert into call_center_details values('%s','%s','%s','%s')"%(a1,a2,a3,a4)
        cur.execute(query)
        db.commit()
        db.close() 

    def cc_update():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        cur=db.cursor()
        query= "update call_center_details set call_center_name='%s', call_center_add='%s', call_center_phone='%s' where call_center_ID='%s'" %(a2,a3,a4,a1)
        cur.execute(query)
        db.commit()
        db.close() 


    def cc_delete():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        cur=db.cursor()
        query="delete from call_center_details where call_center_ID=('%s')"%(a1)
        cur.execute(query)
        db.commit()
        db.close()



    
    ser.geometry('390x450')
    l1=Label(ser,text='Staff ID')
    l1.place(x=20,y=90)
    ser.config(bg='DarkSalmon')
    
    e1=Entry(ser,width=30)
    e1.place(x=150,y=90)
    
    l2=Label(ser,text='Name')
    l2.place(x=20,y=140)
    
    e2=Entry(ser,width=30)
    e2.place(x=150,y=140)
    
    l3=Label(ser,text='Address')
    l3.place(x=20,y=190)
    
    e3=Entry(ser,width=30)
    e3.place(x=150,y=190)
    
    l3=Label(ser,text='Phone')
    l3.place(x=20,y=250)
    
    e4=Entry(ser,width=30)
    e4.place(x=150,y=250)
    
    b1=Button(ser,text='Add',width=13,command=cc_add)
    b1.place(x=70,y=310)
    
    b1=Button(ser,text='Reset',width=13,command=reset)
    b1.place(x=190,y=310)

    b1=Button(ser,text='delete',width=13,command=cc_delete)
    b1.place(x=190,y=360)

    b1=Button(ser,text='Update',width=13,command=cc_update)
    b1.place(x=70,y=360)

    
    
    
#=================================================================    
    # ENGINEERS
def se():
    
    ser=Toplevel()

    def reset():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        


    def eng_add():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        a5=e5.get()
        cur=db.cursor()
        query="insert into engineer_details values('%s','%s','%s','%s','%s')"%(a1,a2,a3,a4,a5)
        cur.execute(query)
        db.commit()
        db.close() 

    def eng_update():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        a5=e5.get()
        cur=db.cursor()
        query= "update engineer_details set engineer_name='%s', engineer_add='%s', engineer_phone='%s', engineer_city='%s' where engineer_ID='%s'" %(a2,a3,a4,a5,a1)
        cur.execute(query)
        db.commit()
        db.close() 


    def eng_delete():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        cur=db.cursor()
        query="delete from engineer_details where engineer_ID=('%s')"%(a1)
        cur.execute(query)
        db.commit()
        db.close()
    
    
    ser.geometry('390x450')
    l1=Label(ser,text='Engineer ID')
    l1.place(x=20,y=90)
    ser.config(bg='coral')
    
    e1=Entry(ser,width=30)
    e1.place(x=150,y=90)
    
    l2=Label(ser,text='Name')
    l2.place(x=20,y=140)
    
    e2=Entry(ser,width=30)
    e2.place(x=150,y=140)
    
    l3=Label(ser,text='Address')
    l3.place(x=20,y=190)
    
    e3=Entry(ser,width=30)
    e3.place(x=150,y=190)
    
    l4=Label(ser,text='Phone')
    l4.place(x=20,y=240)
    
    e4=Entry(ser,width=30)
    e4.place(x=150,y=240)
    
    l5=Label(ser,text='City')
    l5.place(x=20,y=290)
    
    e5=Entry(ser,width=30)
    e5.place(x=150,y=290)
    
    b1=Button(ser,text='Add',width=13,command=eng_add)
    b1.place(x=70,y=330)
    
    b1=Button(ser,text='Reset',width=13,command=reset)
    b1.place(x=190,y=330)

    b1=Button(ser,text='delete',width=13,command=eng_delete)
    b1.place(x=190,y=380)

    b1=Button(ser,text='Update',width=13,command=eng_update)
    b1.place(x=70,y=380)
    
 #========================================================   
 # CUSTOMERS
def re():
    er=Toplevel()

    def reset():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        
    def custo_add():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        a5=e5.get()
        cur=db.cursor()
        query="insert into customer_details values('%s','%s','%s','%s','%s')"%(a1,a2,a3,a4,a5)
        cur.execute(query)
        db.commit()
        db.close() 

    def custo_update():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        a5=e5.get()
        cur=db.cursor()
        query= "update customer_details set customer_name='%s', customer_add='%s', customer_phone='%s', customer_city='%s' where customer_ID='%s'" %(a2,a3,a4,a5,a1)
        cur.execute(query)
        db.commit()
        db.close() 


    def custo_delete():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        cur=db.cursor()
        query="delete from customer_details where customer_ID=('%s')"%(a1)
        cur.execute(query)
        db.commit()
        db.close()
    
    er.geometry('390x450')
    l1=Label(er,text='customer ID')
    l1.place(x=20,y=90)
    er.config(bg='DodgerBlue')
    
    e1=Entry(er,width=30)
    e1.place(x=150,y=90)
    
    l2=Label(er,text='Name')
    l2.place(x=20,y=140)
    
    e2=Entry(er,width=30)
    e2.place(x=150,y=140)
    
    l3=Label(er,text='Address')
    l3.place(x=20,y=190)
    
    e3=Entry(er,width=30)
    e3.place(x=150,y=190)
    
    l4=Label(er,text='Phone')
    l4.place(x=20,y=240)
    
    e4=Entry(er,width=30)
    e4.place(x=150,y=240)
    
    l5=Label(er,text='City')
    l5.place(x=20,y=290)
    
    e5=Entry(er,width=30)
    e5.place(x=150,y=290)
    
    b1=Button(er,text='Add',width=13,command=custo_add)
    b1.place(x=70,y=330)
    
    b1=Button(er,text='Reset',width=13,command=reset)
    b1.place(x=190,y=330)

    b1=Button(er,text='delete',width=13,command=custo_delete)
    b1.place(x=190,y=380)

    b1=Button(er,text='Update',width=13,command=custo_update)
    b1.place(x=70,y=380)

#=========================================================
#calldata

def ca():
    r=Toplevel()

    def reset():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        

    def calldata_add():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        a5=e5.get()
        a6=int(e6.get())
        cur=db.cursor()
        query="insert into calldata_details values('%s','%s','%s','%s','%s',%d)"%(a1,a2,a3,a4,a5,a6)
        cur.execute(query)
        db.commit()
        db.close()

    def calldata_update():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        a5=e5.get()
        a6=e6.get()
        cur=db.cursor()
        query="update calldata_details set assign_date='%s', total_amount=%d where calldata_ID='%s'"%(a5,a6,a1)
        cur.execute(query)
        db.commit()
        db.close() 
 

    def calldata_delete():
        db= pymysql.connect(host="localhost", user="root", password="root", database="minor",port=3306)
        a1=e1.get()
        cur=db.cursor()
        query="delete from calldata_details where call_ID=('%s')"%(a1)
        cur.execute(query)
        db.commit()
        db.close()
    
    r.geometry('390x450')
    r.config(bg='gray')

    l1=Label(r,text='call ID')
    l1.place(x=20,y=90)

   
    e1=Entry(r,width=30)
    e1.place(x=150,y=90)
    
    l2=Label(r,text='product ID')
    l2.place(x=20,y=140)
    
    e2=Entry(r,width=30)
    e2.place(x=150,y=140)
    
    l3=Label(r,text='service ID')
    l3.place(x=20,y=190)
    
    e3=Entry(r,width=30)
    e3.place(x=150,y=190)
    
    l4=Label(r,text='engineer ID')
    l4.place(x=20,y=240)
    
    e4=Entry(r,width=30)
    e4.place(x=150,y=240)
    
    l5=Label(r,text='assign date')
    l5.place(x=20,y=290)
    
    e5=Entry(r,width=30)
    e5.place(x=150,y=290)

    l6=Label(r,text='Amount')
    l6.place(x=20,y=340)
    
    e6=Entry(r,width=30)
    e6.place(x=150,y=340)
    
    b1=Button(r,text='Add',width=13,command=calldata_add)
    b1.place(x=70,y=390)
    
    b1=Button(r,text='Reset',width=13,command=reset)
    b1.place(x=190,y=390)

    b1=Button(r,text='delete',width=13,command=calldata_delete)
    b1.place(x=190,y=440)

    b1=Button(r,text='update',width=13,command=calldata_update)
    b1.place(x=70,y=440)


    
#==========================================
title1=Label(t, text="SERVICE CENTER MANAGEMENT", font=("times new roman", 40, "bold"), fg="white",bg="black", bd=8, relief=RAISED).pack(side=TOP, fill=X)        
title2=Label(t, text="MANAGE SERVICES", font=("times new roman", 20, "bold"), fg="white",bg="black", bd=8, relief=RAISED).place(x=30,y=90)



b1=Button(t,text='Service Center',width=23,font=('arial',15, 'bold'),bg='orange',command=wid1)
b1.place(x=25,y=150)

b1=Button(t,text='Products ',width=23,font=('arial',15,'bold'),bg='sandy brown',command=pr)
b1.place(x=25,y=220)

b1=Button(t,text='Service Type ',width=23,font=('arial',15,'bold'),bg='violet',command=pj)
b1.place(x=25,y=300)

b1=Button(t,text='Staff ',width=23,font=('arial',15,'bold'),bg='salmon',command=serv)
b1.place(x=25,y=390)

b1=Button(t,text='Engineers',width=23,font=('arial',15,'bold'),bg='teal',command=se)
b1.place(x=25,y=480)

b1=Button(t,text='Customers ',width=23,font=('arial',15,'bold'),bg='pink',command=re)
b1.place(x=25,y=570)

b4=Button(t,text='Call Data',width=23,font=('arial',15,'bold'),bg='yellowgreen',command=ca)
b4.place(x=25,y=650)

t.mainloop()

