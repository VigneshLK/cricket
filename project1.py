class User:
    venue = [(1, "Chinnaswamy stadium", "Bangalore"), (2, "Chidhambaram stadium", "Chennai"), (3, "Eden Garden", "Kolkata")] # 1, 2, 3 = venue_id
    tickets = [[11, 100, 0], [12, 200, 0], [13, 300, 0], [14, 400, 0], [15, 500, 0], [16, 600, 0]]
    # match_id & tickets
    matches = [(1, 11, "CSK vs MI", "15-05-2023", "8.00pm"), (1, 12, "RR vs DC", "04-07-2023", "8.00am"), (2, 13, "CSK vs KKR", "24-05-2023", "01.00am"), (2, 14, "RCB vs MI", "23-07-2023", "10.30pm"), (3, 15, "MI vs RR", "24-11-2023", "10.00am"), (3, 16, "CSK vs RR", "04-11-2023", "09.00am")] # venue_id & match_id & matches, date and time

    contacts = {'raj': {'phone': '9952215992', 'email': 'raj@gmail.com', 'password': '123'},
                'kumar': {'phone': '8012305239', 'email': 'kumar@gmail.com', 'password': '456'}}

    def register(self, user_name, phone_number, email_id, password):
        self.user_name = user_name
        self.phone_number = phone_number
        self.email_id = email_id
        self.password = password
        contact = {'phone': self.phone_number, 'email': self.email_id, 'password': self.password}
        User.contacts[self.user_name] = contact
        print(User.contacts)
        print("Registration successful")

    def choose_venue(self, city): # city = Bangalore[2]
        self.city = city
        for x in User.venue:
            if x[2] == self.city:
                print(f"Select the venue {x[0]}, {x[1]}, {x[2]}")
                return x

    def choose_match(self, venue_id, date): # venue_id = 1, date 
        self.venue_id = venue_id
        self.date = date
        for y in User.matches:
            if y[0] == self.venue_id and y[3] == self.date:
                print(f"Select the match {y[0]}, {y[1]}, {y[2]}, {y[3]}, {y[4]}")
                return y

    def check_tickets(self, match_id): # match_id = 11
        self.match_id = match_id
        for z in User.tickets:
            if z[0] == self.match_id:
                print("Tickets available:", z[1])
                return z

    def display(self):
        choice = input("Do you want to see the venues and matches? (yes/no): ")
        if choice == "yes":
            city = input("Enter the city: ")
            city = city.title()
            city_name = obj.choose_venue(city) # call method choose_venue
            venue_id = city_name[0]
            print("Available match list in", city_name[2])
            for y in User.matches:
                if venue_id == y[0]:
                    print(f"{y[0]}, {y[1]}, {y[2]}, {y[3]}, {y[4]}")
            date = input("Enter the date in dd-mm-yyyy format: ")
            select_match = obj.choose_match(venue_id, date) # user call method choose_match
            match_id = select_match[1]
            checking = obj.check_tickets(match_id) # call method check_tickets
            return checking
        elif choice == "no":
            return obj.login_user() # call method login_user

class RegisteredUser(User):
    booked = []

    def login_user(self):
        email_id = input("Enter the email address: ")
        while not email_id.endswith("@gmail.com"):
            print("Enter a valid email address")
            email_id = input("Enter the email address: ")

        password = input("Enter the password: ")
        while not password.isprintable():
            print("Enter a valid password")
            password = input("Enter the password: ")

        for i in User.contacts:
            if User.contacts[i]["email"] == email_id:
                if User.contacts[i]["password"] == password:
                    print("Login successful")
                    return i

        print("Invalid credentials")
        return obj.login_user()

    def booked_ticket(self):
        user = obj.login_user()
        RegisteredUser.booked = obj.display()

        booking = input("Do you want to book a ticket? (yes/no): ")
        if booking == "yes":
            if RegisteredUser.booked[1] != 0:
                num_of_seats = int(input("Enter the number of tickets: "))
                if num_of_seats <= RegisteredUser.booked[1]:
                    RegisteredUser.booked[2] += num_of_seats
                    RegisteredUser.booked[1] -= num_of_seats
                    print("Tickets booked:", num_of_seats)
                    print("Available tickets:", RegisteredUser.booked[1])

                    changes = input("Do you want to cancel the ticket? (yes/no): ")
                    if changes == "yes":
                        obj.cancel_ticket(num_of_seats)
                        return obj.login_user()
                    elif changes == "no":
                        print("Thank you for using our service!")
                        return obj.login_user()
                else:
                    print("Tickets are not available.")
            else:
                print("Tickets are not available.")
        else:
            if booking == "no":
                print("Thank you for using our service!")
                return obj.login_user()

    def cancel_ticket(self, num_of_cancel):
        match_id = int(input("Enter the match ID: "))

        for b in RegisteredUser.tickets:
            if b[0] == match_id:
                if b[2] >= num_of_cancel:
                    b[2] -= num_of_cancel
                    b[1] += num_of_cancel
                    print("Tickets canceled:", num_of_cancel)
                    print("Your ticket has been successfully canceled.")
                else:
                    print("Enter fewer tickets to cancel.")

print("Welcome to the cricket booking service")
obj = RegisteredUser()

i = 0
while i < 2:
    choose = int(input("1. Register\n2. Login\n3. Exit\n"))

    if choose == 1:
        user_name = input("Enter name: ")
        while not user_name.isalpha():
            print("Enter a valid name.")
            user_name = input("Enter name: ")

        phone_number = input("Enter number: ")
        while not phone_number.isdigit() or len(phone_number) != 10:
            if not phone_number.isdigit():
                print("Enter only numbers.")
            if len(phone_number) != 10:
                print("Enter exactly 10 digits.")
            phone_number = input("Enter number: ")

        email_id = input("Enter email ID: ")
        while not email_id.endswith("@gmail.com"):
            print("Enter a valid email ID.")
            email_id = input("Enter email ID: ")

        password = input("Enter a password: ")
        obj.register(user_name, phone_number, email_id, password)

    if choose == 2:
        print("Welcome to the login page")
        obj.booked_ticket()

    if choose == 3:
        i = 4
