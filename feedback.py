from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector



class Feedback:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')


        #============================================variables================
        self.var_fid = StringVar()
        self.varrating = StringVar()
        self.varcom = StringVar()
        self.varhid= StringVar()
        self.vargid= StringVar()

        #============Label===============#
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Feedack Detail',font=('times new roman',19,'bold'),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #==========label and entries==========#
        #f.id
        lblfeedref=Label(labelframeleft,text='FeedbackID',font=('times new roman',15,'bold'),padx=2,pady=6)
        lblfeedref.grid(row=0,column=0,sticky=W)
        
        entryref=ttk.Entry(labelframeleft,textvar=self.var_fid ,width=17,font=('times new roman',15,'bold'))
        entryref.grid(row=0,column=1,sticky=W)

        #rating
        rating=Label(labelframeleft,text='Rating',font=('times new roman',15,'bold'),padx=2,pady=6)
        rating.grid(row=1,column=0,sticky=W)
        

        comborating=ttk.Combobox(labelframeleft,textvar=self.varrating ,width=27 ,state='readonly',font=('times new roman',15,'bold'))
        comborating['value']=('1','2','3','4','5')
        comborating.current(0)
        comborating.grid(row=1,column=1)

        #comments
        comment=Label(labelframeleft,text='Comment',font=('times new roman',15,'bold'),padx=2,pady=6)
        comment.grid(row=2,column=0,sticky=W)
        
        entrycom=ttk.Entry(labelframeleft,textvar=self.varcom ,width=27,font=('times new roman',15,'bold'))
        entrycom.grid(row=2,column=1)

        #hid
        hid=Label(labelframeleft,text='HotelID',font=('times new roman',15,'bold'),padx=2,pady=6)
        hid.grid(row=3,column=0,sticky=W)
        
        entryhid=ttk.Entry(labelframeleft,textvar=self.varhid,width=27,font=('times new roman',15,'bold'))
        entryhid.grid(row=3,column=1,sticky=W)

        #gid
        gid=Label(labelframeleft,text='GuestID',font=('times new roman',15,'bold'),padx=2,pady=6)
        gid.grid(row=4,column=0,sticky=W)
        
        entrygid=ttk.Entry(labelframeleft,textvar=self.vargid,width=27,font=('times new roman',15,'bold'))
        entrygid.grid(row=4,column=1,sticky=W)

        #====fetch data btn====
        btnfetch=Button(labelframeleft,command=self.fetchid,text='Fetch data',font=('times new roman',11,'bold'),width=9)
        btnfetch.place(x=300,y=4)

        ##============btns=========#
        btnframe=Frame(labelframeleft,bd=2,relief=RIDGE)
        btnframe.place(x=0,y=200,width=411,height=40)


        btnadd=Button(btnframe,text='Add',command=self.adddata,font=('times new roman',11,'bold'),width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnup=Button(btnframe,text='Update',command=self.update ,font=('times new roman',11,'bold'),width=10)
        btnup.grid(row=0,column=1,padx=1)

        btnres=Button(btnframe,text='Reset',command=self.reset ,font=('times new roman',11,'bold'),width=10)
        btnres.grid(row=0,column=2,padx=1)

        btndel=Button(btnframe,text='Delete',command=self.mdelete ,font=('times new roman',11,'bold'),width=10)
        btndel.grid(row=0,column=3,padx=1)

        #======tableframe search system=====#
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details And Search System',font=('times new roman',19,'bold'),padx=2)
        tableframe.place(x=435,y=150,width=860,height=490)

        searchby=Label(tableframe,text='Search By',font=('times new roman',15,'bold'),bg='yellow')
        searchby.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combosearch=ttk.Combobox(tableframe,textvariable=self.search_var,width=24 ,state='readonly',font=('times new roman',15,'bold'))
        combosearch['value']=('FeedbackId','GuestID')
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

        self.feedtab=ttk.Treeview(datatab,column=('F.id','Rating','Comment','hid','gid'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X) 
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.feedtab.xview)      
        scrolly.config(command=self.feedtab.yview) 

        self.feedtab.heading('F.id',text='FeedbackID')
        self.feedtab.heading('Rating',text='Rating')
        self.feedtab.heading('Comment',text='Comment')
        self.feedtab.heading('hid',text='HotelID')
        self.feedtab.heading('gid',text='GuestID')

        self.feedtab['show']='headings'

        self.feedtab.column('F.id',width=100)
        self.feedtab.column('Rating',width=100)
        self.feedtab.column('Comment',width=100)
        self.feedtab.column('hid',width=100)
        self.feedtab.column('gid',width=100)

        self.feedtab.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.feedtab.bind('<ButtonRelease-1>',self.getcursor)

    #=========all data fetch=======
    def fetchid(self):
    
        if self.var_fid.get()=='':
            messagebox.showerror('error','Please enter feedback id',parent=self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            my_cursor = conn.cursor()
# ============================== Use JOIN to fetch hotel information
            query = '''
                SELECT                    
                    Hotel_1.Name,
                    Feedback.Rating,
                    Guest.FirstName,
                    Guest.LastName,
                    Guest.Email,
                    Feedback.GuestID
                FROM 
                    Feedback
                    JOIN Hotel_1 ON Feedback.HotelID = Hotel_1.HotelID
                    JOIN Guest ON Feedback.GuestID = Guest.GuestID
                WHERE 
                    Feedback.FeedbackID = %s
            '''

            
            my_cursor.execute(query, (self.var_fid.get(),))

            result = my_cursor.fetchone()
            if result:
                messagebox.showinfo('Can proceed', 'This id is valid',parent = self.root )
                ##=========the fetch data box=====
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=30,width=250,height=110)
                #++++++=======hotel name===========
                lblname=Label(showdataframe,text='Hotel Name:',font=('times new roman',13,'bold'))
                lblname.place(x=0,y=0)
                lbl=Label(showdataframe,text=result[0],font=('times new roman',13,'bold'))
                lbl.place(x=120,y=0)
                #=========Feedback Rating====
                lbladrs=Label(showdataframe,text='Rating :',font=('times new roman',13,'bold'))
                lbladrs.place(x=0,y=25)

                lbl1=Label(showdataframe,text=result[1],font=('times new roman',13,'bold'))
                lbl1.place(x=120,y=25)

                #++++++Guest Name=========
                lblrat=Label(showdataframe,text='Guest Name :',font=('times new roman',13,'bold'))
                lblrat.place(x=0,y=50)
                lbl1=Label(showdataframe,text=f'{result[2]} {result[3]}',font=('times new roman',13,'bold'))
                lbl1.place(x=120,y=50)
                #===========Guest email=======
                lbladrs=Label(showdataframe,text='Guest Email :',font=('times new roman',13,'bold'))
                lbladrs.place(x=0,y=75)

                lbl1=Label(showdataframe,text=result[4],font=('times new roman',13,'bold'))
                lbl1.place(x=120,y=75)
            else:
                messagebox.showwarning('Warning', 'Feedback not found.',parent=self.root)
            
            conn.commit()
            conn.close()
 
    
    def adddata(self):
        if self.var_fid.get() == '' :
            messagebox.showerror('Operation failed', 'You must enter Feedback ID!',parent = self.root )
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
                mycursor = conn.cursor()
                mycursor.execute('INSERT INTO `feedback`(`FeedbackID`, `Rating`, `Comment`, `HotelID`, `GuestID`) VALUES (%s,%s,%s,%s,%s)',(
                    self.var_fid.get(),
                    self.varrating.get(),
                    self.varcom.get(),                            
                    self.varhid.get(),
                    self.vargid.get()


                ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Feedback Added!', parent = self.root)
            except Exception as es:
                messagebox.showwarning('Sorry', f'Something went wrong : {str(es)}', parent = self.root) 


    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
        mycursor = conn.cursor()
        mycursor.execute('select * from feedback')
        rows = mycursor.fetchall()
        if len(rows)!=0:
            self.feedtab.delete(*self.feedtab.get_children())
            for i in rows:
                self.feedtab.insert('',END,values=i)
            conn.commit()
        conn.close()

    def getcursor(self, event =''):
        cursorrow= self.feedtab.focus()
        content = self.feedtab.item(cursorrow)
        row = content["values"]

        self.var_fid.set(row[0]),
        self.varrating.set(row[1]),
        self.varcom.set(row[2]),
        self.varhid.set(row[3]),
        self.vargid.set(row[4])

    def update(self):
        if self.var_fid.get()=='' or self.varhid.get()=='' or self.vargid.get()=='' :
            messagebox.showerror('Error', 'Please Enter all of the Ids', parent = self.root)
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            mycursor = conn.cursor()
            mycursor.execute('UPDATE `feedback` SET `Rating`= %s ,`Comment`= %s , `HotelID`= %s , `GuestID`= %s WHERE `FeedbackID`= %s ',(
                    
                    
                    self.varrating.get(),
                    self.varcom.get(),
                    self.varhid.get(),
                    self.vargid.get(),
                    self.var_fid.get()


            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update', 'Feedback has been updated successfully', parent = self.root)


    def mdelete(self):
        mdelete = messagebox.askyesno('Hotel Management System', 'Want to delete this feedback ?', parent = self.root)
        if mdelete>0:
            connect = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'hotel management system')
            mycursor = connect.cursor()
            query = 'DELETE FROM `feedback` WHERE  `FeedbackID`= %s'
            value = (self.var_fid.get(),)
            mycursor.execute(query,value)
        else:
            if not mdelete:
                return
        connect.commit()
        self.fetch_data()
        connect.close()

    def reset(self):

        self.var_fid.set('')

        self.varrating.set(''),
        self.varcom.set(''),
        self.varhid.set(''),
        self.vargid.set('')


    def search (self):
        connect = mysql.connector.connect(host = 'localhost', username = 'root', port = '3306', password = '', database = 'Hotel Management System')
        mycursor = connect.cursor()

        newvar1 = str(self.search_var.get())
        newvar2 = str(self.txt_search.get())

        mycursor.execute(f"select * from feedback where {newvar1} = '{newvar2}'")
        rows = mycursor.fetchall()
        if len(rows)!=0:
            self.feedtab.delete(*self.feedtab.get_children())
            for i in rows:
                self.feedtab.insert('',END,values=i)
            connect.commit()
        connect.close()


if __name__ == '__main__':
    root=Tk()
    obj=Feedback(root)
    root.mainloop()