# John Funk
# Student ID: 010010682
# Total Big-O for this program is O(N^3)

import csv
import datetime


# Class for interacting with the hash table
# Total Big-O for this class is O(N)
class PackageHashTable:

    # Initializes hash table
    # Big-O for this function is O(1)
    def __init__(self, total_packages=40):
        self.package_table = []
        for init_i in range(total_packages):
            self.package_table.append([])

    # Inserts a package into the hash table
    # Big-O for this function is O(N)
    def insert_package(self, insert_key, insert_item):
        insert_bucket = hash(insert_key) % len(self.package_table)
        insert_bucket_list = self.package_table[insert_bucket]

        for insert_key_value in insert_bucket_list:
            if insert_key_value[0] == insert_key:
                insert_key_value[1] = insert_item
                return True

        insert_key_value = [insert_key, insert_item]
        insert_bucket_list.append(insert_key_value)
        return True

    # Searches for a package
    # Big-O for this function is O(N)
    def search_package(self, search_key):
        search_bucket = hash(search_key) % len(self.package_table)
        search_bucket_list = self.package_table[search_bucket]

        for search_key_value in search_bucket_list:
            if search_key_value[0] == search_key:
                return search_key_value[1]  # value
        return None

    # Removes a package
    # Big-O for this function is O(N)
    def remove_package(self, remove_key):
        remove_bucket = hash(remove_key) % len(self.package_table)
        remove_bucket_list = self.package_table[remove_bucket]

        for remove_key_value in remove_bucket_list:
            if remove_key_value[0] == remove_key:
                remove_bucket_list.remove([remove_key_value[0], remove_key_value[1]])


# Class for packages
# Total Big-O for this class is O(1)
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, mass_kilo, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass_kilo = mass_kilo
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.state, self.zip_code, self.deadline, self.mass_kilo,
            self.status)


# This function is responsible for reading the package data from the attached CSV file
# The Big-O for this function is O(N^2)
def load_package_data(package_file):
    with open(package_file) as packages_csv:
        package_data = csv.reader(packages_csv, delimiter=',')
        next(package_data)
        for package_load in package_data:
            p_id = int(package_load[0])
            p_address = package_load[1]
            p_city = package_load[2]
            p_state = package_load[3]
            p_zip_code = package_load[4]
            p_deadline = package_load[5]
            p_mass_kilo = package_load[6]
            p_status = "Loaded on truck"

            p = Package(p_id, p_address, p_city, p_state, p_zip_code, p_deadline, p_mass_kilo, p_status)

            myHash.insert_package(p_id, p)


# This function is responsible for reading the distance data from the attached CSV file
# The Big-O for this function is O(N^2)
def load_distance_data(distance_file, distance_array_for_load):
    with open(distance_file) as distance_csv:
        distance_data = csv.reader(distance_csv, delimiter=',')
        for row in distance_data:
            for entry in row:
                row[row.index(entry)] = float(entry)
            distance_array_for_load.append(row)


# This function is responsible for assigning a usable location code based on address strings
# It takes the string for the package address and checks the first 4 digits (including a leading space)
# It then assigns and returns a value corresponding to the appropriate row in the distance data table
# The Big-O for this function is O(1)
def assign_location_code(address_strings):
    location_code_for_return = 0
    if address_strings[:4] == " 195":
        location_code_for_return = 5
    elif address_strings[:4] == " 253":
        location_code_for_return = 9
    elif address_strings[:4] == " 233":
        location_code_for_return = 8
    elif address_strings[:4] == " 380":
        location_code_for_return = 18
    elif address_strings[:4] == " 410":
        location_code_for_return = 19
    elif address_strings[:4] == " 306":
        location_code_for_return = 13
    elif address_strings[:4] == " 133":
        location_code_for_return = 2
    elif address_strings[:4] == " 300":
        location_code_for_return = 12
    elif address_strings[:4] == " 600":
        location_code_for_return = 25
    elif address_strings[:4] == " 260":
        location_code_for_return = 10
    elif address_strings[:4] == " 357":
        location_code_for_return = 16
    elif address_strings[:4] == " 201":
        location_code_for_return = 6
    elif address_strings[:4] == " 430":
        location_code_for_return = 20
    elif address_strings[:4] == " 458":
        location_code_for_return = 21
    elif address_strings[:4] == " 314":
        location_code_for_return = 14
    elif address_strings[:4] == " 148":
        location_code_for_return = 3
    elif address_strings[:4] == " 177":
        location_code_for_return = 4
    elif address_strings[:4] == " 359":
        location_code_for_return = 17
    elif address_strings[:4] == " 635":
        location_code_for_return = 26
    elif address_strings[:4] == " 510":
        location_code_for_return = 23
    elif address_strings[:4] == " 502":
        location_code_for_return = 22
    elif address_strings[:4] == " 538":
        location_code_for_return = 24
    elif address_strings[:4] == " 106":
        location_code_for_return = 1
    elif address_strings[:4] == " 283":
        location_code_for_return = 11
    elif address_strings[:4] == " 336":
        location_code_for_return = 15
    elif address_strings[:4] == " 230":
        location_code_for_return = 7
    else:
        print("Error in if statements to assign current location values")
    return location_code_for_return


