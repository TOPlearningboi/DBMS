import mysql.connector as sql
from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime
from PIL import ImageTk, Image
import win32api
import os
os.chdir("C://Users/HP/Desktop")

a=[]
b=0
c=0
o=0
con = sql.connect(host='localhost',user='root',password='12345',database='hotel')
cur=con.cursor()
cur.execute("SELECT * FROM employee")
for x in cur:   
    a.append(str(x))
def AddCustomer():
    global MobileE
    global AddCustomer_Window
    AddCustomer_Window=Toplevel()
    AddCustomer_Window.grab_set()
    imag = Image.open('hotel.png')
    a = ImageTk.PhotoImage(imag)       
    labe=Label(AddCustomer_Window,imag = a)
    labe.place(x=0,y=0)
          
    AddCustomer_Window.title("New Customer")
    AddCustomer_Window.geometry("1366x768")  
    
    HeadF=Label(AddCustomer_Window,text="Customers DETAILS",font=("Helvetica",10))
    HeadF.place(anchor=CENTER,relx=0.5,rely=0.1)

    
    NameF=Label(AddCustomer_Window,text="First Name:",font=("Helvetica",10))
    NameF.place(anchor=CENTER,relx=0.1,rely=0.22)
    NameFE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    NameFE.place(relx=0.29,rely=0.22,anchor=CENTER)
    NameFEV=NameFE.get()
    
    NameL=Label(AddCustomer_Window,text="Last Name:",font=("Helvetica",10))
    NameL.place(anchor=CENTER,relx=0.6,rely=0.22)
    NameLE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    NameLE.place(relx=0.79,rely=0.22,anchor=CENTER)
 
    
    City=Label(AddCustomer_Window,text="City:",font=("Helvetica",10))
    City.place(anchor=CENTER,relx=0.1,rely=0.37)
    CityE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    CityE.place(relx=0.29,rely=0.37,anchor=CENTER)
    CityEV=CityE.get()
   
    Mobile=Label(AddCustomer_Window,text="Mobile No.:",font=("Helvetica",10))
    Mobile.place(anchor=CENTER,relx=0.6,rely=0.37)
    MobileE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    MobileE.place(relx=0.79,rely=0.37,anchor=CENTER)
    Mob=MobileE.get()

    Chekin=Label(AddCustomer_Window,text="Check-in Date:",font=("Helvetica",10))
    Chekin.place(anchor=CENTER,relx=0.1,rely=0.52)
    ChekinE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    ChekinE.place(relx=0.29,rely=0.52,anchor=CENTER)
    ChekinEV=ChekinE.get()

    Chekout=Label(AddCustomer_Window,text="Check-Out Date:",font=("Helvetica",10))
    Chekout.place(anchor=CENTER,relx=0.6,rely=0.52)
    ChekoutE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    ChekoutE.place(relx=0.79,rely=0.52,anchor=CENTER)
    ChekoutEV=ChekoutE.get()

    Nop=Label(AddCustomer_Window,text="Number of People:",font=("Helvetica",10))
    Nop.place(anchor=CENTER,relx=0.1,rely=0.67)
    NopE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    NopE.place(relx=0.29,rely=0.67,anchor=CENTER)
    NumP=NopE.get()

    NoBR=Label(AddCustomer_Window,text="Basic Room:",font=("Helvetica",10))
    NoBR.place(anchor=CENTER,relx=0.6,rely=0.67)
    NoBRE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    NoBRE.place(relx=0.79,rely=0.67,anchor=CENTER)
    NoBREV=NoBRE.get()

    NoPR=Label(AddCustomer_Window,text="Premium Room:",font=("Helvetica",10))
    NoPR.place(anchor=CENTER,relx=0.1,rely=0.82)
    NoPRE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    NoPRE.place(relx=0.29,rely=0.82,anchor=CENTER)
    NoPREV=NoPRE.get()

    NoSR=Label(AddCustomer_Window,text="Suite:",font=("Helvetica",10))
    NoSR.place(anchor=CENTER,relx=0.6,rely=0.82)
    NoSRE=Entry(AddCustomer_Window,width=20,font=("Helvetica",10))
    NoSRE.place(relx=0.79,rely=0.82,anchor=CENTER)
    NoSREV=NoSRE.get()
    
    
    Submit=Button(AddCustomer_Window,text="Submit",command=lambda: submitD(NameFE.get(),NameLE.get(),CityE.get(),MobileE.get(),ChekinE.get(),ChekoutE.get(),NopE.get(),NoBRE.get(),NoPRE.get(),NoSRE.get()))
    Submit.place(relx=0.47,rely=0.95,anchor=CENTER)
    BackAd=Button(AddCustomer_Window,text="Back",command=destroyAdd)
    BackAd.place(relx=0.05,rely=0.05,anchor=CENTER)
