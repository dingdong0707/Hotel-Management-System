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



class room_window:
    def __init__(self,root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')


        #============================================variables================
        self.var_room_id = StringVar()
        x = random.randint(1000,9999)

        self.var_room_id.set(str(x))

        self.var_hotel_id = IntVar()
        self.var_room_number = StringVar()
        self.var_type = StringVar()
        self.var_price = IntVar()
        self.var_room_condition = StringVar()
        
        


        #=============labelframe===================
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Details', font=('times new roman',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=370)


        #==================labels_Attributes==============

        #==================Room ID============== 
        lbl_room_id_ref = Label(labelframeleft, text = 'Room ID', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_room_id_ref.grid(row=0,column=0, sticky=W)

        room_id_entry = ttk.Entry(labelframeleft, textvariable= self.var_room_id, width=30, font=('times new roman', 13, 'bold'))
        room_id_entry.grid(row=0, column=1)

        #==================Hotel ID==============

        lbl_hotel_id_ref = Label(labelframeleft, text = 'Hotel ID', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_hotel_id_ref.grid(row=1,column=0, sticky=W)

        hotel_id_entry = ttk.Entry(labelframeleft, textvariable=self.var_hotel_id ,width=30, font=('times new roman', 13, 'bold'))
        hotel_id_entry.grid(row=1, column=1)

        #==================Room Number==============

        lbl_room_number_ref = Label(labelframeleft, text = 'Room Number', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_room_number_ref.grid(row=2,column=0, sticky=W)

        room_number_entry = ttk.Entry(labelframeleft, textvariable= self.var_room_number, width=30, font=('times new roman', 13, 'bold'))
        room_number_entry.grid(row=2, column=1)

        #==================Type==============

        lbl_type_ref = Label(labelframeleft, text = 'Type', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_type_ref.grid(row=3,column=0, sticky=W)

        type_entry = ttk.Entry(labelframeleft, textvariable= self.var_type, width=30, font=('times new roman', 13, 'bold'))
        type_entry.grid(row=3, column=1)
        
        #==================Price==============

        lbl_price_ref = Label(labelframeleft, text = 'Price', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_price_ref.grid(row=4,column=0, sticky=W)

        price_entry = ttk.Entry(labelframeleft, textvariable = self.var_price , width=30, font=('times new roman', 13, 'bold'))
        price_entry.grid(row=4, column=1)

        #==================Room Condition==============

        lbl_room_condition_ref = Label(labelframeleft, text = 'Room Condition', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_room_condition_ref.grid(row=5,column=0, sticky=W)

        room_condition_entry = ttk.Entry(labelframeleft, textvariable = self.var_room_condition , width=20, font=('times new roman', 13, 'bold'))
        room_condition_entry.grid(row=5, column=1)

        #=========================service name combo box===================

        combo_ref = ttk.Combobox(labelframeleft, values=['Vacant', 'Booked'],
                                 textvariable=self.var_room_condition, font=('times new roman', 13, 'bold'), state='readonly')
        combo_ref.grid(row=5, column=1)


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

        room_info_button = Button(button_frame, command= self.get_room_info ,text='INFO', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=8)
        room_info_button.grid(row=1, column=0)




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
        combo_search['value']=('RoomID', 'RoomNumber')
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

        self.room_details_table = ttk.Treeview(show_data_frame, columns = ('RoomID', 'HotelID', 'RoomNumber', 'Type', 'Price', 'RoomCondition'), xscrollcommand=scroll_bar_x, yscrollcommand=scroll_bar_y)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.room_details_table.xview)
        scroll_bar_y.config(command=self.room_details_table.yview)
        
        self.room_details_table.heading('RoomID', text='Room ID')
        self.room_details_table.heading('HotelID', text='Hotel ID')
        self.room_details_table.heading('RoomNumber', text='Room Number')
        self.room_details_table.heading('Type', text='Type')
        self.room_details_table.heading('Price', text='Price')
        self.room_details_table.heading('RoomCondition', text='RoomCondition')

        self.room_details_table['show'] = 'headings'

        self.room_details_table.column('RoomID', width=100)
        self.room_details_table.column('HotelID', width=100)
        self.room_details_table.column('RoomNumber', width=100)
        self.room_details_table.column('Type', width=100)
        self.room_details_table.column('Price', width=100)
        self.room_details_table.column('RoomCondition', width=100)



        self.room_details_table.pack(fill=BOTH, expand=1)




        self.fetch_data()
        self.room_details_table.bind('<ButtonRelease-1>',self.get_cursor)


#====================================to a add a data=============================
    def add_data(self):
        if self.var_price.get() == '' or self.var_hotel_id.get() == '':
            messagebox.showerror('STUPID!', 'All Fields Are Required!',parent = self.root )
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO `room`(`RoomID`, `HotelID`, `RoomNumber`, `Type`, `Price`, `RoomCondition`) VALUES (%s,%s,%s,%s,%s,%s)',(
                    self.var_room_id.get(),
                    self.var_hotel_id.get(),
                    self.var_room_number.get(),
                    self.var_type.get(),
                    self.var_price.get(),
                    self.var_room_condition.get()

                ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Info!', 'Room Added!', parent = self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong : {str(es)}', parent = self.root)


#=============================to show in the table=====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from room')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    
#===================to select a name from the table===================
    def get_cursor(self, event =''):
        cursor_row= self.room_details_table.focus()
        content = self.room_details_table.item(cursor_row)
        row = content['values']

        self.var_room_id.set(row[0]),
        self.var_hotel_id.set(row[1]),
        self.var_room_number.set(row[2]),
        self.var_type.set(row[3]),
        self.var_price.set(row[4]),
        self.var_room_condition.set(row[5]),



    def update(self):
        if self.var_price.get()=='':
            messagebox.showerror('Error', 'Please Enter Price', parent = self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE `room` SET `HotelID`= %s ,`RoomNumber`= %s ,`Type`= %s ,`Price`= %s ,`RoomCondition`= %s  WHERE `RoomID`= %s ',(
                    
                    self.var_hotel_id.get(),
                    self.var_room_number.get(),
                    self.var_type.get(),
                    self.var_price.get(),
                    self.var_room_condition.get(),
                    self.var_room_id.get()

            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update', 'Room Details has been updated successfully', parent = self.root)

    def fun_delete(self):
        mdelete = messagebox.askyesno('HEY YOU', 'Do you want to delete this room', parent = self.root)
        if mdelete>0:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            query = 'DELETE FROM `room` WHERE  `RoomID`= %s'
            value = (self.var_room_id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    
    def reset(self):

        x = random.randint(1000,9999)
        self.var_room_id.set(str(x))

        self.var_hotel_id.set(''),
        self.var_room_number.set(''),
        self.var_type.set(''),
        self.var_price.set(''),
        self.var_room_condition.set(0)


    
    def search (self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()

        new_var1 = str(self.search_var.get())
        new_var2 = str(self.txt_search.get())

        my_cursor.execute(f"select * from room where {new_var1} = '{new_var2}'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert('',END,values=i)
            conn.commit()
        else:
            messagebox.showerror('Alas!', 'This room does not exist',parent = self.root)
        conn.close()





    def get_room_info(self):

        room_id = self.var_room_id.get()
        try:

            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()

            # ============================== Use JOIN to fetch room details along with additional information
            query = '''
                SELECT 
                    room.RoomID,
                    room.RoomNumber,
                    room.Type,
                    room.Price,
                    room.RoomCondition,
                    hotel_1.Name AS HotelName,
                    hotel_1.Address AS HotelAddress
                FROM 
                    room
                    JOIN hotel_1 ON room.HotelID = hotel_1.HotelID
                WHERE 
                    room.RoomID = %s
            '''

            my_cursor.execute(query, (room_id,))

            result = my_cursor.fetchone()

            if result:
                messagebox.showinfo('Can proceed', 'This id is valid',parent = self.root )

                #=======creating label============
                labelframebottom = LabelFrame(self.root,bd=2,relief=RIDGE,text='Informations', font=('times new roman',12,'bold'))
                labelframebottom.place(x=5,y=470,width=425,height=123)
                
                #==============Room ID===========
                lblname=Label(labelframebottom,text='Room ID :',font=('times new roman',13,'bold'))
                lblname.place(x=0,y=0)
                lbl=Label(labelframebottom,text=result[0],font=('times new roman',13,'bold'))
                lbl.place(x=120,y=0)
                #=========Room Condition====
                lbladrs=Label(labelframebottom,text='Condition :',font=('times new roman',13,'bold'))
                lbladrs.place(x=0,y=25)

                lbl1=Label(labelframebottom,text=result[4],font=('times new roman',13,'bold'))
                lbl1.place(x=120,y=25)

                #==========Hotel Name=========
                lblrat=Label(labelframebottom,text='Hotel Name : ',font=('times new roman',13,'bold'))
                lblrat.place(x=0,y=50)
                lbl1=Label(labelframebottom,text=result[5],font=('times new roman',13,'bold'))
                lbl1.place(x=120,y=50)
                #===========Hotel Adress=======
                lbladrs=Label(labelframebottom,text='Hotel Adress :',font=('times new roman',13,'bold'))
                lbladrs.place(x=0,y=75)

                lbl1=Label(labelframebottom,text=result[6],font=('times new roman',13,'bold'))
                lbl1.place(x=120,y=75)
            else:
                messagebox.showwarning('Warning', 'Room not found.')

            conn.close()

        except Exception as e:

            print(f"Error: {e}")
            messagebox.showerror('Error', 'An error occurred while fetching room details.')






if __name__ == '__main__':
    root = Tk()
    obj = room_window(root)
    root.mainloop()