import random


def calculate_fare(rate, distance):
    return rate * distance


def display_routes():
    print("\n========== AVAILABLE ROUTES ==========")
    print("1. Pune Station to Shivajinagar (5 km)")
    print("2. Swargate to Kothrud (8 km)")
    print("3. Hinjawadi to Wakad (10 km)")
    print("======================================")


while True:
    print("\n========== CAB BOOKING CHATBOT ==========")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nSelect Cab Type:")
        print("1. Auto - INR 12/km")
        print("2. Sedan - INR 18/km")
        print("3. SUV - INR 25/km")

        cab_choice = input("Choose cab type: ")

        if cab_choice == "1":
            cab_type = "Auto"
            rate = 12
        elif cab_choice == "2":
            cab_type = "Sedan"
            rate = 18
        elif cab_choice == "3":
            cab_type = "SUV"
            rate = 25
        else:
            print("Invalid cab choice. Returning to main menu.")
            continue

        display_routes()

        route_choice = input("Choose route number: ")

        if route_choice == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route_choice == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route_choice == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice. Returning to main menu.")
            continue

        fare = calculate_fare(rate, distance)

        print("\n========== RIDE DETAILS ==========")
        print(f"Cab Type: {cab_type}")
        print(f"Source: {source}")
        print(f"Destination: {destination}")
        print(f"Distance: {distance} km")
        print(f"Rate: INR {rate}/km")
        print(f"Total Fare: INR {fare:.2f}")
        print("===================================")

        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirmation = input("Enter your choice: ")

        if confirmation == "1":
            otp = random.randint(1000, 9999)

            print("\nBooking Confirmed!")
            print(f"Your OTP is: {otp}")
            print("Your ride is now locked.")
            print("Cancellation is not allowed after OTP sharing.")
        elif confirmation == "2":
            print("\nRide cancelled successfully.")
            print("No OTP has been shared.")
        else:
            print("Invalid choice. Booking cancelled.")
            print("No OTP has been shared.")

    elif choice == "2":
        print("\nThank you for using the Cab Booking Chatbot!")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 or 2.")