def destroyAdd():
     AddCustomer_Window.destroy()
     

def submitD(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj):
    
       global fuji
       global delta
       cur.execute("Select * from Customers;")
       alooee=cur.fetchall()
       efcegee=0
      
       
       if len(MobileE.get()) == 10:
        for idgee in alooee:
          if idgee[3]==dd:
              
              efcegee=1
              
        if dd.isdigit()==True and gg.isdigit()==True and hh.isdigit()==True and ii.isdigit()==True and jj.isdigit()==True and aa!="" and bb!="" and cc!="" and dd!="" and ee!="" and ff!="" and gg!="" and hh!="" and ii!="" and jj!="" and efcegee==0:
           qwerty=int(hh)+int(ii)+int(jj)
           qwerty1=qwerty*4
           ggqwerty=int(gg)
           if ggqwerty <= qwerty1 and qwerty>0:
               
            try:    
             current_time = datetime.now()
             date_format = "%m/%d/%Y"
             adate = datetime.strptime(ee, date_format)
             bdate = datetime.strptime(ff, date_format)
             eedate=ee.split("/")
             eeday2=eedate[1]
             eemonth2=eedate[0]
             eeyear2=eedate[2]
             eeday=int(eeday2)
             eemonth=int(eemonth2)
             eeyear=int(eeyear2)
             iamdone=int(current_time.year)
             iamdone2=int(current_time.month)
             iamdone3=int(current_time.day)
             if eeyear<iamdone:
                 raise TypeError("Nice")
             if eeyear== iamdone:
                 if eemonth<iamdone2:
                     raise TypeError("Nice")
                 elif eemonth==iamdone2:
                     if eeday<iamdone3:
                         raise TypeError("Nice")
             ffdate=ff.split("/")
             ffday2=ffdate[1]
             ffmonth2=ffdate[0]
             ffyear2=ffdate[2]
             ffday=int(ffday2)
             ffmonth=int(ffmonth2)
             ffyear=int(ffyear2)
             if ffyear<eeyear:
                 raise TypeError("Nice")
             if ffyear== eeyear:
                 if ffmonth<eemonth:
                     raise TypeError("Nice")
                 elif ffmonth==eemonth:
                     if ffday<=eeday:
                         raise TypeError("Nice")
             delta = bdate - adate
             deltas=str(delta)

                 
             cur.execute("Insert into Customers values('"+aa+"','"+bb+"','"+cc+"','"+dd+"','"+ee+"','"+ff+"','"+gg+"','"+hh+"','"+ii+"','"+jj+"')")
             hhint=int(hh)
             iito=int(ii)
             jjint=int(jj)
             GH=hhint*3000+jjint*10000+iito*30000
           
             
             deltasuper=deltas.strip()
             deltasupermax=deltasuper[0]
             deltasupermaxultra=int(deltasupermax)
             fuji=deltasupermaxultra*GH
             HG=str(fuji)
             cur.execute("Insert into pricing values('"+dd+"','"+HG+"','0')")
             con.commit()

             messagebox.showinfo("Success","Data Succesfully Submitted")
             AddCustomer_Window.destroy()
            except:
               messagebox.showerror("Error","Invalid Date") 
           elif qwerty==0:
               messagebox.showerror("Error","No Rooms Selected.")   
           else:
               messagebox.showerror("Error","Excess Number Of People!")   
        elif efcegee==1:
           messagebox.showerror("Error","Mobile Number already Entered.Please Verify then try again.")
        else:
           messagebox.showerror("Error","Invalid Entries.Please Verify then try again.")
           
       else:
         messagebox.showerror("Error","Invalid Mobile Number")     


