import unittest
from unittest.mock import patch, PropertyMock

import mock.adafruit_dht as adafruit_dht
import mock.GPIO as GPIO
from SmartHome import SmartHome
from SmartHomeError import SmartHomeError


class SmartHomeTest(unittest.TestCase):
    """
    Your test cases go here
    """

    def setUp(self) -> None:
        self.smart_home = SmartHome()

    @patch.object(GPIO, 'input')
    def test_check_room_occupancy_true(self, mock_occupancy):
        mock_occupancy.return_value = 0
        occupancy = self.smart_home.check_room_occupancy()
        self.assertTrue(occupancy)

    @patch.object(GPIO, 'input')
    def test_check_room_occupancy_false(self, mock_occupancy):
        mock_occupancy.return_value = 5
        occupancy = self.smart_home.check_room_occupancy()
        self.assertFalse(occupancy)