# This function is responsible for finding the next closest destination
# This function accepts the current location code and the correct packages array
# It sets the shortest distance to a value greater than all possible distances
# It then checks every package one by one to find the shortest destination
# It adds the package index, closest location code, and distance value to the next_location variable and returns it
# The Big-O for this function is O(N^2)
def find_shortest_distance(current_location_code, truck_packages):
    shortest_distance = 50
    current_position_distance_array = distance_array[current_location_code]
    next_package_index = 0
    closest_location_code = 0

    for i in range(len(truck_packages)):

        # O(N)
        location = myHash.search_package(truck_packages[i]).address

        # O(1)
        location_code = assign_location_code(location)

        # O(1)
        if current_position_distance_array[location_code] < shortest_distance:
            shortest_distance = current_position_distance_array[location_code]
            next_package_index = i
            closest_location_code = location_code

    next_location = [next_package_index, closest_location_code, shortest_distance]
    return next_location


# This function is responsible for calculating the distance back to the hub
# It accepts the current location and returns the distance value for the return to hub
# The Big-O for this function is O(1)
def return_to_hub(current_location_code):
    current_position_distance_array = distance_array[current_location_code]
    return current_position_distance_array[0]


# This function is responsible for removing delivered packages
# It accepts the truck, package index, and delivery time
# It then reads the appropriate package, sets the status to complete, and sets the delivery time
# It then inserts the package back into the hash table and removes the package from the truck
# The Big-O for this function is O(N)
def remove_complete_packages(truck, package_index, delivery_time):
    package_delivered = myHash.search_package(truck[package_index])
    package_delivered.status = "Delivery Complete"
    package_delivered.deadline = delivery_time
    myHash.insert_package(truck[package_index], package_delivered)

    truck.pop(package_index)


# This function is responsible for assigning packages, assigning leaving times, and calling the truck_route function
# This function assigns the packages and leave times to each truck
# It then calls the truck_route function for each truck
# It then totals the distance traveled for all trucks and returns it
# The Big-O for this function is O(N^3)
def truck_data():
    truck_one_packages = [1, 4, 5, 7, 13, 14, 15, 16, 19, 20, 29, 30, 34, 37, 39, 40]
    truck_two_packages = [3, 6, 18, 25, 26, 28, 31, 32, 36, 38]
    truck_three_packages = [2, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 27, 33, 35]

    truck_one_leave_time_hour = 8
    truck_one_leave_time_minute = 0
    truck_two_leave_time_hour = 9
    truck_two_leave_time_minute = 5
    truck_three_leave_time_hour = 10
    truck_three_leave_time_minute = 20

    truck_one_distance = truck_route(truck_one_packages, truck_one_leave_time_hour, truck_one_leave_time_minute)
    truck_two_distance = truck_route(truck_two_packages, truck_two_leave_time_hour, truck_two_leave_time_minute)
    truck_three_distance = truck_route(truck_three_packages, truck_three_leave_time_hour, truck_three_leave_time_minute)

    total_distance_truck_data = truck_one_distance + truck_two_distance + truck_three_distance

    return total_distance_truck_data