def IDCheck():
    global o
    global enter
    l=0

    global b
    
    for y in a:
     if y=="('"+ID.get()+"', '"+Pass.get()+"')":
      messagebox.showinfo("Success","Hello "+ID.get()+". Welcome Back")

      l=1
      root.destroy()
      MainWindow()
      break    
    if l!=1:
      b+=1
      messagebox.showerror("Error","Wrong ID or Password Entered.Try Again.")
      
    if b==5:
        messagebox.showwarning("Warning","You have entered wrong credentials for 5 times.Please Wait for 5 minutes before trying again.")
        enter.destroy()
        enter2=Button(root,text="Enter",state=DISABLED)
        enter2.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        time.sleep(300)
        enter2.destroy()
        enter=Button(root,text="Enter",command=IDCheck)
        enter.place(relx=0.5,rely=0.5,anchor=CENTER)
          


def IDCheck2():

    global o
    global enter
    l=0

    global b

    for y in a:
     if y=="('"+ID.get()+"', '"+Pass.get()+"')":
      messagebox.showinfo("Success","Hello "+ID.get()+". Welcome Back")

      l=1
      
      root.destroy()
      MainWindow()
      break    
    if l!=1:
      b+=1
      messagebox.showerror("Error","Wrong ID or Password Entered.Try Again.")
      
    if b==5:
        messagebox.showwarning("Warning","You have entered wrong credentials for 5 times.Please Wait for 5 minutes before trying again.")
        enter.destroy()
        enter2=Button(root,text="Enter",state=DISABLED)
        enter2.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        time.sleep(300)
        enter2.destroy()
        enter=Button(root,text="Enter",command=IDCheck)
        enter.place(relx=0.5,rely=0.5,anchor=CENTER)
            
#LOGIN PAGE ELEMENTS
def LoginPage():
 global  ID
 global Pass
 global root
 global enter
 root = Tk()
 imag = Image.open('image (2).png')

 a = ImageTk.PhotoImage(imag)
 label=Label(root,imag = a)
 label.place(x=0,y=1)
 root.geometry("1366x768")
 root.title("Login Page")
 Login=Label(root,text="LOGIN",font=("Helvetica",30))
 Login.place(anchor=CENTER,relx=0.5,rely=0.36)

 IDName=Label(root,text="ID:",font=("Helvetica",15))
 IDName.place(anchor=CENTER,relx=0.364,rely=0.47)

 PassName=Label(root,text="Password:",font=("Helvetica",15))
 PassName.place(anchor=CENTER,relx=0.34,rely=0.51)

 ID=Entry(root,width=30,font=("Helvetica",15))
 ID.place(relx=0.5,rely=0.47,anchor=CENTER)

 Pass=Entry(root,width=30,font=("Helvetica",15))
 Pass.place(relx=0.5,rely=0.51,anchor=CENTER)

 enter=Button(root,text="Enter",command=IDCheck)
 enter.place(relx=0.5,rely=0.6,anchor=CENTER)
 root.mainloop()
 
