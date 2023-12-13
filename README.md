# Hotel-Management-System
# First You need to write these codes in mysql shell to create the database hotel_management_system
-- 1. hotel_1
CREATE TABLE hotel_1 (
    HotelID INT(11) PRIMARY KEY,
    Name TEXT,
    Address TEXT,
    Rating INT(11),
    `Contact Number` INT(11),
    Revenue INT(11)
);

-- 2. guest
CREATE TABLE guest (
    GuestID INT(11) PRIMARY KEY,
    FirstName VARCHAR(30),
    LastName VARCHAR(30),
    Email VARCHAR(80),
    Phone VARCHAR(20),
    Spent INT(11)
);

-- 3. feedback
CREATE TABLE feedback (
    FeedbackID INT(11) PRIMARY KEY,
    Rating INT(11),
    Comment TEXT,
    HotelID INT(11),
    GuestID INT(11),
    FOREIGN KEY (HotelID) REFERENCES hotel_1(HotelID),
    FOREIGN KEY (GuestID) REFERENCES guest(GuestID)
);

-- 4. myservice
CREATE TABLE myservice (
    Name VARCHAR(45) PRIMARY KEY,
    Price INT(11)
);

-- 5. register
CREATE TABLE register (
    fname VARCHAR(55),
    lname VARCHAR(55),
    contact INT(55) PRIMARY KEY,
    password VARCHAR(55)
);

-- 6. staff
CREATE TABLE staff (
    HotelID INT(11),
    StaffID INT(11) PRIMARY KEY,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Hours INT(10),
    Salary INT(11),
    Position VARCHAR(45),
    DateJoined VARCHAR(11),
    FOREIGN KEY (HotelID) REFERENCES hotel_1(HotelID)
);

-- 7. room
CREATE TABLE room (
    RoomID INT(11) PRIMARY KEY,
    HotelID INT(11),
    RoomNumber VARCHAR(45),
    Type VARCHAR(45),
    Price INT(11),
    RoomCondition VARCHAR(45),
    FOREIGN KEY (HotelID) REFERENCES hotel_1(HotelID)
);

-- 8. service
CREATE TABLE service (
    ServiceID INT(11) PRIMARY KEY,
    Name VARCHAR(45),
    Quantity INT(11),
    Price INT(11),
    HotelID INT(11),
    GuestID INT(11),
    FOREIGN KEY (Name) REFERENCES myservice(Name)
);

-- 9. reservation
CREATE TABLE reservation (
    ReservationID INT(11) PRIMARY KEY,
    GuestID INT(11),
    CheckInDate VARCHAR(45),
    CheckOutDate VARCHAR(45),
    RoomID INT(11),
    HotelID INT(11),
    Days INT(11),
    TotalCost INT(11),
    FOREIGN KEY (GuestID) REFERENCES guest(GuestID),
    FOREIGN KEY (HotelID) REFERENCES hotel_1(HotelID),
    FOREIGN KEY (RoomID) REFERENCES room(RoomID)
);

-- 10. roomservice
CREATE TABLE roomservice (
    OrderID INT(11) PRIMARY KEY,
    ReservationID INT(11),
    ServiceName VARCHAR(45),
    Quantity INT(11),
    TotalPrice INT(11),
    FOREIGN KEY (ReservationID) REFERENCES reservation(ReservationID),
    FOREIGN KEY (ServiceName) REFERENCES myservice(Name)
);
