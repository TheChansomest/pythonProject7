# This program creates a Car object, a Truck object,
# and an SUV object.

import vehicles

def main():
    print("-" * 25, 'Demo Car Objects', "-" * 25)

    used_car = vehicles.Car('Audi', 2007, 12500, 21500.00, 4)

    used_car.__price = used_car.set_price(-90)

    print(used_car)

    print('Make:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Mileage:', used_car.get_mileage())
    print('Price:', used_car.get_price())
    print('Number of doors:', used_car.get_doors())

    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print("-" * 25, 'USED CAR INVENTORY', "-" * 25)
    # Display the car's data.
    print('The following car is in inventory:')
    print('Make:', car.get_make())
    print('Model:', car.get_model())
    print('Mileage:', car.get_mileage())
    print('Price:', car.get_price())
    print('Number of doors:', car.get_doors())
    print()
    
    # Display the truck's data.
    print("-" * 25, "Display the truck's data", "-" * 25)
    print('The following pickup truck is in inventory.')
    print('Make:', truck.get_make())
    print('Model:', truck.get_model())
    print('Mileage:', truck.get_mileage())
    print('Price:', truck.get_price())
    print('Drive type:', truck.get_drive_type())
    print()
    
    # Display the SUV's data.
    print("-" * 25, 'Demo SUV Objects', "-" * 25)
    print('The following SUV is in inventory.')
    print('Make:', suv.get_make())
    print('Model:', suv.get_model())
    print('Mileage:', suv.get_mileage())
    print('Price:', suv.get_price())
    print('Passenger Capacity:', suv.get_pass_cap())

# Call the main function.
if __name__ == '__main__':
      main()