def LoginPage2():
 global root2
 root2.destroy()
 global  ID
 global Pass
 global root
 global enter
 root = Tk()
 imag = Image.open('image (2).png')

 a = ImageTk.PhotoImage(imag)
 label=Label(root,imag = a)
 label.place(x=0,y=1)
 root.geometry("1366x768")
 root.title("Login Page")
 Login=Label(root,text="LOGIN",font=("Helvetica",30))
 Login.place(anchor=CENTER,relx=0.5,rely=0.36)

 IDName=Label(root,text="ID:",font=("Helvetica",15))
 IDName.place(anchor=CENTER,relx=0.364,rely=0.47)

 PassName=Label(root,text="Password:",font=("Helvetica",15))
 PassName.place(anchor=CENTER,relx=0.34,rely=0.51)

 ID=Entry(root,width=30,font=("Helvetica",15))
 ID.place(relx=0.5,rely=0.47,anchor=CENTER)

 Pass=Entry(root,width=30,font=("Helvetica",15))
 Pass.place(relx=0.5,rely=0.51,anchor=CENTER)

 enter=Button(root,text="Enter",command=IDCheck)
 enter.place(relx=0.5,rely=0.6,anchor=CENTER)
 root.mainloop()


##Main window
def MainWindow():
    global root2
    global NewC
    global Exc
    global Service
    global LvC
    global Sgnout
    
    
    root2 = Tk()
    imag = Image.open('image (2).png')

    a = ImageTk.PhotoImage(imag)
    label=Label(root2,imag = a)
    label.place(x=0,y=0)
    root2.geometry("1366x768")
    root2.title("Main Page")
    
    NewC=Button(root2,text="New Customers",command=AddCustomer,width=30)
    NewC.place(relx=0.5,rely=0.45,anchor=CENTER)
    Exc=Button(root2,text="Existing Customers",command=EXCD,width=30)
    Exc.place(relx=0.5,rely=0.5,anchor=CENTER)
    Service=Button(root2,text="Services",command=Services,width=30)
    Service.place(relx=0.5,rely=0.55,anchor=CENTER)
    LvC=Button(root2,text="Customers Checking-Out",command=LeavingC,width=30)
    LvC.place(relx=0.5,rely=0.6,anchor=CENTER)
    Sgnout=Button(root2,text="Sign Out",command=LoginPage2,width=30)
    Sgnout.place(relx=0.5,rely=0.65,anchor=CENTER)
    root2.mainloop()


def LeavingC():
    global AddCustomer_Window2
    global MobLE
    AddCustomer_Window2=Toplevel()
    AddCustomer_Window2.grab_set()
    AddCustomer_Window2.geometry("1366x768")
    AddCustomer_Window2.title("Customer Checking-Out")
    imag = Image.open('hotel.png')

    a = ImageTk.PhotoImage(imag)
    labe=Label(AddCustomer_Window2,imag = a)
    labe.place(x=0,y=0)
    
    HeadL=Label(AddCustomer_Window2,text="Customers Checking-Out",font=("Helvetica",18))
    HeadL.place(anchor=CENTER,relx=0.5,rely=0.1)

    
    MobL=Label(AddCustomer_Window2,text="Mobile No.:",font=("Helvetica",12))
    MobL.place(anchor=CENTER,relx=0.2,rely=0.22)
    MobLE=Entry(AddCustomer_Window2,width=20,font=("Helvetica",12))
    MobLE.place(relx=0.5,rely=0.22,anchor=CENTER)
    
    SearchL=Button(AddCustomer_Window2,text="Search",command=LeavingS)
    SearchL.place(relx=0.75,rely=0.22,anchor=CENTER)
    BackAd2=Button(AddCustomer_Window2,text="Back",command=destroyAdd2)
    BackAd2.place(relx=0.05,rely=0.05,anchor=CENTER)
def destroyAdd2():
     AddCustomer_Window2.destroy()

