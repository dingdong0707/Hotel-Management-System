from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib
from tkinter import Tk, Frame, Label, ttk, Button, messagebox, PhotoImage
from PIL import Image, ImageTk

#===============================importing from differet files =============================
from guest import guest_window
from reservation import reservation_window
from hotel_1 import Hotel_win
from service import Service_win
from feedback import Feedback
from staff import Staff
from room import room_window
from roomservice import roomservice_window
from myservice import myservice_window


def main():
       win=Tk()
       app=Login_win(win)
       win.mainloop()


class Login_win:
    def __init__(self,root):
        self.root=root
        self.root.title('Login')
        self.root.geometry('1550x800+0+0')
        # Specify the path to the image file
        image_path = "C:/Users/Asus/Downloads/Amaranta-Prambanan-Hotel-1024x684.jpg"

        # Load the image using Pillow
        img = Image.open(image_path)
        width=1550
        height= int(800*(width/img.width))
        img = img.resize((width, height))  # Resize the image to the window size

        self.bg_image = ImageTk.PhotoImage(img)

        #self.bg_image = PhotoImage(file=image_path)

        # Create a label to display the image
        bg_label = Label(self.root,image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        #frame = Frame(root)
        #frame.place(x=610, y=170, width=300, height=450)


        
        #frame = Frame(self.root, bg='white')
        #frame.place(x=610, y=170, width=340, height=450)

        get_str=Label(self.root,text='Dear Guest\nWelcome to our hotel',font=('times new roman',20,'italic'),fg='black', borderwidth=0, highlightthickness=0, relief='flat')
        get_str.place(x=550,y=170)

        #______________label________________________
        contactno=Label(self.root,text='Contact Number',font=('times new roman',15,'bold'),fg='black', borderwidth=0, highlightthickness=0, relief='flat')
        contactno.place(x=500,y=250)

        self.txtcontactno=ttk.Entry(self.root,font=('times new roman',15,'bold'))
        self.txtcontactno.place(x=500,y=275,width=200)
        password=Label(self.root,text='Password',font=('times new roman',15,'bold'),fg='black', borderwidth=0, highlightthickness=0, relief='flat')
        password.place(x=500,y=350)

        self.txtpass = ttk.Entry(self.root, show='*', font=('times new roman', 15, 'bold'))
        self.txtpass.place(x=500, y=375, width=200)
        #===================login button===============
        loginbtn=Button(self.root,command=self.login,text="Login",font=('times new roman',15,'bold'),bd=3,relief=RIDGE,fg='white',bg='blue')
        loginbtn.place(x=550,y=415,width=100,height=35)
        #=======================reg button=================
        regbtn=Button(self.root,text="New User Register",command=self.register_window,font=('times new roman',11,'bold'),bd=3,relief=RIDGE,fg='white',bg='black')
        regbtn.place(x=500,y=470,width=160)

    



    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


    # ...

    def login(self):
      if self.txtcontactno.get() == "" or self.txtpass.get() == "":
        messagebox.showerror('ERROR!', 'All data required')
      else:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port='3306',
                                       database='hotel management system')
        my_cursor = conn.cursor()
        entered_password = self.txtpass.get().strip()

        # Hash the entered password for comparison
        hashed_entered_password = hashlib.sha256(entered_password.encode('utf-8')).hexdigest()
        hashed_entered_password =hashed_entered_password[:55]

        # Print the hashed password for debugging
        print("Hashed Entered Password:", hashed_entered_password)

        # Execute the query
        my_cursor.execute('SELECT * FROM register WHERE contact=%s', (self.txtcontactno.get(),))

        # Fetch all rows
        rows = my_cursor.fetchall()
        print(rows)
        if not rows:
            messagebox.showerror('Error', 'Contact not found in the database')
        else:
            for row in rows:
                # Extract the hashed password from the database row
                hashed_db_password = row[3]  # Assuming password is stored in the fourth column (index 3)

                # Print the hashed password from the database for debugging
                print("Hashed Password from Database:", hashed_db_password)
                
                if hashed_entered_password == hashed_db_password:
                    open_main = messagebox.askyesno('YesNo', 'Access only admin')
                    if open_main > 0:
                        self.new_window = Toplevel(self.root)
                        self.app = HotelManagementSystem(self.new_window)
                    else:
                        if not open_main:
                            return
                else:
                    messagebox.showerror('Error', 'Invalid password')

        conn.commit()
        conn.close()

