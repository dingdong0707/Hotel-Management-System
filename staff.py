from tkinter import*
from tkinter import ttk
from tkinter import messagebox
# from datetime import datetime
# from time import strptime
import mysql.connector




class Staff:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')

        #==========variavles==============
        self.varhid = StringVar()
        self.var_sid = StringVar()
        # x = random.randint(1000,9999)

        # self.var_fid.set(str(x))

        self.varfn = StringVar()
        self.varln = StringVar()
        self.varhr = StringVar()
        self.varsal =StringVar()
        self.varpos = StringVar()
        self.vardate= StringVar()
        

        #============Label===============#
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Staff Details',font=('times new roman',19,'bold'),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #==========label and entries==========#
        #st.id
        lblstref=Label(labelframeleft,text='StaffID',font=('times new roman',15,'bold'),padx=2,pady=6)
        lblstref.grid(row=1,column=0,sticky=W)
        
        entryref=ttk.Entry(labelframeleft,textvar=self.var_sid,width=27,font=('times new roman',15,'bold'))
        entryref.grid(row=1,column=1)

        #firstname
        fname=Label(labelframeleft,text='FirstName',font=('times new roman',15,'bold'),padx=2,pady=6)
        fname.grid(row=2,column=0,sticky=W)
        
        entryfn=ttk.Entry(labelframeleft,textvar=self.varfn,width=27,font=('times new roman',15,'bold'))
        entryfn.grid(row=2,column=1)


        #lastname
        lname=Label(labelframeleft,text='LastName',font=('times new roman',15,'bold'),padx=2,pady=6)
        lname.grid(row=3,column=0,sticky=W)
        
        entryln=ttk.Entry(labelframeleft,textvar=self.varln,width=27,font=('times new roman',15,'bold'))
        entryln.grid(row=3,column=1)

        #hour
        lhr=Label(labelframeleft,text='Hours',font=('times new roman',15,'bold'),padx=2,pady=6)
        lhr.grid(row=4,column=0,sticky=W)
        
        entryhr=ttk.Entry(labelframeleft,textvar=self.varhr,width=27,font=('times new roman',15,'bold'))
        entryhr.grid(row=4,column=1)       

        #position
        position=Label(labelframeleft,text='Position',font=('times new roman',15,'bold'),padx=2,pady=6)
        position.grid(row=5,column=0,sticky=W)
        
        entrypos=ttk.Entry(labelframeleft,textvar=self.varpos,width=27,font=('times new roman',15,'bold'))
        entrypos.grid(row=5,column=1)

        #salary
        salary=Label(labelframeleft,text='Salary',font=('times new roman',15,'bold'),padx=2,pady=6)
        salary.grid(row=6,column=0,sticky=W)
        
        entrysal=ttk.Entry(labelframeleft,textvar=self.varsal,width=27,font=('times new roman',15,'bold'))
        entrysal.grid(row=6,column=1)

        #date
        date=Label(labelframeleft,text='DateJoined',font=('times new roman',15,'bold'),padx=2,pady=6)
        date.grid(row=7,column=0,sticky=W)
        
        entrydate=ttk.Entry(labelframeleft,textvar=self.vardate,width=27,font=('times new roman',15,'bold'))
        entrydate.grid(row=7,column=1)

        #hotelid(fk)
        fk=Label(labelframeleft,text='HotelID',font=('times new roman',15,'bold'),padx=2,pady=6)
        fk.grid(row=0,column=0,sticky=W)
        
        entryhid=ttk.Entry(labelframeleft,textvar=self.varhid,width=17,font=('times new roman',15,'bold'))
        entryhid.grid(row=0,column=1,sticky=W)  

        ###===fetch data=====
        #       
        btnfetch=Button(labelframeleft,command=self.fetchid ,text='Check data',font=('times new roman',11,'bold'),width=9)
        btnfetch.place(x=327,y=4)

        ##============btns=========#
        btnframe=Frame(labelframeleft,bd=2,relief=RIDGE)
        btnframe.place(x=0,y=400,width=411,height=40)


        btnadd=Button(btnframe,text='Add',command=self.adddata ,font=('times new roman',11,'bold'),width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnup=Button(btnframe,command=self.update ,text='Update',font=('times new roman',11,'bold'),width=10)
        btnup.grid(row=0,column=1,padx=1)

        btnres=Button(btnframe,command=self.reset ,text='Reset',font=('times new roman',11,'bold'),width=10)
        btnres.grid(row=0,column=2,padx=1)

        btndel=Button(btnframe,command=self.delete ,text='Delete',font=('times new roman',11,'bold'),width=10)
        btndel.grid(row=0,column=3,padx=1)

        #salary button====
        btnsal=Button(labelframeleft,text='Salary',command=self.salary,font=('times new roman',11,'bold'),width=10)
        btnsal.grid(row=9,column=0,padx=1,sticky=W)

        #======tableframe=====#
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details And Search System',font=('times new roman',19,'bold'),padx=2)
        tableframe.place(x=435,y=150,width=860,height=490)

        searchby=Label(tableframe,text='Search By',font=('times new roman',15,'bold'),bg='yellow')
        searchby.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combosearch=ttk.Combobox(tableframe,textvariable=self.search_var,width=24 ,state='readonly',font=('times new roman',15,'bold'))
        combosearch['value']=('StaffID','HotelID')
        #combosearch.current(0)
        combosearch.grid(row=0,column=1)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe,textvariable=self.txt_search,width=27,font=('times new roman',15,'bold'))
        txtsearch.grid(row=0,column=2,padx=2)  

        btnsearch=Button(tableframe,command=self.search,text='Search',font=('times new roman',11,'bold'),width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(tableframe,command=self.fetch_data,text='Show All',font=('times new roman',11,'bold'),width=10)
        btnshowall.grid(row=0,column=4,padx=1) 

        #=============show data table=========
        datatab=Frame(tableframe,bd=2,relief=RIDGE)
        datatab.place(x=0,y=50,width=860,height=250) 

        scrollx=ttk.Scrollbar(datatab,orient=HORIZONTAL) 
        scrolly=ttk.Scrollbar(datatab,orient=VERTICAL)

        self.stafftab=ttk.Treeview(datatab,column=('fk' ,'s.id','fn','ln','hr','sal','pos','date'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X) 
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.stafftab.xview)      
        scrolly.config(command=self.stafftab.yview) 

        self.stafftab.heading('fk',text='HotelID')
        self.stafftab.heading('s.id',text='StaffID')
        self.stafftab.heading('fn',text='FirstName')
        self.stafftab.heading('ln',text='LastName')
        self.stafftab.heading('hr',text='Hours')
        self.stafftab.heading('sal',text='Salary')
        self.stafftab.heading('pos',text='Position')
        self.stafftab.heading('date',text='DateJoined')
        
        self.stafftab['show']='headings'

        self.stafftab.column('fk',width=100)
        self.stafftab.column('s.id',width=100)
        self.stafftab.column('fn',width=100)
        self.stafftab.column('ln',width=100)
        self.stafftab.column('hr',width=100)
        self.stafftab.column('sal',width=100)
        self.stafftab.column('pos',width=100)
        self.stafftab.column('date',width=100) 

        self.stafftab.pack(fill=BOTH,expand=1)

        self.fetch_data()
        self.stafftab.bind('<ButtonRelease-1>',self.get_cursor)

    #=========all data fetch=======
    def fetchid(self):
        if self.var_sid.get()=='' :
            messagebox.showerror('error','Please enter staff id',parent=self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()

# ============================== Use JOIN to fetch hotel information
            query = '''
                SELECT                    
                    Hotel_1.Name,
                    Hotel_1.Address,
                    Hotel_1.Rating,
                    Staff.FirstName,
                    Staff.LastName
                FROM 
                    Staff
                    JOIN Hotel_1 ON Staff.HotelID = Hotel_1.HotelID
                WHERE 
                    Staff.StaffID = %s
            '''
            my_cursor.execute(query, (self.var_sid.get(),))

            result = my_cursor.fetchone()
            if result:
                messagebox.showinfo('Can proceed', 'This id is valid',parent = self.root )
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=30,width=250,height=110)
                lblname=Label(showdataframe,text='Hotel Name:',font=('times new roman',13,'bold'))
                lblname.place(x=0,y=0)
                lbl=Label(showdataframe,text=result[0],font=('times new roman',13,'bold'))
                lbl.place(x=120,y=0)
                #=========address====
                lbladrs=Label(showdataframe,text='Hotel Address :',font=('times new roman',13,'bold'))
                lbladrs.place(x=0,y=25)

                lbl1=Label(showdataframe,text=result[1],font=('times new roman',13,'bold'))
                lbl1.place(x=120,y=25)

                #++++++rating=========
                lblrat=Label(showdataframe,text='Hotel Rating :',font=('times new roman',13,'bold'))
                lblrat.place(x=0,y=50)
                lbl1=Label(showdataframe,text=result[2],font=('times new roman',13,'bold'))
                lbl1.place(x=120,y=50)
                #===========staff name=======
                lbladrs=Label(showdataframe,text='Staff Name :',font=('times new roman',13,'bold'))
                lbladrs.place(x=0,y=75)

                lbl1=Label(showdataframe,text=f'{result[3]} {result[4]}',font=('times new roman',13,'bold'))
                lbl1.place(x=120,y=75)
            else:
                messagebox.showwarning('Warning', 'Staff not found.')
            
            conn.commit()
            conn.close()


    #======calculate salary===
    def salary(self):
 
        q1=float(self.varhr.get())
        #q2=float(200)
        total=str('%.2f'%((q1)*200))
        self.varsal.set(total)

        #==========add data============

    def adddata(self):
        if self.var_sid.get() == '' or self.varhid.get()=='':
            messagebox.showerror('Error', 'All Fields Are Required!',parent = self.root )
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO `staff`(`HotelID`,`StaffID`, `FirstName`, `LastName`, `Hours`,`Salary` ,`Position`, `DateJoined`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.varhid.get(),
                    self.var_sid.get(),
                    self.varfn.get(),
                    self.varln.get(),
                    self.varhr.get(),
                    self.varsal.get(),
                    self.varpos.get(),
                    self.vardate.get()
                    

                ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success', 'Staff Added!', parent = self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong : {str(es)}', parent = self.root)


#=============================to show table=====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from staff')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.stafftab.delete(*self.stafftab.get_children())
            for i in rows:
                self.stafftab.insert('',END,values=i)
            conn.commit()
        conn.close()

#===================to select a name from the table===================
    def get_cursor(self, event =''):
        cursor_row= self.stafftab.focus()
        content = self.stafftab.item(cursor_row)
        row = content['values']

        self.varhid.set(row[0]),
        self.var_sid.set(row[1]),
        self.varfn.set(row[2]),
        self.varln.set(row[3]),
        self.varhr.set(row[4]),
        self.varsal.set(row[5]),
        self.varpos.set(row[6]),
        self.vardate.set(row[7])

#=======update======
    def update(self):
        if self.var_sid.get()=='':
            messagebox.showerror('Error', 'Please Enter Staff id', parent = self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE `staff` SET `HotelID` =%s ,`FirstName`= %s ,`LastName`= %s ,`Hours`= %s,`Salary`= %s ,`Position`= %s ,`DateJoined`= %s  WHERE `StaffID`= %s ',(
                    
                    self.varhid.get(),
                    self.varfn.get(),
                    self.varln.get(),
                    self.varhr.get(),
                    self.varsal.get(),
                    self.varpos.get(),
                    self.vardate.get(),
                    self.var_sid.get()

            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update', 'Staff Details has been updated successfully', parent = self.root)

    def delete(self):
        mdelete = messagebox.askyesno('Warning', 'Do you want to delete this guest', parent = self.root)
        if mdelete>0:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
            query = 'DELETE FROM `staff` WHERE  `StaffID`= %s'
            value = (self.var_sid.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    
    def reset(self):
        self.stafftab.set(''),
        self.varhid.set(''),
        self.varfn.set(''),
        self.varln.set(''),
        self.varhr.set(''),
        self.varsal.set(''),
        self.varpos.set(''),
        self.vardate.set('')


    
    def search (self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        my_cursor = conn.cursor()

        new_var1 = str(self.search_var.get())
        new_var2 = str(self.txt_search.get())

        my_cursor.execute(f"select * from staff where {new_var1} = '{new_var2}'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.stafftab.delete(*self.stafftab.get_children())
            for i in rows:
                self.stafftab.insert('',END,values=i)
            conn.commit()
        conn.close()


if __name__ == '__main__':
    root=Tk()
    obj=Staff(root)
    root.mainloop()