def LeavingS():
    global luvul1
    global luvul
    cur.execute("Select * from Customers;")
    bhind=cur.fetchall()
    saboo=0
    for sabi in bhind:
       if sabi[3]==MobLE.get():
           saboo=1
           luvul1=sabi[3]
           luvul=sabi[0]
    cur.execute("Select * from pricing;")
    bhindi=cur.fetchall()
    try:
     for sabir in bhindi:
           if sabir[0]==luvul1:
               deji=sabir[1]
               duji=sabir[2]
               deji1=int(deji)
               duji1=int(duji)
 
     if saboo==1:
         
         quqqqq=1.18*deji1
         quqqqx=quqqqq+duji1
         Chabi=Label(AddCustomer_Window2,text="Name:",font=("Helvetica",14))
         Chabi.place(anchor=CENTER,relx=0.35,rely=0.4)
         Chaboo=Label(AddCustomer_Window2,text=luvul,font=("Helvetica",14))
         Chaboo.place(anchor=CENTER,relx=0.65,rely=0.4)
         Chabi1=Label(AddCustomer_Window2,text="Room Charge:",font=("Helvetica",14))
         Chabi1.place(anchor=CENTER,relx=0.35,rely=0.45)
         Chaboo1=Label(AddCustomer_Window2,text=deji1,font=("Helvetica",14))
         Chaboo1.place(anchor=CENTER,relx=0.65,rely=0.45)
         Chabi2=Label(AddCustomer_Window2,text="Service Charge:",font=("Helvetica",14))
         Chabi2.place(anchor=CENTER,relx=0.35,rely=0.5)
         Chaboo2=Label(AddCustomer_Window2,text=duji1,font=("Helvetica",14))
         Chaboo2.place(anchor=CENTER,relx=0.65,rely=0.5)
         Chabi=Label(AddCustomer_Window2,text="GST:",font=("Helvetica",14))
         Chabi.place(anchor=CENTER,relx=0.35,rely=0.55)
         Chaboo=Label(AddCustomer_Window2,text=deji1*0.18,font=("Helvetica",14))
         Chaboo.place(anchor=CENTER,relx=0.65,rely=0.55)
         Chabi=Label(AddCustomer_Window2,text="Total Amount:",font=("Helvetica",14))
         Chabi.place(anchor=CENTER,relx=0.35,rely=0.6)
         Chaboo=Label(AddCustomer_Window2,text=quqqqx,font=("Helvetica",14))
         Chaboo.place(anchor=CENTER,relx=0.65,rely=0.6)
         Deleto=Button(AddCustomer_Window2,text="Check-Out",command=Deletey)
         Deleto.place(relx=0.58,rely=0.8,anchor=CENTER)
         Printu=Button(AddCustomer_Window2,text="Print Bill",command=Printy)
         Printu.place(relx=0.4,rely=0.8,anchor=CENTER)
         
         sleepe=str(deji)
         sleepe1=str(sleepe)
        
         myfile1=str(deji1)
         myfile2=str(duji1)
         myfile3=str(sleepe1)
         myfile4=str(quqqqx)
         
         myfile=open("CT.txt","w+")
         myfile.write("     Hotel Sunshine \n")
         myfile.write("\n")
         myfile.write("\n")
         myfile.write("          BILL\n")
         myfile.write("\n")
         myfile.write("Name:              "+luvul+"\n")
         myfile.write("Room Charges:      "+myfile1+"\n")
         myfile.write("Service Charge:    "+myfile2+"\n")
         myfile.write("GST:               "+myfile3+"\n")
         myfile.write("Total Amount:      "+myfile4+"\n")
         myfile.write("\n")
         myfile.write("Come Again Soon "+luvul+"!!!\n")
         
         myfile.flush()
         myfile.close()
         
     else:
       messagebox.showwarning("Error","There is No Customers registered with this Mobile No.")
    except:
         messagebox.showerror("Error","No Customer Found")


def Printy():
    Printyyy="C:/Users/HP/Desktop/CT.txt"
    win32api.ShellExecute(0, "print",Printyyy, None, ".", 0)
