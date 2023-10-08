import json

# Initialize empty flight data dictionary
flight_data = {}

# Function to display available flights
def display_flights():
    print("Available Flights:")
    for flight, details in flight_data.items():
        print(flight, ":", details["name"])

# Function for user login
def user_login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "user" and password == "password":
            return "user"
        elif username == "admin" and password == "adminpass":
            return "admin"
        else:
            print("Incorrect credentials. Please try again.")

# Function to book a ticket
def book_ticket(user):
    display_flights()
    selected_flight = input("Select a flight: ")
    if selected_flight in flight_data:
        # Display seat availability (2D array)
        seat_array = flight_data[selected_flight]["seats"]
        for row in seat_array:
            print(" ".join(row))

        # Ask for row and seat number to book
        while True:
            try:
                row = int(input("Enter row number: "))
                seat = input("Enter seat letter: ").upper()
                if seat in "ABCDEF" and seat_array[row - 1][ord(seat) - ord('A')] == '*':
                    seat_array[row - 1][ord(seat) - ord('A')] = 'X'
                    with open("bookings.txt", "a") as file:
                        file.write(f"{user} booked a seat on {selected_flight}: Row {row}, Seat {seat}\n")
                    print("Booking confirmed.")
                    break
                else:
                    print("Invalid seat selection. Please try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

# Function to cancel a booking
def cancel_booking(user):
    # Implement cancel booking logic here
    pass

# Main program loop
while True:
    print("\nAirplane Management System")
    print("1. User Login")
    print("2. Manage Flight Details")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        user_type = user_login()
        if user_type == "user":
            while True:
                print("\nUser Menu")
                print("1. Book a Ticket")
                print("2. Cancel Booking")
                print("3. Show Flights")
                print("4. Logout")
                user_choice = input("Enter your choice: ")
                if user_choice == "1":
                    book_ticket("User")
                elif user_choice == "2":
                    cancel_booking("User")
                elif user_choice == "3":
                    display_flights()
                elif user_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif user_type == "admin":
            # Implement admin functions
            pass
    elif choice == "2":
        # Implement flight details management
        pass
    elif choice == "3":
        # Save flight_data dictionary to a file
        with open("flight_data.json", "w") as file:
            json.dump(flight_data, file)
        print("Flight data saved.")
        break
    else:
        print("Invalid choice. Please try again.")

