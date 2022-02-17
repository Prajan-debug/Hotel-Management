import pymysql


def connect():
    global con, cursor
    con = pymysql.connect(host="localhost", user="root",
                          password="Prajan@123", database="python")
    cursor = con.cursor()


def closedb():
    con.close()
    cursor.close()


class Hotel_Management:

    def __init__(self, Total='', room_rent=0, Game=0, Food=0, Laundry=0, additional_charges=1800, name='', address='', check_in_date='', check_out_date='', room_no=101):

        print("\n*****WELCOME TO REMI *****\n")

        self.Total = Total
        self.Food = Food
        self.Laundry = Laundry
        self.Game = Game
        self.room_rent = room_rent
        self.additional_charges = additional_charges
        self.name = name
        self.address = address
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_no = room_no


    def inputdata(self):
        self.name = input("\nEnter your name: ")
        self.address = input("\nEnter your address: ")
        self.check_in_date = input("\nEnter your check in date: ")
        self.check_out_date = input("\nEnter your checkout date: ")
        print("Your room no : ", self.room_no, "\n")


# Calculating Room Rent

    def roomrent(self):

        print("We have the following rooms for you:")

        print("1. 6000 Per Night---|")

        print("2. 5000 Per Night---|")

        print("3. 4000 Per Night---|")

        print("4. 3000 Per Night---|")

        c = int(input("Enter Your Choice Please---: "))

        n = int(input("Enter the number of Days you want to stay: "))

        if(c == 1):

            print("You have selected room type 1")

            self.room_rent = 6000*n

        elif (c == 2):

            print("You have selected room type 2")

            self.room_rent = 5000*n

        elif (c == 3):

            print("You have selected room type 3")

            self.room_rent = 4000*n

        elif (c == 4):
            print("You have selected room type 4")

            self.room_rent = 3000*n

        else:
            print("Please choose a room")

        print("Your room rent is =", self.room_rent, "\n")

# Food Billing

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.water--Rs20", "2.tea--Rs10", "3.breakfast combo-Rs90",
              "4.lunch--Rs110", "5.dinner--Rs150", "6.Exit")

        while (1):

            c = int(input("Enter your choice:"))

            if (c == 1):
                q = int(input("Enter the quantity:"))
                self.Food = self.Food+20*q

            elif (c == 2):
                q = int(input("Enter the quantity:"))
                self.Food = self.Food+10*q

            elif (c == 3):
                q = int(input("Enter the quantity:"))
                self.Food = self.Food+90*q

            elif (c == 4):
                q = int(input("Enter the quantity:"))
                self.Food = self.Food+110*q

            elif (c == 5):
                q = int(input("Enter the quantity:"))
                self.Food = self.Food+150*q

            elif (c == 6):
                break
            else:
                print("Invalid option")

        print("Total food Cost= Rs ", self.Food, "\n")

# Laundry Billing

    def laundrybill(self):
        print("******LAUNDRY MENU*******")

        print("1.Shorts----->Rs3", "2.Trousers----->Rs4", "3.Shirt--->Rs5",
              "4.Jeans---->Rs6", "5.Saree--->Rs8", "6.Exit")

        while (1):

            e = int(input("Enter your choice:"))

            if (e == 1):
                q = int(input("Enter the quantity:"))
                self.Laundry = self.Laundry+3*q

            elif (e == 2):
                q = int(input("Enter the quantity:"))
                self.Laundry = self.Laundry+4*q

            elif (e == 3):
                q = int(input("Enter the quantity:"))
                self.Laundry = self.Laundry+5*q

            elif (e == 4):
                q = int(input("Enter the quantity:"))
                self.Laundry = self.Laundry+6*q

            elif (e == 5):
                q = int(input("Enter the quantity:"))
                self.Laundry = self.Laundry+8*q
            elif (e == 6):
                break
            else:

                print("Invalid option")

        print("Total Laundary Cost=Rs", self.Laundry, "\n")

# Game Billing

    def gamebill(self):
        print("******GAME MENU*******")

        print("1.Table tennis----->Rs400", "2.Bowling----->Rs700", "3.Turf--->Rs1500",
              "4.Video games---->Rs300", "5.Pool--->Rs 600", "6.Exit")

        while (1):

            g = int(input("Enter your choice:"))

            if (g == 1):
                h = int(input("No. of hours:"))
                self.Game = self.Game+400*h

            elif (g == 2):
                h = int(input("No. of hours:"))
                self.Game = self.Game+700*h

            elif (g == 3):
                h = int(input("No. of hours:"))
                self.Game = self.Game+1500*h

            elif (g == 4):
                h = int(input("No. of hours:"))
                self.Game = self.Game+300*h

            elif (g == 5):
                h = int(input("No. of hours:"))
                self.Game = self.Game+600*h
            elif (g == 6):
                break

            else:

                print("Invalid option")

        print("Total Game Bill=Rs", self.Game, "\n")

# To display all the information entered by the user

    def display(self):
        print("******HOTEL BILL******")
        print("Customer details")
        print("Room no.", self.room_no)
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.check_in_date)
        print("Check out date", self.check_out_date)
        print("Your Room rent is:", self.room_rent)
        print("Your Food bill is:", self.Food)
        print("Your laundary bill is:", self.Laundry)
        print("Your Game bill is:", self.Game)

        self.Total = self.room_rent+self.Laundry+self.Food+self.Game

        print("Your sub total bill is:", self.Total)
        print("Additional Service Charges is", self.additional_charges)
        print("Your grandtotal bill is:", self.Total +
              self.additional_charges, "\n")
        self.room_no += 1




class Update:
    def execute(self, choice):
        if choice == 1:
            print('Insert customer details')
            q = 'select * from hotel_management;'
            connect()
            cursor.execute(q)
            data = cursor.fetchall()
            print(data)

        print('1>Update Customer Details 2>exit \n')
        x = int(input('select choice:'))
        if x == 1:
            room_no = int(input('Enter Room number: '))
            name = input("Enter customer name: ")
            address = input("Enter address: ")
            check_in_date = input("Enter check in date: ")
            check_out_date = input("Enter check out date: ")
            room_rent = int(input("Enter room rent: "))
            Food = int(input('Enter food bill: '))
            Laundry = int(input("Enter laundry bill: "))
            game = int(input("Enter Game bill: "))
            Total = int(input("Enter Total Bill: "))

        try:
            data = [room_no, name, address, check_in_date, check_out_date, room_rent, Food, Laundry, game, Total]
            q = "insert into hotel_management values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(q, data)
            con.commit()
            print('details has been inserted...')
        except pymysql.DatabaseError as e:
            con.rollback()
            print(e)

        finally:
            closedb()

            
def main():

    a = Hotel_Management()
    q = Update()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate gamebill")

        print("6.Show total cost")

        print("7.Update")

        print("Exit")

        b = int(input("\nEnter your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):

            a.roomrent()

        if (b == 3):

            a.restaurentbill()

        if (b == 4):

            a.laundrybill()

        if (b == 5):

            a.gamebill()

        if (b == 6):

            a.display()

        if (b == 7):

            q.execute(1)

        if (b == 8):
            exit()

main()


