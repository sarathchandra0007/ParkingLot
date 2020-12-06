import unittest
from parking_lot import VehicleParkingLot


class TestVehicleParkingLot(unittest.TestCase):
    """
    This class contains test cases for all the parking lot functionalities.
    """

    def test_create_parking_lot(self):
        """Test case to create parking lot with the capacity given"""
        parking_lot = VehicleParkingLot()
        response = parking_lot.create_parking_lot(3)
        self.assertEqual(3, response)

    def test_park_vehicle_success(self):
        """Test case for success scenario of parking a vehicle"""
        parking_lot = VehicleParkingLot()
        response = parking_lot.create_parking_lot(3)
        self.assertEqual(3, response)
        vehicle1_slot = parking_lot.park_vehicle("KA-01-HH-1234", 21)
        self.assertEqual(1, vehicle1_slot)

    def test_park_vehicle_failure(self):
        """Test case for failure scenario of parking a vehicle"""
        parking_lot = VehicleParkingLot()
        response = parking_lot.create_parking_lot(3)
        self.assertEqual(3, response)
        _ = parking_lot.park_vehicle("KA-01-HH-1234", 21)
        _ = parking_lot.park_vehicle("KB-01-HH-1234", 31)
        _ = parking_lot.park_vehicle("KC-01-HH-1234", 31)
        vehicle4_slot = parking_lot.park_vehicle("KD-01-HH-1234", 31)
        self.assertEqual(0, vehicle4_slot)

    def test_is_parking_slot_available(self):
        """Test case to check if a parking slot is available or not"""
        parking_lot = VehicleParkingLot()
        _ = parking_lot.create_parking_lot(3)
        response = parking_lot.is_parking_slot_available()
        self.assertEqual(True, response)

    def test_get_slot_numbers_for_drivers_by_age(self):
        """Test case to get slot numbers for drivers for a give age"""
        parking_lot = VehicleParkingLot()
        _ = parking_lot.create_parking_lot(3)
        _ = parking_lot.park_vehicle("KA-01-HH-1234", 21)
        _ = parking_lot.park_vehicle("KB-01-HH-1234", 21)
        _ = parking_lot.park_vehicle("KC-01-HH-1234", 31)
        response = parking_lot.get_slot_numbers_for_drivers_by_age(21)
        self.assertEqual("1,2", response)

    def test_get_vehicle_registration_numbers_for_driver_age(self):
        """Test case to get vehicle registration numbers for a give age"""
        parking_lot = VehicleParkingLot()
        _ = parking_lot.create_parking_lot(3)
        _ = parking_lot.park_vehicle("KA-01-HH-1234", 21)
        _ = parking_lot.park_vehicle("KB-01-HH-1234", 21)
        _ = parking_lot.park_vehicle("KC-01-HH-1234", 31)
        response = parking_lot.get_vehicle_registration_numbers_for_driver_age(21)
        self.assertIn("KA-01-HH-1234,KB-01-HH-1234", response)
        response1 = parking_lot.get_vehicle_registration_numbers_for_driver_age(18)
        self.assertEqual("", response1)

    def test_get_slot_number_for_vehicle(self):
        """Test case to get slot number for a vehicle with given registration number"""
        parking_lot = VehicleParkingLot()
        _ = parking_lot.create_parking_lot(3)
        _ = parking_lot.park_vehicle("KA-01-HH-1234", 21)
        _ = parking_lot.park_vehicle("KB-01-HH-1234", 21)
        response = parking_lot.get_slot_number_for_vehicle("KB-01-HH-1234")
        self.assertEqual(2, response)

    def test_leave(self):
        """Test case to leave the vehicle from parking lob."""
        parking_lot = VehicleParkingLot()
        _ = parking_lot.create_parking_lot(3)
        _ = parking_lot.park_vehicle("KA-01-HH-1234", 21)
        _ = parking_lot.park_vehicle("KB-01-HH-1234", 21)
        vehicle_slot_before_leaving = parking_lot.get_slot_number_for_vehicle("KB-01-HH-1234")
        self.assertEqual(2, vehicle_slot_before_leaving)
        _, _, _, is_available = parking_lot.leave(10)
        self.assertEqual(False, is_available)
        _, _, _, is_available = parking_lot.leave(2)
        self.assertEqual(True, is_available)
        vehicle_slot_after_leaving = parking_lot.get_slot_number_for_vehicle("KB-01-HH-1234")
        self.assertEqual(0, vehicle_slot_after_leaving)


if __name__ == '__main__':
    unittest.main()