def EXCD():
    global AddCustomer_Window3
    cur.execute("Select * from Customers;")
    oloo=cur.fetchall()
    AddCustomer_Window3=Toplevel()
    AddCustomer_Window3.grab_set()
    AddCustomer_Window3.geometry("1366x768")
    AddCustomer_Window3.title("Existing Customerss")
    
    HeadLx=Label(AddCustomer_Window3,text="Existing Customerss",font=("Helvetica",20))
    HeadLx.place(anchor=CENTER,relx=0.5,rely=0.1)
    
    
    NAMEEXC=Label(AddCustomer_Window3,text="First Name",font=("Helvetica",13))
    NAMEEXC.place(anchor=CENTER,relx=0.07,rely=0.2)
    NAMELEXC=Label(AddCustomer_Window3,text="Last Name",font=("Helvetica",13))
    NAMELEXC.place(anchor=CENTER,relx=0.17,rely=0.2)
    CITYEXC=Label(AddCustomer_Window3,text="City",font=("Helvetica",13))
    CITYEXC.place(anchor=CENTER,relx=0.27,rely=0.2)
    MOBILEEXC=Label(AddCustomer_Window3,text="Mobile",font=("Helvetica",13))
    MOBILEEXC.place(anchor=CENTER,relx=0.37,rely=0.2)
    CHECKIN=Label(AddCustomer_Window3,text="Check-In",font=("Helvetica",13))
    CHECKIN.place(anchor=CENTER,relx=0.47,rely=0.2)
    CHECKOUT=Label(AddCustomer_Window3,text="Check-Out",font=("Helvetica",13))
    CHECKOUT.place(anchor=CENTER,relx=0.57,rely=0.2)
    NUMBPE=Label(AddCustomer_Window3,text="No. of People",font=("Helvetica",13))
    NUMBPE.place(anchor=CENTER,relx=0.67,rely=0.2)
    NUMBBR=Label(AddCustomer_Window3,text="Basic Rooms",font=("Helvetica",13))
    NUMBBR.place(anchor=CENTER,relx=0.77,rely=0.2)
    NUMBPR=Label(AddCustomer_Window3,text="Premium Rooms",font=("Helvetica",13))
    NUMBPR.place(anchor=CENTER,relx=0.87,rely=0.2)
    NUMBSR=Label(AddCustomer_Window3,text="Suites",font=("Helvetica",13))
    NUMBSR.place(anchor=CENTER,relx=0.97,rely=0.2)
    xyx=0
    for iyi in range(100):
     LINE=Label(AddCustomer_Window3,text="-")
     LINE.place(anchor=CENTER,relx=xyx,rely=0.225)
     xyx+=0.01
    yyyy=0.25
    
    for lll in oloo:
        xxxx=0.07
        for i in range(10):
        
         DATA=Label(AddCustomer_Window3,text=lll[i],font=("Helvetica",10))
         DATA.place(anchor=CENTER,relx=xxxx,rely=yyyy)
         xxxx+=0.1
        yyyy+=0.05
    BackAd3=Button(AddCustomer_Window3,text="Back",command=destroyAdd3)
    BackAd3.place(relx=0.04,rely=0.04,anchor=CENTER)
def destroyAdd3():
         AddCustomer_Window3.destroy()
def Services():
    global MobLESer
    global AddCustomer_Window4
    AddCustomer_Window4=Toplevel()
    AddCustomer_Window4.grab_set()
    AddCustomer_Window4.geometry("1366x768")
    AddCustomer_Window4.title("Services")
    imag = Image.open('hotel.png')

    a = ImageTk.PhotoImage(imag)
    labe=Label(AddCustomer_Window4, imag = a)
    labe.place(x=0,y=0) 
    
    ServX=Label(AddCustomer_Window4,text="Services",font=("Helvetica",20))
    ServX.place(anchor=CENTER,relx=0.5,rely=0.1)
    
    MobLSer=Label(AddCustomer_Window4,text="Mobile No.:",font=("Helvetica",10))
    MobLSer.place(anchor=CENTER,relx=0.1,rely=0.22)
    MobLESer=Entry(AddCustomer_Window4,width=20,font=("Helvetica",10))
    MobLESer.place(relx=0.29,rely=0.22,anchor=CENTER)
    SearchLSer=Button(AddCustomer_Window4,text="Search",command=ServicesS)
    SearchLSer.place(relx=0.5,rely=0.22,anchor=CENTER)
    BackAd4=Button(AddCustomer_Window4,text="Back",command=destroyAdd4)
    BackAd4.place(relx=0.05,rely=0.05,anchor=CENTER)
