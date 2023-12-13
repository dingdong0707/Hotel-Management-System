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



class myservice_window:
    def __init__(self,root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')


        #============================================variables================
        self.var_name = StringVar()
        self.var_price = IntVar()
        #=============labelframe===================
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text='Our Services', font=('times new roman',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=370)

        #==================labels_Attributes==============

        #==================Name============== 
        lbl_name_ref = Label(labelframeleft, text = 'Name', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_name_ref.grid(row=0,column=0, sticky=W)

        name_id_entry = ttk.Entry(labelframeleft, textvariable= self.var_name, width=30, font=('times new roman', 13, 'bold'))
        name_id_entry.grid(row=0, column=1)

        #==================Price==============

        lbl_price_ref = Label(labelframeleft, text = 'Price', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_price_ref.grid(row=1,column=0, sticky=W)

        price_entry = ttk.Entry(labelframeleft, textvariable=self.var_price ,width=30, font=('times new roman', 13, 'bold'))
        price_entry.grid(row=1, column=1)

       

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

        service_info_button = Button(button_frame, command= self.get_service_total_sold ,text='INFO', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=8)
        service_info_button.grid(row=1, column=0)


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
        combo_search['value']=('Name', 'Price')
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

        self.myservice_details_table = ttk.Treeview(show_data_frame, columns = ('Name', 'Price'), xscrollcommand=scroll_bar_x, yscrollcommand=scroll_bar_y)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.myservice_details_table.xview)
        scroll_bar_y.config(command=self.myservice_details_table.yview)
        
        self.myservice_details_table.heading('Name', text='Name')
        self.myservice_details_table.heading('Price', text='Price')
        

        self.myservice_details_table['show'] = 'headings'

        self.myservice_details_table.column('Name', width=100)
        self.myservice_details_table.column('Price', width=100)



        self.myservice_details_table.pack(fill=BOTH, expand=1)



        self.fetch_data()
        self.myservice_details_table.bind('<ButtonRelease-1>',self.get_cursor)


#====================================to a add a data=============================
    def add_data(self):
        if self.var_name.get() == '' or self.var_price.get() == '':
            messagebox.showerror('STUPID!', 'All Fields Are Required!',parent = self.root )
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO `myservice`(`Name`, `Price`) VALUES (%s,%s)',(
                    self.var_name.get(),
                    self.var_price.get()

                ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Info!', 'New Service Added!', parent = self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong : {str(es)}', parent = self.root)


#=============================to show in the table=====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from myservice')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.myservice_details_table.delete(*self.myservice_details_table.get_children())
            for i in rows:
                self.myservice_details_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    
#===================to select a name from the table===================
    def get_cursor(self, event =''):
        cursor_row= self.myservice_details_table.focus()
        content = self.myservice_details_table.item(cursor_row)
        row = content['values']

        self.var_name.set(row[0]),
        self.var_price.set(row[1]),



    def update(self):
        if self.var_price.get()=='':
            messagebox.showerror('Error', 'Please Enter Price', parent = self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE `myservice` SET `Price`= %s WHERE `Name`= %s ',(
                    
                    self.var_price.get(),
    
                    self.var_name.get()

            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update', 'MyService Details has been updated successfully', parent = self.root)

    def fun_delete(self):
        mdelete = messagebox.askyesno('HEY YOU', 'Do you want to delete this Service', parent = self.root)
        if mdelete>0:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            query = 'DELETE FROM `myservice` WHERE  `Name`= %s'
            value = (self.var_name.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    
    def reset(self):

        x = random.randint(1000,9999)
        self.var_name.set(str(x))
        self.var_price.set(0)


    
    def search (self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()

        new_var1 = str(self.search_var.get())
        new_var2 = str(self.txt_search.get())

        my_cursor.execute(f"select * from myservice where {new_var1} = '{new_var2}'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.myservice_details_table.delete(*self.myservice_details_table.get_children())
            for i in rows:
                self.myservice_details_table.insert('',END,values=i)
            conn.commit()
        else:
            messagebox.showerror('Alas!', 'This Service does not exist',parent = self.root)
        conn.close()





    def get_service_total_sold(self):
        service_name = self.var_name.get()
        try:
            conn = mysql.connector.connect(host='localhost', username='root', port='3306', password='', database='hotel management system')
            my_cursor = conn.cursor()

            # ============================== Use JOIN to fetch total sold for a service
            query = '''
                SELECT 
                    m.Name,
                    m.Price,
                    COALESCE(SUM(s.Quantity), 0),
                    COALESCE(SUM(rs.Quantity), 0),
                    COALESCE(SUM(s.Quantity), 0) + COALESCE(SUM(rs.Quantity), 0) AS TotalSold
                FROM 
                    myservice m
                    LEFT JOIN service s ON m.Name = s.Name
                    LEFT JOIN roomservice rs ON m.Name = rs.ServiceName
                WHERE 
                    m.Name = %s
                GROUP BY
                    m.Name
            '''

            my_cursor.execute(query, (service_name,))

            result = my_cursor.fetchone()

            if result:
                messagebox.showinfo('Can proceed', 'This Name is valid',parent = self.root )

                #=======creating label============
                labelframebottom = LabelFrame(self.root,bd=2,relief=RIDGE,text='Informations', font=('times new roman',12,'bold'))
                labelframebottom.place(x=5,y=470,width=425,height=150)
                
                #==============Name===========
                lblname=Label(labelframebottom,text='Name :',font=('times new roman',13,'bold'))
                lblname.place(x=0,y=0)
                lbl=Label(labelframebottom,text=result[0],font=('times new roman',13,'bold'))
                lbl.place(x=220,y=0)
                #=========Price============
                lbladrs=Label(labelframebottom,text='Price :',font=('times new roman',13,'bold'))
                lbladrs.place(x=0,y=25)

                lbl1=Label(labelframebottom,text=result[1],font=('times new roman',13,'bold'))
                lbl1.place(x=220,y=25)

                #==========From service Table Total Sold=========
                lblrat=Label(labelframebottom,text='Quantity (Service) : ',font=('times new roman',13,'bold'))
                lblrat.place(x=0,y=50)
                lbl1=Label(labelframebottom,text=result[2],font=('times new roman',13,'bold'))
                lbl1.place(x=220,y=50)
                #===========From roomservice Table Total Sold=======
                lbladrs=Label(labelframebottom,text='Quantity (RoomService) :',font=('times new roman',13,'bold'))
                lbladrs.place(x=0,y=75)

                lbl1=Label(labelframebottom,text=result[3],font=('times new roman',13,'bold'))
                lbl1.place(x=220,y=75)

                #===========Total Sold=======
                lbladrs=Label(labelframebottom,text='Quantity (Total) :',font=('times new roman',13,'bold'))
                lbladrs.place(x=0,y=100)

                lbl1=Label(labelframebottom,text=result[4],font=('times new roman',13,'bold'))
                lbl1.place(x=220,y=100)
            else:
                messagebox.showwarning('Warning', 'Service name not found.', parent = self.root)

            conn.close()

        except Exception as e:

            print(f"Error: {e}")
            messagebox.showerror('Error', 'An error occurred while fetching room details.')



    







if __name__ == '__main__':
    root = Tk()
    obj = myservice_window(root)
    root.mainloop()