# This function is responsible for calculating the distances and times for deliveries
# It first sets the status of all packages on the truck to "On the way"
# It then calls the find_shortest_distance function for each package
# It then adds the distance traveled to the total and calculates the total time spent traveling
# It then calls the remove_complete_packages function to remove the package from the truck
# It then calls the return_to_hub function to add the distance back to the hub into the calculation and returns distance
# The Big-O for this function is O(N^3)
def truck_route(truck_packages, leave_time_hour, leave_time_minute):
    current_truck_location = 0  # Initialize to home
    distance_traveled = 0

    # O(N^2)
    for i in range(len(truck_packages)):
        package_on_way = myHash.search_package(truck_packages[i])
        package_on_way.status = "On the way"
        myHash.insert_package(truck_packages[i], package_on_way)

    # O(N^3)
    for i in range(len(truck_packages)):
        next_location = find_shortest_distance(current_truck_location, truck_packages)
        distance_traveled = distance_traveled + next_location[2]
        time_spent_minutes = (distance_traveled / 18) * 60
        total_minutes = time_spent_minutes + leave_time_minute
        if total_minutes >= 60:
            time_of_day_hour = leave_time_hour + (total_minutes // 60)
            time_of_day_minute = total_minutes % 60
        else:
            time_of_day_hour = leave_time_hour + (time_spent_minutes // 60)
            time_of_day_minute = total_minutes

        current_time = "{:.0F}:".format(time_of_day_hour) + "{:.0F}".format(time_of_day_minute)

        package_to_delete = next_location[0]

        remove_complete_packages(truck_packages, package_to_delete, current_time)

        current_truck_location = next_location[1]

    distance_traveled = distance_traveled + return_to_hub(current_truck_location)

    return distance_traveled


# This function is responsible for displaying the correct report
# For the first two reports, it compares the package deadline to the current time of the report to set the proper status
# It then prints the package information for each package
# For the individual package report, the function searches the hash table for the requested package
# It uses if statements to check the package for which truck a package is on
# It then uses nested if statements to check the status of the package based on time and prints the package information
# After it displays the requested report, it calls the user_interface function to return the user to the main menu
# The Big-O for this function is O(N^2)
def display_reports(user_package_id, user_package_hour, user_package_minute):
    package_id = int(user_package_id)
    package_time_string = str(user_package_hour) + ":" + str(user_package_minute)
    package_time_format = '%I:%M'
    package_time = datetime.datetime.strptime(package_time_string, package_time_format)
    package_hour = int(user_package_hour)
    package_minute = int(user_package_minute)
    truck_one_packages = [1, 4, 5, 7, 13, 14, 15, 16, 19, 20, 29, 30, 34, 37, 39, 40]
    truck_two_packages = [3, 6, 18, 25, 26, 28, 31, 32, 36, 38]

    if user_package_id == 41:
        print("Package status as of 9:00 AM:")
        print("Package ID\t\tAddress\t\t\t\t\t\t\t\t\t\tCity\t\t\tState\tZip Code\tDelivery Time\tWeight\tStatus")
        report_a_time = datetime.datetime.strptime('9:00', package_time_format)
        for i in range(len(myHash.package_table)):

            report_package_id = i
            package_for_display = myHash.search_package(i + 1)
            package_deadline = datetime.datetime.strptime(package_for_display.deadline, package_time_format)

            if report_package_id in truck_one_packages:
                if report_a_time < package_deadline:
                    package_for_display.status = "Package on the way"
                    print(package_for_display)
                else:
                    package_for_display.status = "Package delivered"
                    print(package_for_display)
            else:
                package_for_display.status = "Loaded on truck"
                print(package_for_display)

    elif user_package_id == 42:
        print("Package status as of 10:00 AM:")
        print("Package ID\t\tAddress\t\t\t\t\t\t\t\t\t\tCity\t\t\tState\tZip Code\tDelivery Time\tWeight\tStatus")
        report_b_time = datetime.datetime.strptime('10:00', package_time_format)
        for i in range(len(myHash.package_table)):

            package_for_display = myHash.search_package(i + 1)
            package_deadline = datetime.datetime.strptime(package_for_display.deadline, package_time_format)
            report_package_id = i

            if report_package_id in truck_one_packages:
                package_for_display.status = "Package delivered"
                print(package_for_display)

            elif report_package_id in truck_two_packages:
                if package_deadline < report_b_time:
                    package_for_display.status = "Package delivered"
                    print(package_for_display)

                else:
                    package_for_display.status = "Package on the way"
                    print(package_for_display)

            else:
                package_for_display.status = "Loaded on truck"
                print(package_for_display)

    elif 0 < package_id < 41:

        package_for_display = myHash.search_package(package_id)
        package_deadline = datetime.datetime.strptime(package_for_display.deadline, package_time_format)

        if package_id in truck_one_packages:
            if package_time < package_deadline:
                if package_hour < 8:
                    package_for_display.status = "Loaded on truck"
                    print(package_for_display)
                else:
                    package_for_display.status = "Package on the way"
                    print(package_for_display)
            else:
                package_for_display.status = "Package delivered"
                print(package_for_display)

        elif package_id in truck_two_packages:
            print("Package in truck two")
            if package_time < package_deadline:
                print("Package time is less than package deadline")
                if package_hour < 9:
                    package_for_display.status = "Loaded on truck"
                    print(package_for_display)
                elif package_hour == 9:
                    if package_minute < 5:
                        package_for_display.status = "Loaded on truck"
                        print(package_for_display)
                    else:
                        package_for_display.status = "Package on the way"
                        print(package_for_display)
            else:
                package_for_display.status = "Package delivered"
                print(package_for_display)

        else:
            if package_time < package_deadline:
                if package_hour < 10:
                    package_for_display.status = "Loaded on truck"
                    print(package_for_display)
                elif package_hour == 10:
                    if package_minute < 20:
                        package_for_display.status = "Loaded on truck"
                        print(package_for_display)
                else:
                    package_for_display.status = "Package on the way"
                    print(package_for_display)
            else:
                package_for_display.status = "Package delivered"
                print(package_for_display)

    else:
        print("Invalid input from display_reports")

    user_interface(total_distance)


# This function displays and accepts input for the user interface
# It uses if statements to determine what report the user wants
# If the user requests either of the first two reports, it calls the display_reports function
# If the user requests the 1:00 PM report, it displays all packages as delivered
# If the user requests the total mileage report, it prints the total mileage
# The Big-O for this function is O(1)
def user_interface(total_distance_all_trucks):
    print("\n\nWelcome to the Package Information Application")
    print("\nFor all packages at 9:00 AM, input A")
    print("For all packages at 10:00 AM, input B")
    print("For all packages at 1:00 PM, input C")
    print("For total mileage driven by all trucks, input D")
    print("To view specific package information, input the package ID")
    print("To exit, input 99")
    user_input = input()

    if user_input == "A":
        display_reports(41, 9, 00)
    elif user_input == "B":
        display_reports(42, 10, 00)
    elif user_input == "C":
        print("Package status as of 1:00 PM:")
        print("Package ID\t\tAddress\t\t\t\t\t\t\t\t\t\tCity\t\t\tState\tZip Code\tDelivery Time\tWeight\tStatus")
        for i in range(len(myHash.package_table)):
            print(format(myHash.search_package(i + 1)))
        user_interface(total_distance)
    elif user_input == "D":
        print("Total mileage traveled by all trucks: {}".format(total_distance_all_trucks))
        # user_interface(total_distance)
    elif 0 < int(user_input) < 41:
        user_input_hour = input("Enter the hour (24 hour format) you want to view: ")
        user_input_minute = input("Enter the minute you want to view: ")
        display_reports(user_input, user_input_hour, user_input_minute)
    elif int(user_input) == 99:
        print("Thank you for using the application")
    else:
        print("Invalid input from user_interface")
        user_interface(total_distance)


# This function creates the hash table
myHash = PackageHashTable()

# These functions load the CSV information and create the distance array
load_package_data('WGUPSPackages.csv')
distance_array = []
load_distance_data('WGUPSDistanceTable.csv', distance_array)

# This function calls the truck_data function
total_distance = truck_data()

# This function starts the user interface
user_interface(total_distance)