def destroyAdd4():
     AddCustomer_Window4.destroy()

def ServicesS():
    global zyz
    global LaundryE
    global FoodsE
    cur.execute("Select * from Customers;")
    aloo=cur.fetchall()
    efceg=0
    for idg in aloo:
       if idg[3]==MobLESer.get():
           zyz=MobLESer.get()
           efceg=1
           qq=idg[0]
    if efceg==1:
        NameSer=Label(AddCustomer_Window4,text="Name:",font=("Helvetica",10))
        NameSer.place(anchor=CENTER,relx=0.1,rely=0.3)
        ANameSer=Label(AddCustomer_Window4,text=qq,font=("Helvetica",10))
        ANameSer.place(anchor=CENTER,relx=0.29,rely=0.3)
        
        Foods=Label(AddCustomer_Window4,text="Food Cost:",font=("Helvetica",10))
        Foods.place(anchor=CENTER,relx=0.1,rely=0.4)
        FoodsE=Entry(AddCustomer_Window4,width=20,font=("Helvetica",10))
        FoodsE.place(relx=0.29,rely=0.4,anchor=CENTER)
        Menus=Button(AddCustomer_Window4,text="Menu",command=Menu)
        Menus.place(relx=0.5,rely=0.4,anchor=CENTER)
        
        Laundry=Label(AddCustomer_Window4,text="Laundry Cost:",font=("Helvetica",10))
        Laundry.place(anchor=CENTER,relx=0.1,rely=0.6)
        LaundryE=Entry(AddCustomer_Window4,width=20,font=("Helvetica",10))
        LaundryE.place(relx=0.29,rely=0.6,anchor=CENTER)
        LaundryP=Button(AddCustomer_Window4,text="Laundry Pricing",command=Lau)
        LaundryP.place(relx=0.5,rely=0.6,anchor=CENTER)
        
        SubmitSer=Button(AddCustomer_Window4,text="Submit",command=submitting)
        SubmitSer.place(relx=0.45,rely=0.8,anchor=CENTER)
    elif MobLESer.get()=="":
        messagebox.showwarning("Error","No Customers Mobile No. Entered")

    else:   
        messagebox.showwarning("Error","There is No Customers registered with this Mobile No.")


def Menu():
    global AddCustomer_Window6
    AddCustomer_Window6=Toplevel()
    AddCustomer_Window6.grab_set()
    AddCustomer_Window6.geometry("600x400")
    AddCustomer_Window6.title("Menu")
    cur.execute("Select * from menu;")
    yoyo=cur.fetchall()
    MenuX=Label(AddCustomer_Window6,text="Menu",font=("Helvetica",20))
    MenuX.place(anchor=CENTER,relx=0.5,rely=0.1)
    MenuItemName=Label(AddCustomer_Window6,text="Item Name",font=("Helvetica",15))
    MenuItemName.place(anchor=CENTER,relx=0.3,rely=0.21)
    MenuXPrice=Label(AddCustomer_Window6,text="Price",font=("Helvetica",15))
    MenuXPrice.place(anchor=CENTER,relx=0.7,rely=0.21)
    gfe=0
    for iyis in range(100):
     LINEpp=Label(AddCustomer_Window6,text="-")
     LINEpp.place(anchor=CENTER,relx=gfe,rely=0.16)
     gfe+=0.01
    xyxyx=0
    for iyis in range(100):
     LINElll=Label(AddCustomer_Window6,text="-")
     LINElll.place(anchor=CENTER,relx=xyxyx,rely=0.26)
     xyxyx+=0.01
    yyyygs=0.32
    
    for abcd in yoyo:
        xxxxgs=0.3
        for isk in range(2):
        
         DATA=Label(AddCustomer_Window6,text=abcd[isk],font=("Helvetica",10))
         DATA.place(anchor=CENTER,relx=xxxxgs,rely=yyyygs)
         xxxxgs+=0.4
        yyyygs+=0.07
    BackAd5=Button(AddCustomer_Window6,text="Back",command=destroyAdd5)
    BackAd5.place(relx=0.05,rely=0.05,anchor=CENTER)
