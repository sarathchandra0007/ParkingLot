import sys
from parking_slot_info import ParkingSlotInfo


class VehicleParkingLot:
    """
    A class which contains car parking functionalities.

    Attributes
    ----------

    slots : list
        This has slots information and size depends on the given capacity.

    """
    def __init__(self):
        """
        Initializes slots variable
        """
        self.slots = []

    def create_parking_lot(self, capacity: int) -> int:
        """
        This function initializes slots variable based on the capacity.

        :param capacity: int
            Capacity defines the number of slots in the parking lot

        :return: int
            Number of slots created.
        """

        self.slots = [None] * capacity
        return capacity

    def park_vehicle(self, registration_number: str, age: int) -> int:
        """
        This function generates a parking slot for a vehicle based on it's availability and updates the slots variable.

        :param registration_number: string
            Registration  number for a vehicle
        :param age: int
            Age of the driver of the vehicle

        :return: int
            Returns the slot number
        """

        if self.is_parking_slot_available():
            slot_obj = ParkingSlotInfo(registration_number, age)

            # Allocate slot
            for slot_number, slot in enumerate(self.slots):
                if slot is None:
                    self.slots[slot_number] = slot_obj
                    return slot_number + 1
        else:
            return 0

    def is_parking_slot_available(self) -> bool:
        """
        This function checks for empty slots in the parking lot, returns true if exists.

        :return: bool
            True if there is a parking slot exists, else return false
        """

        return any(slot is None for slot in self.slots)

    def get_slot_numbers_for_drivers_by_age(self, age: int) -> str:
        """
        This function iterates through all the slots and provides the slot numbers (Comma separated) for a given age.

        :param age: int
            Age of the driver.
        :return: string
            Slot numbers with Comma separated.
        """

        slot_numbers_lst = []

        for slot_number, slot in enumerate(self.slots, 1):
            if slot is not None:
                if slot.age == age:
                    slot_numbers_lst.append(str(slot_number))
        return ','.join(slot_numbers_lst)

    def get_vehicle_registration_numbers_for_driver_age(self, age: int) -> str:
        """
        This function iterates through all the slots and provides the vehicle registration numbers (Comma separated)
        for a given age.

        :param age: int
            Age of the driver.
        :return: string
            Vehicle registration numbers with Comma separated
        """

        car_registration_numbers = []
        for slot in self.slots:
            if slot is not None:
                if slot.age == age:
                    car_registration_numbers.append(slot.registration_number)

        return ','.join(car_registration_numbers)

    def get_slot_number_for_vehicle(self, registration_number: str) -> int:
        """
        This function finds the slot number for a vehicle for a given registration number.

        :param registration_number: string
            Registration  number for a vehicle.
        :return: int
            Slot number for a given registration number.
        """

        for slot_number, slot in enumerate(self.slots, 1):
            if slot is not None:
                if slot.registration_number == registration_number:
                    return slot_number
        return 0

    def leave(self, slot_number: int) -> (int, str, int, bool):
        """
        This function updates the slots list after vacating the vehicle from the parking lot'

        :param slot_number: int
            Slot number in the parking lot

        :return:
            slot number (int): Vacated slot number
            Registration number (string):  Registration number of vacated vehicle
            age (int): Age of the driver of vacated vehicle
            is_possible (bool): Check if valid index or not
        """

        if 0 < slot_number <= len(self.slots) and self.slots[slot_number - 1] is not None:
            vehicle_info = self.slots[slot_number - 1]
            self.slots[slot_number - 1] = None
            return slot_number, vehicle_info.registration_number, vehicle_info.age, True

        # Populate with default values
        return slot_number, "", 0, False

    def execute_command(self, command: str):
        """
        This function parses the command and calls relevant functions defined for parking lot and prints required
        output.

        :param command: string
            parking lot command
        :return: None
        """

        if command.startswith("Create_parking_lot"):
            capacity = int(command.split(" ")[1])
            slots_created = self.create_parking_lot(capacity)
            print("Created parking of %s slots" % slots_created)

        elif command.startswith("Park"):
            slot_info = command.split(" ")
            registration_number, age = slot_info[1], int(slot_info[3])
            slot_number = self.park_vehicle(registration_number, age)
            if slot_number:
                print('Car with vehicle registration number "%s" has been parked at slot number %s' % (
                    registration_number, slot_number))
            else:
                print("There is no parking slot available!!!")

        elif command.startswith("Slot_numbers_for_driver_of_age"):
            age = int(command.split(" ")[1])
            all_slots = self.get_slot_numbers_for_drivers_by_age(age)
            print(all_slots)

        elif command.startswith("Slot_number_for_car_with_number"):
            registration_number = command.split(" ")[1]
            slot_number = self.get_slot_number_for_vehicle(registration_number)
            print(slot_number)

        elif command.startswith("Vehicle_registration_number_for_driver_of_age"):
            age = int(command.split(" ")[1])
            registration_number = self.get_vehicle_registration_numbers_for_driver_age(age)
            print(registration_number)

        elif command.startswith("Leave"):
            slot_number = int(command.split(" ")[1])
            slot_number, registration_number, age, is_possible = self.leave(slot_number)
            if is_possible:
                print('Slot number %s vacated, the car with vehicle registration number "%s" left the space, '
                      'the driver of the car was of age %s' % (slot_number, registration_number, age))
            else:
                print("Given slot number %s is not valid" % slot_number)


def main(file_name):
    parking_lot = VehicleParkingLot()

    with open(file_name) as file:
        for command in file:
            command = command.strip()
            parking_lot.execute_command(command)

        file.close()


if __name__ == '__main__':
    main(sys.argv[1])
