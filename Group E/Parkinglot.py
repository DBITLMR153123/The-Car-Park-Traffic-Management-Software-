#Define a class to represent a ParkingLot
class ParkingLot:
    def __init__(self):
        self.parking_slots = []

    def add_slot(self, slot_number, name, slot_type, car_slot_number):
        slot_info = {
            "slot_number": slot_number,
            "name": name,
            "type": slot_type,
            "car_slot_number": car_slot_number
        }
        self.parking_slots.append(slot_info)

    def display_slots(self):
        if not self.parking_slots:
            print("No parking slots found.")
        else:
            print("Parking Slots:")
            for slot_info in self.parking_slots:
                print(f"Slot Number: {slot_info['slot_number']}")
                print(f"Name: {slot_info['name']}")
                print(f"Type: {slot_info['type']}")
                print(f"Car Slot Number: {slot_info['car_slot_number']}")
                print()

if __name__ == "__main__":
    parking_lot = ParkingLot()

    while True:
        print("1. Add Parking Slot")
        print("2. Display Parking Slots")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            slot_number = int(input("Enter parking slot number: "))
            name = input("Enter name: ")
            slot_type = input("Enter type: ")
            car_slot_number = int(input("Enter car slot number: "))
            parking_lot.add_slot(slot_number, name, slot_type, car_slot_number)

        elif choice == "2":
            parking_lot.display_slots()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

#Define a class to represent Customer
class Customer:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, customer_id, phone_number):
        customer_info = {
            "name": name,
            "customer_id": customer_id,
            "phone_number": phone_number
        }
        self.customers.append(customer_info)

    def display_customers(self):
        if not self.customers:
            print("No customers found.")
        else:
            print("Customer Details:")
            for customer_info in self.customers:
                print(f"Name: {customer_info['name']}")
                print(f"ID: {customer_info['customer_id']}")
                print(f"Phone Number: {customer_info['phone_number']}")
                print()

if __name__ == "__main__":
    customer_manager = Customer()

    while True:
        print("1. Add Customer")
        print("2. Display Customers")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            name = input("Enter customer name: ")
            customer_id = input("Enter customer ID: ")
            phone_number = input("Enter customer phone number (with +254): ")
            customer_manager.add_customer(name, customer_id, phone_number)

        elif choice == "2":
            customer_manager.display_customers()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

#Define a class to represent Vehicle
class Vehicle:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle_number, owner_id, phone_number, vehicle_type):
        vehicle_info = {
            "vehicle_number": vehicle_number,
            "owner_id": owner_id,
            "phone_number": phone_number,
            "vehicle_type": vehicle_type
        }
        self.vehicles.append(vehicle_info)

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles found.")
        else:
            print("Vehicle Details:")
            for vehicle_info in self.vehicles:
                print(f"Vehicle Number: {vehicle_info['vehicle_number']}")
                print(f"Owner ID: {vehicle_info['owner_id']}")
                print(f"Phone Number: {vehicle_info['phone_number']}")
                print(f"Vehicle Type: {vehicle_info['vehicle_type']}")
                print()

if __name__ == "__main__":
    vehicle_manager = Vehicle()

    while True:
        print("1. Add Vehicle")
        print("2. Display Vehicles")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            owner_id = input("Enter owner ID: ")
            phone_number = input("Enter owner phone number: ")
            vehicle_type = input("Enter vehicle type: ")
            vehicle_manager.add_vehicle(vehicle_number, owner_id, phone_number, vehicle_type)

        elif choice == "2":
            vehicle_manager.display_vehicles()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

#Define a class to represent Duration
class Duration:
    def __init__(self):
        self.durations = []

    def add_duration(self, duration_id, name, duration_time):
        duration_info = {
            "duration_id": duration_id,
            "name": name,
            "duration_time": duration_time
        }
        self.durations.append(duration_info)

    def display_durations(self):
        if not self.durations:
            print("No durations found.")
        else:
            print("Duration Details:")
            for duration_info in self.durations:
                print(f"ID: {duration_info['duration_id']}")
                print(f"Name: {duration_info['name']}")
                print(f"Duration Time: {duration_info['duration_time']}")
                print()

if __name__ == "__main__":
    duration_manager = Duration()

    while True:
        print("1. Add Duration")
        print("2. Display Durations")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            duration_id = input("Enter duration ID: ")
            name = input("Enter name: ")
            duration_time = input("Enter duration time: ")
            duration_manager.add_duration(duration_id, name, duration_time)

        elif choice == "2":
            duration_manager.display_durations()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")
