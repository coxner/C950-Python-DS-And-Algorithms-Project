# Christian Oxner 009554482

import csv
import truck
import datetime

from package import Package
from hashtable import HashTable

# Open CSV files with encoding store distance and address in list
with open("csv/distance.csv", encoding='utf-8-sig') as csvfile_distance:
    distance_csv = csv.reader(csvfile_distance)
    distance_csv = list(distance_csv)
with open("csv/address.csv", encoding='utf-8-sig') as csvfile_address:
    address_csv = csv.reader(csvfile_address)
    address_csv = list(address_csv)
with open("csv/package.csv", encoding='utf-8-sig') as csvfile_package:
    package_csv = csv.reader(csvfile_package)


# Put packages into a hash map
def package_to_hash(filename, hash_table):
    with open(filename, encoding='utf-8-sig') as all_packages:
        packages = csv.reader(all_packages)
        for package in packages:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deadline = package[5]
            mass = package[6]
            status = "Hub"
            package = Package(id, address, city, state, zip, deadline, mass, status)
            hash_table.insert(id, package)


# Create truck objects and manually load them full of packages
# Instantiation of truck_one
truck_one = truck.Truck(1, 16, 18, [13, 19, 16, 14, 15, 20, 21, 31, 34, 40, 1, 17, 29], 0.0, "4001 South 700 East",
                        datetime.timedelta(hours=8))
# Instantiation of truck_two
truck_two = truck.Truck(2, 16, 18, [3, 18, 36, 38, 30, 33, 35, 37, 39, 6, 2, 24, 25, 27], 0.0, "4001 South 700 East",
                        datetime.timedelta(hours=9, minutes=5))
# Instantiation of truck_three
truck_three = truck.Truck(3, 16, 18, [26, 22, 28, 7, 10, 11, 12, 23, 9, 32, 4, 5, 8], 0.0, "4001 South 700 East",
                          datetime.timedelta(hours=10, minutes=20))


# Create hash table and load packages
package_hash_table = HashTable()
package_to_hash("csv/package.csv", package_hash_table)

# had to create a empty array or package would keep checking out of bounds
def delivery(truck):
    packages_for_truck = []
    # Loop through packages in truck and add them to array
    for package in truck.packages:
        package_add_to_truck = package_hash_table.search(package)
        # Truck has departed add departure time to package
        package_add_to_truck.on_truck = truck.time
        package_add_to_truck.loaded_on_truck = truck.id
        packages_for_truck.append(package_add_to_truck)
    # Empty out all packages on truck
    truck.packages.clear()
    # While there is packages to deliver
    while len(packages_for_truck) > 0:
        # Index used to compare packages
        index_of_first_package = 0
        index_of_last_package = len(packages_for_truck) - 1
        # Keep comparing packages while the last index is > or = the first index
        while index_of_first_package <= index_of_last_package:
            # Get packages that will be compared
            first_package = packages_for_truck[index_of_first_package]
            last_package = packages_for_truck[index_of_last_package]
            # Get the distance from current address for both packages being compared
            for address in address_csv:
                if truck.curr_address == address[2]:
                    truck_index = int(address[0])
                elif first_package.address == address[2]:
                    first_package_index = int(address[0])
                elif last_package.address == address[2]:
                    last_package_index = int(address[0])
            start_distance = distance_csv[truck_index][first_package_index]
            if start_distance == '':
                start_distance = distance_csv[first_package_index][
                    truck_index]
            start_distance = float(start_distance)
            end_distance = distance_csv[truck_index][last_package_index]
            if end_distance == '':
                end_distance = distance_csv[last_package_index][truck_index]
            end_distance = float(end_distance)
            # if first package difference is less than last package difference
            if start_distance < end_distance:
                # first package index is the min package and min distance is equal to this package distance
                min_package = first_package
                min_package_distance = start_distance
                # decrease the index of the last package
                index_of_last_package -= 1
            # last package is less than first package
            else:
                # min package and distance are set to the last package index
                min_package = last_package
                min_package_distance = end_distance
                # increase the index of the first package
                index_of_first_package += 1
        # set the trucks current address to the min package address
        truck.curr_address = min_package.address
        # Add distance traveled to the trucks total
        truck.distance_travel += min_package_distance
        # Remove package from the list as its been delivered
        packages_for_truck.pop(packages_for_truck.index(min_package))
        # Time added to truck is the distance traveled divded by the speed the truck was driving
        truck.time += datetime.timedelta(hours=min_package_distance / 18)
        # Packages delivery time is equal to the trucks time
        min_package.delivery_time = truck.time

# Deliver packages for all trucks
delivery(truck_one)
delivery(truck_two)
delivery(truck_three)
# Calculate the total distance traveled by trucks
total_distance = truck_one.distance_travel + truck_two.distance_travel + truck_three.distance_travel


# Main class provides interface for the user
class Main:
    print("WGUPS Delivery Data Structure and Algorithms")
    print("The total mileage of all packages traveled is " + str(total_distance))
    print("Please enter T if you want to enter two times to view packages between.")
    print("Please enter P if you want to enter a package to view its status")
    # Allows user to enter T to select a time to view packages status or enter a P to view a individual package
    user_input = input("Enter a T or P if anything else is entered program will close: ")
    # If user wants to enter a time
    if user_input.upper() == "T":
        print("Please enter a time in HH:MM:SS format so that time program can read in the time properly")
        user_time = input("Enter a time to view packages: ")
        # Splits the user input up into hour minute and seconds
        hour, min, sec = [int(i) for i in user_time.split(":")]
        # converts the input into a time variable for comparison
        time_to_check = datetime.timedelta(hours=int(hour), minutes=int(min), seconds=int(sec))
        print("Packages at the time of " + str(time_to_check))
        print("Package ID      On Truck #        Package Status")
        print(" _________     ______________     ___________")
        # Loop through packages to determine status of package at time enetered
        for i in range(1, 41):
            package = package_hash_table.search(i)
            # If packages delivery time is before time entered the package is delivered
            if package.delivery_time < time_to_check:
                package.delivery_status = "Delivered"
            # if the package has been added to the truck yet but not delivered it is en route
            elif package.on_truck < time_to_check:
                package.delivery_status = "En route"
            # Package is still at the hub
            else:
                package.delivery_status = "At Hub"
            print("    " + str(package.ID) + "            " + str(package.loaded_on_truck)
                  + "                " + str(package.delivery_status))
    elif user_input.upper() == "P":
        package_number_to_check = input("Enter a package # you wish to view make sure it is between 1 - 41: ")
        if int(package_number_to_check) < 1 or int(package_number_to_check) > 41:
            print("Invalid entry program now closing")
            exit()
        for i in range(1, 41):
            if i == int(package_number_to_check):
                package_to_print = package_hash_table.search(i)
        print("Package ID      Package Address     Delivery Deadline    Package Weight     Time Delivered")
        print(" _________     _________________    ___________________  ______________     ______________")
        print("   " + str(package_to_print.ID) + "         "
              + str(package_to_print.address) + "    " + str(package_to_print.deadline) + "                       "
              + str(package_to_print.mass) + "           " + str(package_to_print.delivery_time))

    else:
        print("Invalid character program will now close")
        exit()
