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

"""
TEST rosbridge driver
------------------------

This test requires a running node on the host ip that takes <TOPIC_1> and mirrors the value of it to <TOPIC_2>. This test script
will publish a value to <TOPIC_1>, and when it receives a change in value of <TOPIC_2> it sends back that value +1 in <TOPIC_1>.

Make sure that the rosbridge_websocket is running on the host. The following script can be used for the test, it needs to be 
built and started on the host (instructions at https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html).

```
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

class Topic_Mirror(Node):

    def __init__(self):
        super().__init__('agv_control')
        self.publisher = self.create_publisher(Int32, 'test_02', 10)
        self.subscriber = self.create_subscription(Int32, 'test_01', self.callback, 10)

    def callback(self, msg):
        to_publish = Int32()
        to_publish.data = msg.data
        self.publisher.publish(to_publish)


def main(args=None):
    print("Starting...")
    rclpy.init(args=args)
    mirror_node = Topic_Mirror()
    rclpy.spin(mirror_node)

    mirror_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```
"""

import sys
from os import path
import time
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.rosbridge.rosbridge import rosbridge
from drivers.driver import VariableOperation

HOST = "192.168.1.186"
PORT = 9090

TOPIC_1 = "test_01"
TOPIC_2 = "test_02"

VARIABLES = {
    TOPIC_1:{'datatype': "int", 'size': 1, 'operation': VariableOperation.WRITE},
    TOPIC_2:{'datatype': "int", 'size': 1, 'operation': VariableOperation.READ},
}

d = rosbridge(None, 'test')
d.host = HOST
d.port = PORT

if d.connect():
    d.addVariables(VARIABLES)

    value = 1
    start_time = time.perf_counter()
    while time.perf_counter() - start_time < 10:
        d.writeVariables([(TOPIC_1, value)])

        time.sleep(0.01)

        var_id, var_value, var_quality = d.readVariables([TOPIC_2])[0]
        print(var_id, var_value, var_quality)
        if var_value:
            value = var_value + 1

    d.disconnect()
else:
    print("Could not connect to host")
