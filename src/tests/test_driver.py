# Simumatik Gateway - Simumatik 3rd party integration tool
# Copyright (C) 2021 Simumatik AB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import logging
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from driver_tester import Test_Driver
from setup_data import setup_data

test_drivers = ['opcua_client', 'robodk_driver'] # JUST MODIFY THIS LIST TO TEST ONE OR MORE DRIVERS

if __name__ == '__main__':
    my_setup_data = {}
    for driver_name in test_drivers:
        if driver_name in setup_data:
            my_setup_data.update({driver_name:setup_data[driver_name]})
            
    Test_Driver(setup_data=my_setup_data, run_time=10, log_level=logging.INFO, sleep_time=1e-2)
