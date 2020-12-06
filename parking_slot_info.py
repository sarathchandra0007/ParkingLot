class ParkingSlotInfo:
    """
    A Class which contains information of vehicle registration number and the age of the driver of the vehicle.
    """
    def __init__(self, registration_number: str, driver_age: int):
        """
        Initializes registration_number and age.
        :param registration_number: Vehicle registration number
        :param driver_age: Age of the driver
        """
        self.registration_number = registration_number
        self.age = driver_age

