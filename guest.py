from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector

conn = mysql.connector.connect(host = 'localhost', username = 'root', password = '', database = 'hotel management system')
my_cursor = conn.cursor()
conn.commit()
conn.close()
print('Connection successfully created')



class guest_window:
    def __init__(self,root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')


        #============================================variables================
        self.var_guest_id = StringVar()
        x = random.randint(1000,9999)

        self.var_guest_id.set(str(x))

        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_spent = IntVar()
        
        


        #=============labelframe===================
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text='Guest Details', font=('times new roman',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=370)


        #==================labels_Attributes==============

        #==================Guest ID==============
        lbl_guest_id_ref = Label(labelframeleft, text = 'Guest ID', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_guest_id_ref.grid(row=0,column=0, sticky=W)

        guest_id_entry = ttk.Entry(labelframeleft, textvariable= self.var_guest_id, width=30, font=('times new roman', 13, 'bold'))
        guest_id_entry.grid(row=0, column=1)

        #==================First Name==============

        lbl_first_name_ref = Label(labelframeleft, text = 'First Name', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_first_name_ref.grid(row=1,column=0, sticky=W)

        first_name_entry = ttk.Entry(labelframeleft, textvariable=self.var_first_name ,width=30, font=('times new roman', 13, 'bold'))
        first_name_entry.grid(row=1, column=1)

        #==================Last Name==============

        lbl_last_name_ref = Label(labelframeleft, text = 'Last Name', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_last_name_ref.grid(row=2,column=0, sticky=W)

        last_name_entry = ttk.Entry(labelframeleft, textvariable= self.var_last_name, width=30, font=('times new roman', 13, 'bold'))
        last_name_entry.grid(row=2, column=1)

        #==================Email==============

        lbl_email_ref = Label(labelframeleft, text = 'Email', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_email_ref.grid(row=3,column=0, sticky=W)

        email_entry = ttk.Entry(labelframeleft, textvariable= self.var_email, width=30, font=('times new roman', 13, 'bold'))
        email_entry.grid(row=3, column=1)

        #==================Phone==============

        lbl_phone_ref = Label(labelframeleft, text = 'Phone', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_phone_ref.grid(row=4,column=0, sticky=W)

        phone_entry = ttk.Entry(labelframeleft, textvariable=self.var_phone, width=30, font=('times new roman', 13, 'bold'))
        phone_entry.grid(row=4, column=1)

        #==================Spent==============

        lbl_spent_ref = Label(labelframeleft, text = 'Spent', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_spent_ref.grid(row=5,column=0, sticky=W)

        spent_entry = ttk.Entry(labelframeleft, textvariable=self.var_spent, width=30, font=('times new roman', 13, 'bold'), state='readonly')
        spent_entry.grid(row=5, column=1)


        #=====================================buttons================


        #====button frame===
        button_frame = Frame(labelframeleft, bd =2, relief=RIDGE)
        button_frame.place(x=0,y=230,width=410,height=90)

        #=========buttons========
        add_button = Button(button_frame,command=self.add_data, text='ADD', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=8)
        add_button.grid(row=0, column=0)

        update_button = Button(button_frame,command= self.update, text='UPDATE', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=9)
        update_button.grid(row=0, column=1)

        delete_button = Button(button_frame, command=self.fun_delete, text='DELETE', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=10)
        delete_button.grid(row=0, column=2)

        reset_button = Button(button_frame, command= self.reset ,text='RESET', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=10)
        reset_button.grid(row=0, column=3)

        calculate_total_button = Button(button_frame, command= self.calculate_total ,text='TOTAL', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=8)
        calculate_total_button.grid(row=1, column=0)




        #========================table frame========================
        tableframe = LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details', font=('times new roman',12,'bold'))
        tableframe.place(x=435,y=50,width=860,height=890)
        

        #================================Search By=========================
        #=========search label=======
        lbl_search_by = Label(tableframe, text = 'Search By :', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_search_by.grid(row=0,column=0, sticky=W)

        
        
        #=========combo box=======

        self.search_var = StringVar()
        combo_search = ttk.Combobox(tableframe, textvariable=self.search_var, font=('times new roman',12, 'bold'), width=24, state='readonly')
        combo_search['value']=('Phone', 'Email')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=6)

        
        #=========search entry space=======

        self.txt_search = StringVar()
        search_by_entry = ttk.Entry(tableframe, textvariable=self.txt_search, width=29, font=('times new roman', 13, 'bold'))
        search_by_entry.grid(row=0, column=2, padx=6)
        
        #=========search button=======
        search_button = Button(tableframe, command= self.search , text='SEARCH', font=('times new roman', 13, 'bold'),padx=2, pady=0, width=8)
        search_button.grid(row=0, column=3, padx=6)
        
        #=========show all button=======
        show_all_button = Button(tableframe, command= self.fetch_data, text='SHOW ALL', font=('times new roman', 13, 'bold'),padx=2, pady=0, width=8)
        show_all_button.grid(row=0, column=4, padx=6)



        #==========================Show Data Frame======================

        show_data_frame = Frame(tableframe, bd =2, relief=RIDGE)
        show_data_frame.place(x=2,y=50,width=850,height=600)

        scroll_bar_x = ttk.Scrollbar(show_data_frame,orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(show_data_frame,orient=VERTICAL)

        self.guest_details_table = ttk.Treeview(show_data_frame, columns = ('GuestID', 'FirstName', 'LastName', 'Email', 'Phone', 'Spent'), xscrollcommand=scroll_bar_x, yscrollcommand=scroll_bar_y)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.guest_details_table.xview)
        scroll_bar_y.config(command=self.guest_details_table.yview)
        
        self.guest_details_table.heading('GuestID', text='Guest ID')
        self.guest_details_table.heading('FirstName', text='First Name')
        self.guest_details_table.heading('LastName', text='Last Name')
        self.guest_details_table.heading('Email', text='Email')
        self.guest_details_table.heading('Phone', text='Phone')
        self.guest_details_table.heading('Spent', text='Spent')

        self.guest_details_table['show'] = 'headings'

        self.guest_details_table.column('GuestID', width=100)
        self.guest_details_table.column('FirstName', width=100)
        self.guest_details_table.column('LastName', width=100)
        self.guest_details_table.column('Email', width=100)
        self.guest_details_table.column('Phone', width=100)
        self.guest_details_table.column('Spent', width=100)



        self.guest_details_table.pack(fill=BOTH, expand=1)




        self.fetch_data()
        self.guest_details_table.bind('<ButtonRelease-1>',self.get_cursor)


#====================================to a add a data=============================
    def add_data(self):
        if self.var_phone.get() == '' or self.var_first_name.get() == '':
            messagebox.showerror('STUPID!', 'All Fields Are Required!',parent = self.root )
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO `guest`(`GuestID`, `FirstName`, `LastName`, `Email`, `Phone`, `Spent`) VALUES (%s,%s,%s,%s,%s,%s)',(
                    self.var_guest_id.get(),
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_spent.get()

                ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('GENIUS!', 'Guest Added!', parent = self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong : {str(es)}', parent = self.root)


#=============================to show in the table=====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from guest')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.guest_details_table.delete(*self.guest_details_table.get_children())
            for i in rows:
                self.guest_details_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    
#===================to select a name from the table===================
    def get_cursor(self, event =''):
        cursor_row= self.guest_details_table.focus()
        content = self.guest_details_table.item(cursor_row)
        row = content['values']

        self.var_guest_id.set(row[0]),
        self.var_first_name.set(row[1]),
        self.var_last_name.set(row[2]),
        self.var_email.set(row[3]),
        self.var_phone.set(row[4]),
        self.var_spent.set(row[5]),



    def update(self):
        if self.var_phone.get()=='':
            messagebox.showerror('Error', 'Please Enter Mobile Number', parent = self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE `guest` SET `FirstName`= %s ,`LastName`= %s ,`Email`= %s ,`Phone`= %s ,`Spent`= %s  WHERE `GuestID`= %s ',(
                    
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_spent.get(),
                    self.var_guest_id.get()

            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update', 'Customer Details has been updated successfully', parent = self.root)

    def fun_delete(self):
        mdelete = messagebox.askyesno('HEY YOU', 'Do you want to delete this guest', parent = self.root)
        if mdelete>0:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            query = 'DELETE FROM `guest` WHERE  `GuestID`= %s'
            value = (self.var_guest_id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    
    def reset(self):

        x = random.randint(1000,9999)
        self.var_guest_id.set(str(x))

        self.var_first_name.set(''),
        self.var_last_name.set(''),
        self.var_email.set(''),
        self.var_phone.set(''),
        self.var_spent.set(0)


    
    def search (self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()

        new_var1 = str(self.search_var.get())
        new_var2 = str(self.txt_search.get())

        my_cursor.execute(f"select * from guest where {new_var1} = '{new_var2}'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.guest_details_table.delete(*self.guest_details_table.get_children())
            for i in rows:
                self.guest_details_table.insert('',END,values=i)
            conn.commit()
        else:
            messagebox.showerror('Alas!', 'This guest does not exist',parent = self.root)
        conn.close()




    def calculate_total(self):
        guest_id = self.var_guest_id.get()

        try:
            conn = mysql.connector.connect(
                host='localhost', username='root', port='3306', password='', database='hotel management system')
            my_cursor = conn.cursor()

            
            total_cost_query = "SELECT COALESCE(SUM(TotalCost), 0) FROM reservation WHERE GuestID = %s"
            my_cursor.execute(total_cost_query, (guest_id,))
            total_cost = my_cursor.fetchone()[0]

            
            price_query = "SELECT COALESCE(SUM(Price), 0) FROM service WHERE GuestID = %s"
            my_cursor.execute(price_query, (guest_id,))
            price = my_cursor.fetchone()[0]

            
            total_price_query = "SELECT COALESCE(SUM(TotalPrice), 0) FROM roomservice WHERE ReservationID IN (SELECT ReservationID FROM reservation WHERE GuestID = %s)"
            my_cursor.execute(total_price_query, (guest_id,))
            total_price = my_cursor.fetchone()[0]

            total_spent = total_cost + price + total_price
            self.var_spent.set(total_spent)

           
            #=======creating label============
            labelframebottom = LabelFrame(self.root,bd=2,relief=RIDGE,text='Informations', font=('times new roman',12,'bold'))
            labelframebottom.place(x=5,y=470,width=425,height=150)
                
            #==============Reservation Cost===========
            lblname=Label(labelframebottom,text='Reservation Cost :',font=('times new roman',13,'bold'))
            lblname.place(x=0,y=0)
            lbl=Label(labelframebottom,text=total_cost,font=('times new roman',13,'bold'))
            lbl.place(x=220,y=0)
            #=========Service Cost============
            lbladrs=Label(labelframebottom,text='Service Cost :',font=('times new roman',13,'bold'))
            lbladrs.place(x=0,y=25)

            lbl1=Label(labelframebottom,text=price,font=('times new roman',13,'bold'))
            lbl1.place(x=220,y=25)

            #==========RoomService Cost=========
            lblrat=Label(labelframebottom,text='RoomService Cost : ',font=('times new roman',13,'bold'))
            lblrat.place(x=0,y=50)
            lbl1=Label(labelframebottom,text=total_price,font=('times new roman',13,'bold'))
            lbl1.place(x=220,y=50)
            #===========Total=======
            lbladrs=Label(labelframebottom,text='Total Spent :',font=('times new roman',13,'bold'))
            lbladrs.place(x=0,y=75)

            lbl1=Label(labelframebottom,text=total_spent,font=('times new roman',13,'bold'))
            lbl1.place(x=220,y=75)

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()





if __name__ == '__main__':
    root = Tk()
    obj = guest_window(root)
    root.mainloop()