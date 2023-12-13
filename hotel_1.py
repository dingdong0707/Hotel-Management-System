from tkinter import*
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Hotel_win:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Window')
        self.root.geometry('1295x550+230+220')


        #============================================variables================
        self.var_hotel_id = StringVar()
        x = random.randint(1000,9999)

        self.var_hotel_id.set(str(x))

        #self.var_hotel_id= StringVar()
        self.var_name = StringVar()
        self.var_address = StringVar()
        self.var_rating = StringVar()
        self.var_number = StringVar()
        self.var_revenue= IntVar()
    
        
        #=======================Title===============================
        lbl_title=Label(self.root,text='Hotel Details',font=('times new roman',18,'bold'),bg='sky blue',fg='Black')
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #=========================labelFrame=============================================
        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Hotel Details',font=('times new roman',12,'bold'),padx=2)
        labelFrameleft.place(x=5,y=50,width=425,height=490)

        #===================================== Labels & Entry=============================
        lbl_hotel_ref=Label(labelFrameleft,text='HotelID', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_hotel_id,font=('times new roman',13,'bold'))
        enty_ref.grid(row=0,column=1)


        lbl_hotel_ref=Label(labelFrameleft,text='Name', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=1,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_name,font=('times new roman',13,'bold'))
        enty_ref.grid(row=1,column=1)



        lbl_hotel_ref=Label(labelFrameleft,text='Address', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=2,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_address,font=('times new roman',13,'bold'))
        enty_ref.grid(row=2,column=1)



        lbl_hotel_ref=Label(labelFrameleft,text='Rating', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=3,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_rating,font=('times new roman',13,'bold'))
        enty_ref.grid(row=3,column=1)


        lbl_hotel_ref=Label(labelFrameleft,text='Contact Number', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=4,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_number,font=('times new roman',13,'bold'))
        enty_ref.grid(row=4,column=1)


        lbl_hotel_ref=Label(labelFrameleft,text='Revenue', font=('times new roman',12,'bold'),padx=2,pady=6)
        lbl_hotel_ref.grid(row=5,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=29,textvariable=self.var_revenue,font=('times new roman',13,'bold'))
        enty_ref.grid(row=5,column=1)


        #==================================Buttons in TableFrame==================

        btnHotelRevenue=Button(labelFrameleft,text="Revenue",command=self.calculate_hotel_revenue,font=("arial",12,'bold'),bg="sky blue",width=15)
        btnHotelRevenue.grid(row=6,column=0,padx=1,sticky=W)

        btnHotelRating=Button(labelFrameleft,text="Rating",command=self.calculate_hotel_rating,font=("arial",12,'bold'),bg="sky blue",width=15)
        btnHotelRating.grid(row=6,column=1,padx=1,sticky=W)

        btnShowGuest=Button(labelFrameleft,text="Total Guest",command=self.get_guest_count_for_hotel,font=("arial",12,'bold'),bg="sky blue",width=15)
        btnShowGuest.grid(row=7,column=0,padx=1,sticky=W)

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
        


        
        lbl_search=Label(TableFrame,text='Search By', font=('times new roman',12,'bold'),bg='grey',fg='black')
        lbl_search.grid(row=0,column=0,sticky=W,padx=2)


        self.search_var=StringVar()
        combo_search=ttk.Combobox(TableFrame,textvariable=self.search_var,font=("arial",12,'bold'),width=24,state="readonly")
        combo_search['value']=("HotelID","Rating")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2) 


        self.txt_search = StringVar()
        txtSearch=ttk.Entry(TableFrame,textvariable=self.txt_search,font=("arial",13,'bold'),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(TableFrame,text="Search",command=self.search,font=("arial",12,'bold'),bg="sky blue",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(TableFrame,text="Show All",command=self.fetch_data,font=("arial",12,'bold'),bg="sky blue",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #===========================Show Data Table========================

        det_table=Frame(TableFrame,bd=2,relief=RIDGE)
        det_table.place(x=0,y=50,width=860,height=350)

        Scroll_x=ttk.Scrollbar(det_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(det_table,orient=VERTICAL)

        self.Hotel_details_Table= ttk.Treeview(det_table,column=('HotelID','Name','Address','Rating','Contact Number','Revenue'),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Hotel_details_Table.xview)
        Scroll_y.config(command=self.Hotel_details_Table.yview)

        self.Hotel_details_Table.heading('HotelID',text="HotelID")
        self.Hotel_details_Table.heading('Name',text="Name")
        self.Hotel_details_Table.heading('Address',text="Address")
        self.Hotel_details_Table.heading('Rating',text="Rating")
        self.Hotel_details_Table.heading('Contact Number',text="Contact Number")
        self.Hotel_details_Table.heading('Revenue',text="Revenue")

        self.Hotel_details_Table['show']="headings"
        self.Hotel_details_Table.pack(fill=BOTH,expand=1)


        self.fetch_data()
        self.Hotel_details_Table.bind('<ButtonRelease-1>',self.get_cursor)






##====================adding data==========================
    def add_data(self):
        if self.var_number.get()==''or self.var_hotel_id.get()=='':
              messagebox.showerror('Error','Please provide all the data',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO `hotel_1`(`HotelID`, `Name`, `Address`, `Rating`, `Contact Number`, `Revenue`) VALUES (%s,%s,%s,%s,%s,%s)',(
                    self.var_hotel_id.get(),
                    self.var_name.get(),
                    self.var_address.get(),
                    self.var_rating.get(),
                    self.var_number.get(),
                    self.var_revenue.get()

                ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Good!', 'Data Added!', parent = self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong : {str(es)}', parent = self.root)

         
#=============================to show in the table=====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from hotel_1')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Hotel_details_Table.delete(*self.Hotel_details_Table.get_children())
            for i in rows:
                self.Hotel_details_Table.insert('',END,values=i)
            conn.commit()
        conn.close()
#===================to select a name from the table===================
    def get_cursor(self, event =''):
        cursor_row= self.Hotel_details_Table.focus()
        content = self.Hotel_details_Table.item(cursor_row)
        row = content['values']

        self.var_hotel_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_address.set(row[2]),
        self.var_rating.set(row[3]),
        self.var_number.set(row[4]),
        self.var_revenue.set(row[5])
    
    def update(self):
        if self.var_hotel_id.get()=='':
            messagebox.showerror('Error', 'Please Enter Your ID', parent = self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE `hotel_1` SET `Name`= %s ,`Address`= %s ,`Rating`= %s ,`Contact Number`= %s ,`Revenue`= %s  WHERE `HotelID`= %s ',(
                    
                    self.var_name.get(),
                    self.var_address.get(),
                    self.var_rating.get(),
                    self.var_number.get(),
                    self.var_revenue.get(),
                    self.var_hotel_id.get()

            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Updated', 'Data has been updated successfully', parent = self.root)
    
    def fun_delete(self):
          mdelete = messagebox.askyesno('HEY YOU', 'Do you want to delete this guest', parent = self.root)
          if mdelete>0:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            query = 'DELETE FROM `hotel_1` WHERE  `HotelID`= %s'
            value = (self.var_hotel_id.get(),)
            my_cursor.execute(query,value)
          else:
            if not mdelete:
                return
          conn.commit()
          self.fetch_data()
          conn.close()

    
    def reset(self):
        x = random.randint(1000,9999)
        self.var_hotel_id.set(str(x))

        self.var_name.set(''),
        self.var_address.set(''),
        self.var_rating.set(''),
        self.var_number.set(''),
        self.var_revenue.set(0)


    
    def search (self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()

        new_var1 = str(self.search_var.get())
        new_var2 = str(self.txt_search.get())

        my_cursor.execute(f"select * from hotel_1 where {new_var1} = '{new_var2}'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Hotel_details_Table.delete(*self.Hotel_details_Table.get_children())
            for i in rows:
                self.Hotel_details_Table.insert('',END,values=i)
            conn.commit()
        else:
            messagebox.showerror('Alas!', 'This hotel does not exist',parent = self.root)
        conn.close()




    def calculate_hotel_revenue(self):
        hotel_id = self.var_hotel_id.get()

        try:
            conn = mysql.connector.connect(
                host='localhost', username='root', port='3306', password='', database='hotel management system')
            my_cursor = conn.cursor()

            total_cost_query = "SELECT COALESCE(SUM(TotalCost), 0) FROM reservation WHERE HotelID = %s"
            my_cursor.execute(total_cost_query, (hotel_id,))
            total_cost = my_cursor.fetchone()[0]

  
            price_query = "SELECT COALESCE(SUM(Price), 0) FROM service WHERE HotelID = %s"
            my_cursor.execute(price_query, (hotel_id,))
            price = my_cursor.fetchone()[0]


            total_price_query = "SELECT COALESCE(SUM(TotalPrice), 0) FROM roomservice WHERE ReservationID IN (SELECT ReservationID FROM reservation WHERE HotelID = %s)"
            my_cursor.execute(total_price_query, (hotel_id,))
            total_price = my_cursor.fetchone()[0]

            total_revenue = total_cost + price + total_price
            self.var_revenue.set(total_revenue)

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()

    


    

    def calculate_hotel_rating(self):
        hotel_id = self.var_hotel_id.get()
        try:
            conn = mysql.connector.connect(
                host='localhost', username='root', port='3306', password='', database='hotel management system')
            my_cursor = conn.cursor()

            # Calculate average rating for the specified hotel
            rating_query = "SELECT COALESCE(AVG(Rating), 0) FROM feedback WHERE HotelID = %s"
            my_cursor.execute(rating_query, (hotel_id,))
            average_rating = my_cursor.fetchone()[0]
            self.var_rating.set(average_rating)

            

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()



    def get_guest_count_for_hotel(self):

        hotel_id = self.var_hotel_id.get()


        try:
            conn = mysql.connector.connect(
                host='localhost', username='root', port='3306', password='', database='hotel management system')
            my_cursor = conn.cursor()

            guest_count_query = """
                SELECT COUNT(DISTINCT g.GuestID) AS GuestCount
                FROM guest g
                INNER JOIN reservation r ON g.GuestID = r.GuestID
                WHERE r.HotelID = %s
            """
            
            my_cursor.execute(guest_count_query, (hotel_id,))
            guest_count = my_cursor.fetchone()[0]

            new_val = hotel_id
            new_val2 = guest_count

            messagebox.showinfo('Showing Information', f"Number of Guests in Hotel ID {new_val} Are = {new_val2}", parent = self.root)

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:

            if conn.is_connected():
                my_cursor.close()
                conn.close()









if __name__ == "__main__":
        root=Tk()
        obj=Hotel_win(root)
        root.mainloop()