# ...

             
              
                   
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Register')
        self.root.geometry('1600x900+0+0')
        #====================Variables======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_password=StringVar()
        self.var_conpass=StringVar()
        self.var_check=IntVar()

        frame=Frame(self.root,bg='white')
        frame.place(x=520,y=100,width=880,height=550)

        reg_lbl=Label(frame,text="Register here",font=('times new roman',20,'bold'),fg='green')
        reg_lbl.place(x=20,y=20)
#=============================label & entry=========================


#===================================row1====================================
        fname=Label(frame,text="First Name",font=('times new roman',15,'bold'),bg='white',fg='blue')
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=('times new roman',15,'bold'))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=('times new roman',15,'bold'),bg='white',fg='blue')
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=('times new roman',15))
        self.txt_lname.place(x=370,y=130,width=250)

#=======================================row2==========================
        contact=Label(frame,text="Contact No",font=('times new roman',15,'bold'),bg='white',fg='blue')
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=('times new roman',15))
        self.txt_contact.place(x=50,y=200,width=250)

#+++++++++++++++++++password row3===================================

        password=Label(frame,text="Password",font=('times new roman',15,'bold'),bg='white',fg='blue')
        password.place(x=50,y=310)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=('times new roman',15))
        self.txt_password.place(x=50,y=340,width=250)

        con_pass=Label(frame,text="Confirm Password",font=('times new roman',15,'bold'),bg='white',fg='blue')
        con_pass.place(x=370,y=310)

        self.txt_con_pass=ttk.Entry(frame,textvariable=self.var_conpass,font=('times new roman',15))
        self.txt_con_pass.place(x=370,y=340,width=250)

#======================================check Button============================

        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree with the terms and conditions",font=('times new roman',15,'bold'),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        btn1=Button(frame,text="Register",command=self.register_data,font=('times new roman',15,'bold'),bd=3,relief=RIDGE,fg='white',bg='green')
        btn1.place(x=10,y=470,width=300) 

        btn2=Button(frame,text="Login Now",command=self.return_login,font=('times new roman',15,'bold'),bd=3,relief=RIDGE,fg='white',bg='green')
        btn2.place(x=330,y=470,width=300) 


#=================================FUNC DECL============================================
    def register_data(self):
           if self.var_fname.get()=='' or self.var_contact.get()=='':
                  messagebox.showerror("Error",'fill all the data')
           elif self.var_password.get()!=self.var_conpass.get():
                  messagebox.showerror('Error','Both Passwords must be same')
           elif self.var_check.get()==0:
                  messagebox.showerror('Error',"please agree to all the terms and condition")
           else: 
                  # Hash the password before storing it in the database
                  hashed_password = hashlib.sha256(self.var_password.get().encode('utf-8')).hexdigest()
                  conn=mysql.connector.connect(host='localhost',user='root',password='',port = '3306',database='hotel management system')
                  my_cursor=conn.cursor()
                  query=('select * from register where contact=%s')
                  value=(self.var_contact.get(),)
                  my_cursor.execute(query,value)
                  row=my_cursor.fetchone()
                  if row!=None:
                         messagebox.showerror('Error','user already exists')
                  else:  
                         

                         my_cursor.execute('INSERT INTO `register`(`fname`, `lname`, `contact`, `password`) VALUES (%s,%s,%s,%s)',(
                                                                                  self.var_fname.get(),
                                                                                  self.var_lname.get(),
                                                                                  self.var_contact.get(),
                                                                                  hashed_password
                                                
                        
                        
                                                                                ))
                  conn.commit() 
                  conn.close()
                  messagebox.showinfo('Success','Registration Done!')          
    def  return_login(self):
        self.root.destroy()
                  
           
