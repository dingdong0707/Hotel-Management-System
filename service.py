from tkinter import*
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Service_win:
    def __init__(self,root):
        self.root=root
        self.root.title('Service Window')
        self.root.geometry('1295x550+230+220')


        #============================================variables================
        self.var_service_id = StringVar()
        x = random.randint(1000,9999)

        self.var_service_id.set(str(x))
        
        #self.var_service_id= StringVar()
        
        self.var_name = StringVar()
        self.var_quantity = IntVar()
        self.var_price = StringVar()
        self.var_hotel_id = StringVar()
        self.var_guest_id = StringVar()
    
        
        #=======================Title===============================
        lbl_title=Label(self.root,text='Service Details',font=('times new roman',18,'bold'),bg='sky blue',fg='Black')
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #=========================labelFrame=============================================
        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Service Details',font=('times new roman',12,'bold'),padx=2)
        labelFrameleft.place(x=5,y=50,width=425,height=490)

        #===================================== Labels & Entry=============================
        lbl_hotel_ref=Label(labelFrameleft,text='ServiceID', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_service_id,font=('times new roman',13,'bold'))
        enty_ref.grid(row=0,column=1)


        lbl_hotel_ref=Label(labelFrameleft,text='Name', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=1,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=21,textvariable=self.var_name,font=('times new roman',13,'bold'))
        enty_ref.grid(row=1,column=1)

        #=========================service name combo box===================

        combo_ref = ttk.Combobox(labelFrameleft, values=self.get_myservice_names(),
                                 textvariable=self.var_name, font=('times new roman', 13, 'bold'), state='readonly')
        combo_ref.grid(row=1, column=1)

        

        #==========================LabelFrameLeft Button ====================

        btncalculate_price_for_service=Button(labelFrameleft,text="Generate Price",command=self.calculate_price_for_service,font=("arial",12,'bold'),bg="sky blue",width=15)
        btncalculate_price_for_service.grid(row=6,column=0,padx=1, sticky=W)



        #===================================== Labels & Entry=============================

        lbl_hotel_ref=Label(labelFrameleft,text='Quantity', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=2,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_quantity,font=('times new roman',13,'bold'))
        enty_ref.grid(row=2,column=1)



        lbl_hotel_ref=Label(labelFrameleft,text='Price', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=3,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_price,font=('times new roman',13,'bold'))
        enty_ref.grid(row=3,column=1)

        lbl_hotel_ref=Label(labelFrameleft,text='HotelID', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=4,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_hotel_id,font=('times new roman',13,'bold'))
        enty_ref.grid(row=4,column=1)

        lbl_hotel_ref=Label(labelFrameleft,text='GuestID', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=5,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_guest_id,font=('times new roman',13,'bold'))
        enty_ref.grid(row=5,column=1)

        #=================================A_U_D_R=========================
        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,'bold'),bg="sky blue",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,'bold'),bg="sky blue",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.fun_delete,font=("arial",12,'bold'),bg="sky blue",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,'bold'),bg="sky blue",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #=========================TableFrame SEARCH=============================================
        TableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search',font=('times new roman',12,'bold'),padx=2)
        TableFrame.place(x=435,y=50,width=860,height=490)
        
        #=================================================Search By=============================
        #================================Search label======================================
        lbl_search=Label(TableFrame,text='Search By', font=('times new roman',12,'bold'),bg='grey',fg='black')
        lbl_search.grid(row=0,column=0,sticky=W,padx=2)

        #===========================Commbo Box==================================
        self.search_var=StringVar()
        combo_search=ttk.Combobox(TableFrame,textvariable=self.search_var,font=("arial",12,'bold'),width=24,state="readonly")
        combo_search['value']=("ServiceID","Price",'Name')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2) 

        #=================search entry place================================
        self.txt_search = StringVar()
        search_by_entry =ttk.Entry(TableFrame,textvariable=self.txt_search,font=("arial",13,'bold'),width=24)
        search_by_entry.grid(row=0,column=2,padx=2)

        #==========================================Search button====================
        search_button=Button(TableFrame,text="Search",command=self.search,font=("arial",12,'bold'),bg="sky blue",width=10)
        search_button.grid(row=0,column=3,padx=1)

        btnShowAll=Button(TableFrame,text="Show All",command=self.fetch_data,font=("arial",12,'bold'),bg="sky blue",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #===========================Show Data Table========================

        det_table=Frame(TableFrame,bd=2,relief=RIDGE)
        det_table.place(x=0,y=50,width=860,height=350)

        Scroll_x=ttk.Scrollbar(det_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(det_table,orient=VERTICAL)

        self.Service_details_Table= ttk.Treeview(det_table,column=('ServiceID','Name','Quantity','Price','HotelID', 'GuestID'),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Service_details_Table.xview)
        Scroll_y.config(command=self.Service_details_Table.yview)

        self.Service_details_Table.heading('ServiceID',text="ServiceID")
        self.Service_details_Table.heading('Name',text="Name")
        self.Service_details_Table.heading('Quantity',text="Quantity")
        self.Service_details_Table.heading('Price',text="Price")
        self.Service_details_Table.heading('HotelID',text="HotelID")
        self.Service_details_Table.heading('GuestID',text="GuestID")
  

        self.Service_details_Table['show']="headings"


        #=================adjusting width ===========
        self.Service_details_Table.column('ServiceID', width=100)
        self.Service_details_Table.column('Name', width=100)
        self.Service_details_Table.column('Quantity', width=100)
        self.Service_details_Table.column('Price', width=100)
        self.Service_details_Table.column('HotelID', width=100)
        self.Service_details_Table.column('GuestID', width=100)


        self.Service_details_Table.pack(fill=BOTH,expand=1)


        self.fetch_data()
        self.Service_details_Table.bind('<ButtonRelease-1>',self.get_cursor)





##====================adding data==========================
    def add_data(self):
        if self.var_name.get()==''or self.var_service_id.get()=='':
              messagebox.showerror('Error','Please provide all the data',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO `service`(`ServiceID`, `Name`, `Quantity`, `Price`, `HotelID`,`GuestID`) VALUES (%s,%s,%s,%s,%s,%s)',(
                    self.var_service_id.get(),
                    self.var_name.get(),
                    self.var_quantity.get(),
                    self.var_price.get(),
                    self.var_hotel_id.get(),
                    self.var_guest_id.get()

                ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('good!', 'Data  Added!', parent = self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong : {str(es)}', parent = self.root)

            
         
#=============================to show in the table=====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from service')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Service_details_Table.delete(*self.Service_details_Table.get_children())
            for i in rows:
                self.Service_details_Table.insert('',END,values=i)
            conn.commit()
        conn.close()
#===================to select a name from the table===================
    def get_cursor(self, event =''):
        cursor_row= self.Service_details_Table.focus()
        content = self.Service_details_Table.item(cursor_row)
        row = content['values']

        self.var_service_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_quantity.set(row[2]),
        self.var_price.set(row[3])
        self.var_hotel_id.set(row[4]),
        self.var_guest_id.set(row[5])
    
    def update(self):
        if self.var_service_id.get()=='':
            messagebox.showerror('Error', 'Please Enter Your ID', parent = self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE `service` SET `Name`= %s ,`Quantity`= %s ,`Price`= %s ,`HotelID`= %s ,`GuestID`= %s WHERE `ServiceID`= %s ',(
                    
                    self.var_name.get(),
                    self.var_quantity.get(),
                    self.var_price.get(),
                    self.var_hotel_id.get(),
                    self.var_guest_id.get(),
                    self.var_service_id.get()

            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Updated', 'Data has been updated successfully', parent = self.root)
    
    def fun_delete(self):
          mdelete = messagebox.askyesno('HELLO', 'Do you want to delete this data', parent = self.root)
          if mdelete>0:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            query = 'DELETE FROM `service` WHERE  `ServiceID`= %s'
            value = (self.var_service_id.get(),)
            my_cursor.execute(query,value)
          else:
            if not mdelete:
                return
          conn.commit()
          self.fetch_data()
          conn.close()

    
    def reset(self):
        x = random.randint(1000,9999)
        self.var_service_id.set(str(x))

        self.var_name.set(''),
        self.var_quantity.set(''),
        self.var_price.set('')
        self.var_hotel_id.set(''),
        self.var_guest_id.set('')


    
    def search (self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()

        new_var1 = str(self.search_var.get())
        new_var2 = str(self.txt_search.get())

        my_cursor.execute(f"select * from service where {new_var1} = '{new_var2}'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Service_details_Table.delete(*self.Service_details_Table.get_children())
            for i in rows:
                self.Service_details_Table.insert('',END,values=i)
            conn.commit()
        else:
            messagebox.showerror('Alas!', 'This service does not exist',parent = self.root)
        conn.close()







    def calculate_price_for_service(self):
        try:
            service_name = self.var_name.get()
            quantity = int(self.var_quantity.get())

            
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()

            price_query = "SELECT Price FROM myservice WHERE Name = %s"
            my_cursor.execute(price_query, (service_name,))
            result = my_cursor.fetchone()

            if result:
                myservice_price = result[0]
                total_price = quantity * myservice_price

                self.var_price.set(total_price)

                messagebox.showinfo('Notice!',f"Service Name: {service_name}, Quantity: {quantity}, MyService Price: {myservice_price}, Total Price: {total_price}", parent = self.root)
            else:
                messagebox.showerror('Error!',f"Service {service_name} not found in myservice table.")

        except Exception as e:
            messagebox.showerror('Error!',f"Error: {str(e)}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()


    def get_myservice_names(self):
        try:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT DISTINCT Name FROM myservice")
            service_names = [row[0] for row in my_cursor.fetchall()]
            if service_names:
                return service_names
            else:
                messagebox.showinfo('Info', 'No services in this hotel')
        
        except Exception as e:
            messagebox.showerror('Error!',f"Error: {str(e)}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()


            


        




if __name__ == "__main__":
        root=Tk()
        obj=Service_win(root)
        root.mainloop()

