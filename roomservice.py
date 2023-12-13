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



class roomservice_window:
    def __init__(self,root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')


        #============================================variables================
        self.var_order_id = StringVar()
        x = random.randint(1000,9999)

        self.var_order_id.set(str(x))

        

        self.var_reservation_id = IntVar()
        self.var_service_name = StringVar()
        self.var_quantity = IntVar()
        self.var_total_price = IntVar()

        
        

        #=============labelframe===================
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Service Details', font=('times new roman',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=370)


        #==================labels_Attributes==============

        #==================Order ID============== 
        lbl_order_id_ref = Label(labelframeleft, text = 'Order ID', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_order_id_ref.grid(row=0,column=0, sticky=W)

        order_id_entry = ttk.Entry(labelframeleft, textvariable= self.var_order_id, width=30, font=('times new roman', 13, 'bold'))
        order_id_entry.grid(row=0, column=1)

        #==================Reservation ID==============

        lbl_reservation_id_ref = Label(labelframeleft, text = 'Reservation ID', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_reservation_id_ref.grid(row=1,column=0, sticky=W)

        reservation_id_entry = ttk.Entry(labelframeleft, textvariable=self.var_reservation_id ,width=30, font=('times new roman', 13, 'bold'))
        reservation_id_entry.grid(row=1, column=1)

        #==================Service Name==============

        lbl_service_name_ref = Label(labelframeleft, text = 'Service Name', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_service_name_ref.grid(row=2,column=0, sticky=W)

        service_name_entry = ttk.Entry(labelframeleft, textvariable= self.var_service_name, width=15, font=('times new roman', 13, 'bold'))
        service_name_entry.grid(row=2, column=1)

        #=========================service name combo box===================

        combo_ref = ttk.Combobox(labelframeleft,  values=self.get_myservice_names(),
                                 textvariable=self.var_service_name, font=('times new roman', 13, 'bold'), state='readonly')
        combo_ref.grid(row=2, column=1)

        #==================Quantity==============

        lbl_quantity_ref = Label(labelframeleft, text = 'Quantity', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_quantity_ref.grid(row=3,column=0, sticky=W)

        quantity_entry = ttk.Entry(labelframeleft, textvariable= self.var_quantity, width=30, font=('times new roman', 13, 'bold'))
        quantity_entry.grid(row=3, column=1)

        #==================Total Price==============

        lbl_total_price_ref = Label(labelframeleft, text = 'Total Price', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_total_price_ref.grid(row=4,column=0, sticky=W)

        total_price_entry = ttk.Entry(labelframeleft, textvariable = self.var_total_price , width=30, font=('times new roman', 13, 'bold'))
        total_price_entry.grid(row=4, column=1)




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

        bill_button = Button(button_frame,command=self.calculate_price_for_service, text='BILL', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=8)
        bill_button.grid(row=1, column=0)





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
        combo_search['value']=('ReservationID', 'OrderID', 'ServiceName')
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

        self.room_service_details_table = ttk.Treeview(show_data_frame, columns = ('OrderID', 'ReservationID', 'ServiceName', 'Quantity', 'TotalPrice'), xscrollcommand=scroll_bar_x, yscrollcommand=scroll_bar_y)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.room_service_details_table.xview)
        scroll_bar_y.config(command=self.room_service_details_table.yview)
        
        self.room_service_details_table.heading('OrderID', text='Order ID')
        self.room_service_details_table.heading('ReservationID', text='Reservation ID')
        self.room_service_details_table.heading('ServiceName', text='Service Name')
        self.room_service_details_table.heading('Quantity', text='Quantity')
        self.room_service_details_table.heading('TotalPrice', text='TotalPrice')
        

        self.room_service_details_table['show'] = 'headings'

        self.room_service_details_table.column('OrderID', width=100)
        self.room_service_details_table.column('ReservationID', width=100)
        self.room_service_details_table.column('ServiceName', width=100)
        self.room_service_details_table.column('Quantity', width=100)
        self.room_service_details_table.column('TotalPrice', width=100)
        



        self.room_service_details_table.pack(fill=BOTH, expand=1)




        self.fetch_data()
        self.room_service_details_table.bind('<ButtonRelease-1>',self.get_cursor)


#====================================to a add a data=============================
    def add_data(self):
        if self.var_total_price.get() == '' or self.var_reservation_id.get() == '':
            messagebox.showerror('STUPID!', 'All Fields Are Required!',parent = self.root )
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO `roomservice`(`OrderID`, `ReservationID`, `ServiceName`, `Quantity`, `TotalPrice`) VALUES (%s,%s,%s,%s,%s)',(
                    self.var_order_id.get(),
                    self.var_reservation_id.get(),
                    self.var_service_name.get(),
                    self.var_quantity.get(),
                    self.var_total_price.get()

                ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Info!', 'Order Added!', parent = self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong : {str(es)}', parent = self.root)


#=============================to show in the table=====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from roomservice')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.room_service_details_table.delete(*self.room_service_details_table.get_children())
            for i in rows:
                self.room_service_details_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    
#===================to select a name from the table===================
    def get_cursor(self, event =''):
        cursor_row= self.room_service_details_table.focus()
        content = self.room_service_details_table.item(cursor_row)
        row = content['values']

        self.var_order_id.set(row[0]),
        self.var_reservation_id.set(row[1]),
        self.var_service_name.set(row[2]),
        self.var_quantity.set(row[3]),
        self.var_total_price.set(row[4]),
        



    def update(self):
        if self.var_total_price.get()=='':
            messagebox.showerror('Error', 'Please Enter Price', parent = self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE `roomservice` SET `ReservationID`= %s ,`ServiceName`= %s ,`Quantity`= %s ,`TotalPrice`= %s  WHERE `OrderID`= %s ',(
                    
                    self.var_reservation_id.get(),
                    self.var_service_name.get(),
                    self.var_quantity.get(),
                    self.var_total_price.get(),
                    self.var_order_id.get()

            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update', 'Order Details has been updated successfully', parent = self.root)

    def fun_delete(self):
        mdelete = messagebox.askyesno('HEY YOU', 'Do you want to delete this order', parent = self.root)
        if mdelete>0:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            query = 'DELETE FROM `roomservice` WHERE  `OrderID`= %s'
            value = (self.var_order_id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    
    def reset(self):

        x = random.randint(1000,9999)
        self.var_order_id.set(str(x))

        self.var_reservation_id.set(''),
        self.var_service_name.set(''),
        self.var_quantity.set(''),
        self.var_total_price.set('')
        


    
    def search (self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()

        new_var1 = str(self.search_var.get())
        new_var2 = str(self.txt_search.get())

        my_cursor.execute(f"select * from roomservice where {new_var1} = '{new_var2}'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.room_service_details_table.delete(*self.room_service_details_table.get_children())
            for i in rows:
                self.room_service_details_table.insert('',END,values=i)
            conn.commit()
        else:
            messagebox.showerror('Alas!', 'This order does not exist',parent = self.root)
        conn.close()


    def calculate_price_for_service(self):
        try:
            service_name = self.var_service_name.get()
            quantity = int(self.var_quantity.get())

            
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()

            price_query = "SELECT Price FROM myservice WHERE Name = %s"
            my_cursor.execute(price_query, (service_name,))
            result = my_cursor.fetchone()

            if result:
                myservice_price = result[0]
                total_price = quantity * myservice_price

                self.var_total_price.set(total_price)

                messagebox.showinfo('Notice!',f"Service Name: {service_name}, Quantity: {quantity}, MyService Price: {myservice_price}, Total Price: {total_price}", parent = self.root)
            else:
                messagebox.showerror('Error!',f"Service {service_name} not found in myservice table.",parent = self.root)

        except Exception as e:
            messagebox.showerror('Error!',f"Error: {str(e)}",parent = self.root)

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





if __name__ == '__main__':
    root = Tk()
    obj = roomservice_window(root)
    root.mainloop()