def destroyAdd5():
         AddCustomer_Window6.destroy()
def Lau():
    global AddCustomer_Window7
    AddCustomer_Window7=Toplevel()
    AddCustomer_Window7.grab_set()
    AddCustomer_Window7.geometry("600x400")
    AddCustomer_Window7.title("Laundry")
    cur.execute("Select * from laundry;")
    Laundr=cur.fetchall()
    LaundrX=Label(AddCustomer_Window7,text="Laundry",font=("Helvetica",20))
    LaundrX.place(anchor=CENTER,relx=0.5,rely=0.1)
    LaundrXc=Label(AddCustomer_Window7,text="Item Name",font=("Helvetica",15))
    LaundrXc.place(anchor=CENTER,relx=0.3,rely=0.21)
    PriceXCL=Label(AddCustomer_Window7,text="Price",font=("Helvetica",15))
    PriceXCL.place(anchor=CENTER,relx=0.7,rely=0.21)
    gfess=0
    for iyisss in range(100):
     LINEss=Label(AddCustomer_Window7,text="-")
     LINEss.place(anchor=CENTER,relx=gfess,rely=0.16)
     gfess+=0.01
    xyxyxss=0
    for iyis in range(100):
     LINEsa=Label(AddCustomer_Window7,text="-")
     LINEsa.place(anchor=CENTER,relx=xyxyxss,rely=0.26)
     xyxyxss+=0.01
    yyyygsss=0.32
    
    for abcdss in Laundr:
        xxxxgsss=0.3
        for iskss in range(2):
        
         DATssA=Label(AddCustomer_Window7,text=abcdss[iskss],font=("Helvetica",10))
         DATssA.place(anchor=CENTER,relx=xxxxgsss,rely=yyyygsss)
         xxxxgsss+=0.4
        yyyygsss+=0.07
    BackAd6=Button(AddCustomer_Window7,text="Back",command=destroyAdd6)
    BackAd6.place(relx=0.05,rely=0.05,anchor=CENTER)
def destroyAdd6():
         AddCustomer_Window7.destroy()
def submitting():
    global xyq
    cur.execute("Select Services from pricing where Mobile="+zyz)
    qfq=cur.fetchall()
    fdsa=qfq[0]
    fdsapro=fdsa[0]
    fdsamax=int(fdsapro)
    if LaundryE.get().isdigit()==True and FoodsE.get().isdigit()==True:
       LaundrPricing=int(LaundryE.get())
       FoodPricin=int(FoodsE.get())
       xyq=FoodPricin+LaundrPricing+fdsamax
       xyqstr=str(xyq)
       zyzstr=str(zyz)
       cur.execute("UPDATE pricing SET services="+xyqstr+" WHERE Mobile="+zyzstr)
       con.commit()
       messagebox.showinfo("Success","Service Charges Successfully added.")
       AddCustomer_Window4.destroy()
    else:
        messagebox.showerror("Error","Invalid Entries.Please Verify then try again.")

def Deletey():
        response=messagebox.askyesno("Check-Out","Are you sure you want to Check-Out "+luvul+"?")
        Label(AddCustomer_Window2, text=response)
        if response==1:
           cur.execute("Delete from Customers where Mobile="+luvul1)
           con.commit()
           messagebox.showinfo("Success","Guest Checked Out.")
           AddCustomer_Window2.destroy()

LoginPage()
try:
 os.remove("CT.txt")
except:
  pass
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    

