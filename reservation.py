from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
from time import strftime
from datetime import date
from datetime import datetime
import mysql.connector


conn = mysql.connector.connect(host = 'localhost', username = 'root', password = '', database = 'hotel management system')
my_cursor = conn.cursor()
conn.commit()
conn.close()
print('Connection successfully created')


class reservation_window:
    def __init__(self,root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')

        #============================================variables================
        self.var_reservation_id = IntVar()
        x = random.randint(1000,9999)
        self.var_reservation_id.set(str(x))

        self.var_guest_id = StringVar()
        self.var_check_in_date = StringVar()
        self.var_check_out_date = StringVar()
        self.var_room_id = IntVar()
        self.var_hotel_id = IntVar()
        self.var_days = IntVar()
        self.var_total_cost = IntVar()

        #=============labelframe===================
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text='Reservation Details', font=('times new roman',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=410)

        #==================labels_Attributes==============

        #==================reservation_id==============
        lbl_reservation_id = Label(labelframeleft, text = 'ReservationID', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_reservation_id.grid(row=0,column=0, sticky=W)

        lbl_reservation_id_entry = ttk.Entry(labelframeleft, textvariable= self.var_reservation_id, width=30, font=('times new roman', 13, 'bold'))
        lbl_reservation_id_entry.grid(row=0, column=1)

        #==================guest_id==============

        lbl_guest_id = Label(labelframeleft, text = 'GuestID', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_guest_id.grid(row=1,column=0, sticky=W)

        guest_id_entry = ttk.Entry(labelframeleft, textvariable=self.var_guest_id ,width=30, font=('times new roman', 13, 'bold'))
        guest_id_entry.grid(row=1, column=1)

        #==================CheckInDate==============

        lbl_check_in_date = Label(labelframeleft, text = 'CheckInDate', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_check_in_date.grid(row=2,column=0, sticky=W)

        check_in_date_entry = ttk.Entry(labelframeleft, textvariable= self.var_check_in_date, width=30, font=('times new roman', 13, 'bold'))
        check_in_date_entry.grid(row=2, column=1)

        #==================CheckOutDate==============

        lbl_check_out_date = Label(labelframeleft, text = 'CheckOutDate', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_check_out_date.grid(row=3,column=0, sticky=W)

        check_out_date_entry = ttk.Entry(labelframeleft, textvariable= self.var_check_out_date, width=30, font=('times new roman', 13, 'bold'))
        check_out_date_entry.grid(row=3, column=1)

        #==================RoomID==============

        lbl_room_id = Label(labelframeleft, text = 'RoomID', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_room_id.grid(row=4,column=0, sticky=W)

        room_id_entry = ttk.Entry(labelframeleft, textvariable=self.var_room_id, width=30, font=('times new roman', 13, 'bold'))
        room_id_entry.grid(row=4, column=1)

        #==================HotelID==============

        lbl_hotel_id = Label(labelframeleft, text = 'HotelID', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_hotel_id.grid(row=5,column=0, sticky=W)

        hotel_id_entry = ttk.Entry(labelframeleft, textvariable=self.var_hotel_id, width=30, font=('times new roman', 13, 'bold'))
        hotel_id_entry.grid(row=5, column=1)

        #==================Days==============

        lbl_days = Label(labelframeleft, text = 'Days', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_days.grid(row=6,column=0, sticky=W)

        Days_entry = ttk.Entry(labelframeleft, textvariable=self.var_days, width=30, font=('times new roman', 13, 'bold'),state='readonly')
        Days_entry.grid(row=6, column=1)

        #==================total_cost==============

        lbl_total_cost = Label(labelframeleft, text = 'TotalCost', font=('times new roman',12,'bold'), padx=2, pady=6)
        lbl_total_cost.grid(row=7,column=0, sticky=W)

        total_cost_entry = ttk.Entry(labelframeleft, textvariable=self.var_total_cost, width=30, font=('times new roman', 13, 'bold'), state='readonly')
        total_cost_entry.grid(row=7, column=1)










        #====button frame===
        button_frame = Frame(labelframeleft, bd =2, relief=RIDGE)
        button_frame.place(x=0,y=300,width=410,height=89)

        #=========buttons========
        add_button = Button(button_frame, command=self.add_data ,text='ADD', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=8)
        add_button.grid(row=0, column=0)

        update_button = Button(button_frame, command= self.update, text='UPDATE', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=9)
        update_button.grid(row=0, column=1)

        delete_button = Button(button_frame, command=self.fun_delete,  text='DELETE', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=11)
        delete_button.grid(row=0, column=2)

        reset_button = Button(button_frame, command=self.reset, text='RESET', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=9)
        reset_button.grid(row=0, column=3)

        number_of_days_button = Button(button_frame, command=self.number_of_days, text='DAYS', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=8)
        number_of_days_button.grid(row=1, column=0)

        get_reservation_info_button = Button(button_frame,command=self.get_reservation_info, text='INFO', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=9)
        get_reservation_info_button.grid(row=1, column=1)


        total_price_button = Button(button_frame, command=self.calculate_total, text='BILL', font=('times new roman', 13, 'bold'),padx=2, pady=6, width=11)
        total_price_button.grid(row=1, column=2)



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
        combo_search['value']=('GuestID', 'RoomId', 'ReservationID', 'Days')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=6)

        
        #=========search entry space=======

        self.txt_search = StringVar()
        search_by_entry = ttk.Entry(tableframe, textvariable=self.txt_search, width=29, font=('times new roman', 13, 'bold'))
        search_by_entry.grid(row=0, column=2, padx=6)
        
        #=========search button=======
        search_button = Button(tableframe, command=self.search,  text='SEARCH', font=('times new roman', 13, 'bold'),padx=2, pady=0, width=8)
        search_button.grid(row=0, column=3, padx=6)
        
        #=========show all button=======
        show_all_button = Button(tableframe, command=self.fetch_data , text='SHOW ALL', font=('times new roman', 13, 'bold'),padx=2, pady=0, width=8)
        show_all_button.grid(row=0, column=4, padx=6)

        #==========================Show Data Frame======================
        show_data_frame = Frame(tableframe, bd =2, relief=RIDGE)
        show_data_frame.place(x=2,y=50,width=850,height=600)
        #===================================== scroll bar ============================
        scroll_bar_x = ttk.Scrollbar(show_data_frame,orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(show_data_frame,orient=VERTICAL)
        #========= for scrolling ==============
        self.reservation_details_table = ttk.Treeview(show_data_frame, columns = ('ReservationID', 'GuestID', 'CheckInDate', 'CheckOutDate', 'RoomID', 'HotelID', 'Days','TotalCost'), xscrollcommand=scroll_bar_x, yscrollcommand=scroll_bar_y)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)
        #====where to config=====
        scroll_bar_x.config(command=self.reservation_details_table.xview)
        scroll_bar_y.config(command=self.reservation_details_table.yview)
        #======================================================Creating Heading===============
        self.reservation_details_table.heading('ReservationID', text='ReservationID')
        self.reservation_details_table.heading('GuestID', text='GuestID')
        self.reservation_details_table.heading('CheckInDate', text='CheckInDate')
        self.reservation_details_table.heading('CheckOutDate', text='CheckOutDate')
        self.reservation_details_table.heading('RoomID', text='RoomID')
        self.reservation_details_table.heading('HotelID', text='HotelID')
        self.reservation_details_table.heading('Days', text='Days')
        self.reservation_details_table.heading('TotalCost', text='TotalCost')
        self.reservation_details_table['show'] = 'headings'  
        #=================adjusting width ===========
        self.reservation_details_table.column('ReservationID', width=100)
        self.reservation_details_table.column('GuestID', width=100)
        self.reservation_details_table.column('CheckInDate', width=100)
        self.reservation_details_table.column('CheckOutDate', width=100)
        self.reservation_details_table.column('RoomID', width=100)
        self.reservation_details_table.column('HotelID', width=100)
        self.reservation_details_table.column('Days', width=100)
        self.reservation_details_table.column('TotalCost', width=100)
        self.reservation_details_table.pack(fill=BOTH, expand=1)  
        self.reservation_details_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

        

        










    #=======================================to a add a data=============================
    def add_data(self):
        if self.var_check_out_date.get() == '' or self.var_check_in_date.get() == '':
            messagebox.showerror('STUPID!', 'All Fields Are Required!', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    username='root',
                    port='3306',
                    password='',
                    database='hotel management system'
                )
                my_cursor = conn.cursor()

                # ========== Check if the RoomCondition is 'Vacant' before adding the reservation
                room_condition_query = 'SELECT `RoomCondition` FROM `room` WHERE `RoomID` = %s'
                room_condition_values = (self.var_room_id.get(),)
                my_cursor.execute(room_condition_query, room_condition_values)
                room_condition_info = my_cursor.fetchone()

                if room_condition_info and room_condition_info[0] == 'Vacant':
                    #=============== Update RoomCondition to 'Booked'
                    update_query = 'UPDATE `room` SET `RoomCondition` = %s WHERE `RoomID` = %s'
                    update_values = ('Booked', self.var_room_id.get())
                    my_cursor.execute(update_query, update_values)

                    # =============== Insert reservation data
                    insert_query = '''
                        INSERT INTO `reservation` (`ReservationID`, `GuestID`, `CheckInDate`, `CheckOutDate`, 
                                                `RoomID`, `HotelID`, `Days`, `TotalCost`)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    '''
                    insert_values = (
                        self.var_reservation_id.get(),
                        self.var_guest_id.get(),
                        self.var_check_in_date.get(),
                        self.var_check_out_date.get(),
                        self.var_room_id.get(),
                        self.var_hotel_id.get(),
                        self.var_days.get(),
                        self.var_total_cost.get()
                    )
                    my_cursor.execute(insert_query, insert_values)

                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo('GENIUS!', 'Reservation Added!', parent=self.root)
                else:
                    messagebox.showerror('Error', 'Room is not vacant. Cannot add reservation.', parent=self.root)

                conn.close()

            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong: {str(es)}', parent=self.root)





    #=============================to show in the table=====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from reservation')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.reservation_details_table.delete(*self.reservation_details_table.get_children())
            for i in rows:
                self.reservation_details_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    #===================to select a name from the table===================
    def get_cursor(self, event =''):
        cursor_row= self.reservation_details_table.focus()
        content = self.reservation_details_table.item(cursor_row)
        row = content['values']

        self.var_reservation_id.set(row[0]),
        self.var_guest_id.set(row[1]),
        self.var_check_in_date.set(row[2]),
        self.var_check_out_date.set(row[3]),
        self.var_room_id.set(row[4]),
        self.var_hotel_id.set(row[5]),
        self.var_days.set(row[6]),
        self.var_total_cost.set(row[7]),







    def update(self):
        if self.var_room_id.get() == '':
            messagebox.showerror('Error', 'Please Enter Room ID', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    username='root',
                    port='3306',
                    password='',
                    database='hotel management system'
                )
                my_cursor = conn.cursor()

                # Fetch current RoomCondition and RoomID before updating the reservation
                room_info_query = 'SELECT `RoomID`, `RoomCondition` FROM `room` WHERE `RoomID` = %s'
                room_info_values = (self.var_room_id.get(),)
                my_cursor.execute(room_info_query, room_info_values)
                room_info = my_cursor.fetchone()

                if room_info:
                    room_id, current_condition = room_info

                    # ==================Check if the RoomCondition is 'Vacant' before updating the reservation
                    if current_condition == 'Vacant':
                        # =====================Update RoomCondition to 'Booked'
                        update_room_query = 'UPDATE `room` SET `RoomCondition` = %s WHERE `RoomID` = %s'
                        update_room_values = ('Booked', room_id)
                        my_cursor.execute(update_room_query, update_room_values)

                        # ===================Update RoomCondition to 'Vacant' for the previous room (if it exists)
                        previous_room_id_query = 'SELECT `RoomID` FROM `reservation` WHERE `ReservationID` = %s'
                        previous_room_id_values = (self.var_reservation_id.get(),)
                        my_cursor.execute(previous_room_id_query, previous_room_id_values)
                        previous_room_id = my_cursor.fetchone()

                        if previous_room_id:
                            previous_room_id = previous_room_id[0]
                            update_previous_room_query = 'UPDATE `room` SET `RoomCondition` = %s WHERE `RoomID` = %s'
                            update_previous_room_values = ('Vacant', previous_room_id)
                            my_cursor.execute(update_previous_room_query, update_previous_room_values)

                        # ========================Update reservation
                        update_reservation_query = '''
                            UPDATE `reservation` SET 
                                `GuestID`= %s,
                                `CheckInDate`= %s,
                                `CheckOutDate`= %s,
                                `RoomID`= %s,
                                `HotelID`= %s,
                                `Days`= %s,
                                `TotalCost`= %s
                            WHERE `ReservationID`= %s
                        '''
                        update_reservation_values = (
                            self.var_guest_id.get(),
                            self.var_check_in_date.get(),
                            self.var_check_out_date.get(),
                            self.var_room_id.get(),
                            self.var_hotel_id.get(),
                            self.var_days.get(),
                            self.var_total_cost.get(),
                            self.var_reservation_id.get()
                        )
                        my_cursor.execute(update_reservation_query, update_reservation_values)

                        conn.commit()
                        self.fetch_data()
                        messagebox.showinfo('Update', 'Customer Details has been updated successfully', parent=self.root)

                    else:
                        messagebox.showerror('Error', 'Room is not vacant. Cannot update reservation.', parent=self.root)
                        
                else:
                    messagebox.showwarning('Warning', 'Room not found.', parent=self.root)

            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror('Error', 'An error occurred while updating the reservation.', parent=self.root)

            finally:
                conn.close()


            

    
    def fun_delete(self):
        mdelete = messagebox.askyesno('HEY YOU', 'Do you want to delete this reservation', parent=self.root)

        if mdelete:
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    username='root',
                    port='3306',
                    password='',
                    database='hotel management system'
                )

                my_cursor = conn.cursor()

                # Fetch RoomID before deleting the reservation
                room_id_query = 'SELECT `RoomID` FROM `reservation` WHERE `ReservationID` = %s'
                room_id_values = (self.var_reservation_id.get(),)
                my_cursor.execute(room_id_query, room_id_values)
                room_id_info = my_cursor.fetchone()

                if room_id_info:
                    room_id = room_id_info[0]

                    # ======Delete the reservation=====
                    delete_query = 'DELETE FROM `reservation` WHERE `ReservationID` = %s'
                    delete_values = (self.var_reservation_id.get(),)
                    my_cursor.execute(delete_query, delete_values)

                    # =======Update RoomCondition to 'Vacant'======
                    update_query = 'UPDATE `room` SET `RoomCondition` = %s WHERE `RoomID` = %s'
                    update_values = ('Vacant', room_id)
                    my_cursor.execute(update_query, update_values)

                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo('Success', 'Reservation deleted successfully.', parent=self.root)

                else:
                    messagebox.showwarning('Warning', 'Reservation not found.', parent=self.root)

            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror('Error', 'An error occurred while deleting the reservation.', parent=self.root)

            finally:
                conn.close()

    
    def reset(self):

        x = random.randint(1000,9999)
        self.var_reservation_id.set(str(x))

        self.var_guest_id.set(''),
        self.var_check_in_date.set(''),
        self.var_check_out_date.set(''),
        self.var_room_id.set(0),
        self.var_hotel_id.set(0),
        self.var_days.set('')
        self.var_total_cost.set('')


    
    def search (self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()

        new_var1 = str(self.search_var.get())
        new_var2 = str(self.txt_search.get())

        my_cursor.execute(f"select * from reservation where {new_var1} = '{new_var2}'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.reservation_details_table.delete(*self.reservation_details_table.get_children())
            for i in rows:
                self.reservation_details_table.insert('',END,values=i)
            conn.commit()
        else:
            messagebox.showerror('Alas!', 'This reservation does not exist',parent = self.root)

        conn.close()





    def number_of_days(self):
        try:
            inDate = self.var_check_in_date.get()
            outDate = self.var_check_out_date.get()
            inDate = datetime.strptime(inDate, '%d/%m/%Y')
            outDate = datetime.strptime(outDate, '%d/%m/%Y')
            self.var_days.set(abs(outDate-inDate).days)

        except Exception as e:
            messagebox.showerror('Error', 'Try maintaining the format d/m/Y for CheckIn and CheckOut')




    def calculate_total(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                port='3306',
                password='',
                database='hotel management system'
            )


            my_cursor = conn.cursor()

            reservation_id = self.var_reservation_id.get()
            room_id = self.var_room_id.get()
            days = self.var_days.get()

            room_price_query = 'SELECT `Price` FROM `Room` WHERE `RoomID` = %s'
            room_price_values = (room_id,)
            my_cursor.execute(room_price_query, room_price_values)
            room_price_info = my_cursor.fetchone()

            if room_price_info:
                room_price = room_price_info[0]

                total_cost = days * room_price

                update_query = 'UPDATE `Reservation` SET `TotalCost` = %s WHERE `ReservationID` = %s'
                update_values = (total_cost, reservation_id)
                my_cursor.execute(update_query, update_values)

                conn.commit()
                
                self.var_total_cost.set(total_cost)

                messagebox.showinfo('Success', 'Total cost calculated and stored successfully.', parent= self.root)
            else:
                messagebox.showwarning('Warning', 'Room not found or invalid RoomID.',parent= self.root)
            
            

            conn.close()

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror('Error', 'An error occurred while calculating the total cost.',parent= self.root)





    

    def get_reservation_info(self):

        reservation_id = self.var_reservation_id.get()
        try:

            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                port='3306',
                password='',
                database='hotel management system'
            )

            my_cursor = conn.cursor()

            query_1 = f"SELECT ReservationID FROM reservation WHERE ReservationID = '{reservation_id}';"
            my_cursor.execute(query_1)
            result_1 = my_cursor.fetchone()

            if  result_1:
                
                # ============================== Use JOIN to fetch reservation details along with guest and room information
                query = '''
                    SELECT 
                        Reservation.ReservationID,
                        Guest.FirstName,
                        Guest.LastName,
                        Room.RoomNumber,
                        Room.Type,
                        Room.Price
                        
                    FROM 
                        Reservation
                        JOIN Guest ON Reservation.GuestID = Guest.GuestID
                        JOIN Room ON Reservation.RoomID = Room.RoomID
                    WHERE 
                        Reservation.ReservationID = %s
                '''


                my_cursor.execute(query, (reservation_id,))

                result = my_cursor.fetchone()

                if result:
                    
                    messagebox.showinfo('Can proceed', 'This id is valid',parent = self.root )

                    #=======creating label============
                    labelframebottom = LabelFrame(self.root,bd=2,relief=RIDGE,text='Informations', font=('times new roman',12,'bold'))
                    labelframebottom.place(x=5,y=470,width=425,height=150)
                    
                    #==============reservation id===========
                    lblname=Label(labelframebottom,text='Reservation ID:',font=('times new roman',13,'bold'))
                    lblname.place(x=0,y=0)
                    lbl=Label(labelframebottom,text=result[0],font=('times new roman',13,'bold'))
                    lbl.place(x=150,y=0)
                    #=========guest name====
                    lbladrs=Label(labelframebottom,text='Guest Name :',font=('times new roman',13,'bold'))
                    lbladrs.place(x=0,y=25)

                    lbl1=Label(labelframebottom,text=f'{result[1]} {result[2]}',font=('times new roman',13,'bold'))
                    lbl1.place(x=150,y=25)

                    #==========room number=========
                    lblrat=Label(labelframebottom,text='Room Number : ',font=('times new roman',13,'bold'))
                    lblrat.place(x=0,y=50)
                    lbl1=Label(labelframebottom,text=result[3],font=('times new roman',13,'bold'))
                    lbl1.place(x=150,y=50)
                    #===========room type=======
                    lbladrs=Label(labelframebottom,text='Room Type :',font=('times new roman',13,'bold'))
                    lbladrs.place(x=0,y=75)

                    lbl1=Label(labelframebottom,text=result[4],font=('times new roman',13,'bold'))
                    lbl1.place(x=150,y=75)
                    #===========room price=======
                    lbladrs=Label(labelframebottom,text='Room Price :',font=('times new roman',13,'bold'))
                    lbladrs.place(x=0,y=100)

                    lbl1=Label(labelframebottom,text=result[5],font=('times new roman',13,'bold'))
                    lbl1.place(x=150,y=100)
                else:
                    messagebox.showwarning('Warning', 'Reservation ID not found.', parent = self.root)
            else:
                message = f"Reservation with ID {reservation_id} does not exist."
                messagebox.showinfo("Result", message, parent = self.root)
            
            conn.commit()
            conn.close()

        except Exception as e:

            print(f"Error: {e}")
            messagebox.showerror('Error', 'An error occurred while fetching reservation details.')


    



  


    




if __name__ == '__main__':
    root = Tk()
    obj = reservation_window(root)
    root.mainloop()