class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')
        image_path = "C:/Users/Asus/Downloads/hotel-welcome.jpg"

        # Load the image using Pillow
        img = Image.open(image_path)
        img = img.resize((1550, 800))  # Resize the image to the window size

        self.bg_image = ImageTk.PhotoImage(img)

        # Create a label to display the image
        bg_label = Label(self.root, image=self.bg_image)
        bg_label.place(x=0,y=0)

        #self.bg_image = PhotoImage(file=image_path)

        
        #=========== In Frame ============
        main_frame = Frame(self.root, bd = 4, relief=RIDGE)
        main_frame.place(x=0,y=270,width=1550,height=700)
        # Specify the path to the image file
        image_path1 = "C:/Users/Asus/Downloads/welcome_hotel_neckarsulm_lobby_3k.2560x1600.jpg"

        # Load the image using Pillow
        img1 = Image.open(image_path1)
        img1 = img1.resize((1000, 800))  # Resize the image to the window size

        self.bg_image1 = ImageTk.PhotoImage(img1)

        # Create a label to display the image
        bg_label1 = Label(main_frame, image=self.bg_image1)
        bg_label1.place(x=58,y=0,width=1550,height=700)


        #=========== In Frame ============
        #main_frame = Frame(self.root, bd = 4, relief=RIDGE)
        #main_frame.place(x=0,y=190,width=1550,height=620)

        #============ Menu ============
        lbl_menu = Label(main_frame, text = 'Menu', font=('times new roman',20,'bold'))
        lbl_menu.place(x=0,y=0)

       #=========== Button Frame ============
        btn_frame = Frame(main_frame, bd = 4, relief=RIDGE)
        btn_frame.place(x=0,y=35,width=330,height=330)

       #=========== Buttons ============
        hotel_btn = Button(btn_frame,text='HOTEL', command=self.Hotel_details, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        hotel_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame,text='ROOM', command=self.roomdetails,width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        room_btn.grid(row=1,column=0,pady=1)

        guest_btn = Button(btn_frame,text='GUEST', command= self.guest_details ,width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        guest_btn.grid(row=2,column=0,pady=1)

        service_btn = Button(btn_frame,text='SERVICE',command= self.service_details, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        service_btn.grid(row=3,column=0,pady=1)

        staff_btn = Button(btn_frame,command=self.staffdetails,text='STAFF',width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        staff_btn.grid(row=4,column=0,pady=1)

        reservation_btn = Button(btn_frame, command= self.reservation_details,text='RESERVATION',width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        reservation_btn.grid(row=5,column=0,pady=1)

        room_service_order = Button(btn_frame,text='ROOM SERVICE ORDER',command=self.roomservicedetails,width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        room_service_order.grid(row=6,column=0,pady=1)

        feedback = Button(btn_frame,text='FEEDBACK',command=self.feedbackdetails,width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        feedback.grid(row=7,column=0,pady=1)

        myservice = Button(btn_frame,text='OUR SERVICES', command= self.myservicedetails, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        myservice.grid(row=8,column=0,pady=1)

        logout = Button(btn_frame,text='LOGOUT',command=self.logout,width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        logout.grid(row=9,column=0,pady=1)
    

    #=============guest button funtion================
    def guest_details(self):
        self.new_window = Toplevel(self.root)
        self.app = guest_window(self.new_window)


    #================reservatioon funtion=============
    def reservation_details(self):
         self.new_window = Toplevel(self.root)
         self.app = reservation_window(self.new_window)
    

    #=============Hotel button funtion================
    def Hotel_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Hotel_win(self.new_window)

    #=============Service button funtion================
    def service_details(self):
         self.new_window = Toplevel(self.root)
         self.app = Service_win(self.new_window)

    #=====================Feedback================
    def feedbackdetails(self):
        self.new_window=Toplevel(self.root)
        self.app=Feedback(self.new_window)
    #=================================staff===========================
    def staffdetails(self):
        self.new_window1=Toplevel(self.root)
        self.app=Staff(self.new_window1)

    #=================================room===========================
    def roomdetails(self):
        self.new_window1=Toplevel(self.root)
        self.app=room_window(self.new_window1)

    #=================================roomservice===========================
    def roomservicedetails(self):
        self.new_window1=Toplevel(self.root)
        self.app=roomservice_window(self.new_window1)

    #=============MyService button funtion================
    def myservicedetails(self):
        self.new_window1=Toplevel(self.root)
        self.app=myservice_window(self.new_window1)

    



    
    #==========================LOG OUT============================
    def logout(self):
         self.root.destroy()



if __name__ == "__main__":
    main()
