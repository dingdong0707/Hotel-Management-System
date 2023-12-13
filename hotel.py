from tkinter import*

# ====================================Importing Other Files====================
from guest import guest_window
from reservation import reservation_window
from hotel_1 import Hotel_win
from service import Service_win
from feedback import Feedback
from room import room_window
from roomservice import roomservice_window
from staff import Staff
from myservice import myservice_window

class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')

        #=========== In Frame ============
        main_frame = Frame(self.root, bd = 4, relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        #============ Menu ============
        lbl_menu = Label(main_frame, text = 'Menu', font=('times new roman',20,'bold'))
        lbl_menu.place(x=0,y=0)
        #=========== Button Frame ============
        btn_frame = Frame(main_frame, bd = 4, relief=RIDGE)
        btn_frame.place(x=0,y=35,width=330,height=330)
        #=========== Buttons ============
        hotel_btn = Button(btn_frame,text='HOTEL', command=self.Hotel_details, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        hotel_btn.grid(row=0,column=0,pady=1)
        room_btn = Button(btn_frame,text='ROOM',command=self.roomdetails, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        room_btn.grid(row=1,column=0,pady=1)
        guest_btn = Button(btn_frame,text='GUEST', command= self.guest_details ,width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        guest_btn.grid(row=2,column=0,pady=1)
        service_btn = Button(btn_frame,text='SERVICE',command= self.service_details, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        service_btn.grid(row=3,column=0,pady=1)

        staff_btn = Button(btn_frame,text='STAFF', command= self.staffdetails, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        staff_btn.grid(row=4,column=0,pady=1)

        reservation_btn = Button(btn_frame, text='RESERVATION', command= self.reservation_details, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        reservation_btn.grid(row=5,column=0,pady=1)

        room_service_order = Button(btn_frame,text='ROOM SERVICE ORDER',command = self.roomservicedetails, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        room_service_order.grid(row=6,column=0,pady=1)

        feedback = Button(btn_frame,text='FEEDBACK',command = self.feedbackdetails, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        feedback.grid(row=7,column=0,pady=1)

        myservice = Button(btn_frame,text='OUR SERVICES', command= self.myservicedetails, width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
        myservice.grid(row=8,column=0,pady=1)

        logout = Button(btn_frame,text='LOGOUT',width=22,bd=0,font=('times new roman',13,'bold'),cursor='hand1')
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


    #=============Feedback button funtion================
    def feedbackdetails(self):
        self.new_window=Toplevel(self.root)
        self.app=Feedback(self.new_window)
    

    #=============Staff button funtion================
    def staffdetails(self):
        self.new_window1=Toplevel(self.root)
        self.app=Staff(self.new_window1)

    #=============Room button funtion================
    def roomdetails(self):
        self.new_window1=Toplevel(self.root)
        self.app=room_window(self.new_window1)

    #=============Room Service button funtion================
    def roomservicedetails(self):
        self.new_window1=Toplevel(self.root)
        self.app=roomservice_window(self.new_window1)


    #=============MyService button funtion================
    def myservicedetails(self):
        self.new_window1=Toplevel(self.root)
        self.app=myservice_window(self.new_window1)

    










if __name__ == '__main__':
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()


