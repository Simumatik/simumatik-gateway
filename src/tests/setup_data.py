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

from drivers.driver import VariableOperation, VariableDatatype

setup_data = {}

# development
setup_data.update({
    "development": {
        "DRIVER": "development", 
        "SETUP": {
            "parameters": {
                "rpi": 10,
            },
            "variables": {
                "inputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "outputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# acs_spiiplus
setup_data.update({
    "acs_spiiplus": {
        "DRIVER": "acs_spiiplus", 
        "SETUP": {
            "parameters": {
                "ip": "192.168.240.1", 
                "comm": "simulator",
                "rpi": 10,
            },
            "variables": {
                "I0":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "I1":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "V0":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "V1":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
                "I(0)":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "I(1)":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "V(0)":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "V(1)":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# allenbradley_logix
setup_data.update({
    "allenbradley_logix": {
        "DRIVER": "allenbradley_logix", 
        "SETUP": {
            "parameters": {
                "ip": "192.168.1.246", 
            },
            "variables": {
                "inputs_BOOL":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "outputs_BOOL":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "inputs_BYTE":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "outputs_BYTE":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "inputs_WORD":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "outputs_WORD":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "inputs_DWORD":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "outputs_DWORD":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "inputs_INT":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "outputs_INT":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "inputs_FLOAT":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "outputs_FLOAT":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# cprog_cri
setup_data.update({
    "cprog_cri": {
        "DRIVER": "cprog_cri", 
        "SETUP": {
            "parameters": {
                #"ip": "192.168.0.233",
            },
            "variables": {
                "Axis":{"datatype": VariableDatatype.FLOAT, "size": 6, "operation": VariableOperation.READ},
                "DOUT":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "GSIG":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "GRIPPERSTATE":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# enip_generic_device
"""
Test with Codesys:
1. Create a project with Control Win V3 or the RPI equivalent.
2. Add an Ethernet (Ethernet) module from Ethernet/IP section as a new device.
3. Inside the Ethernet module, add an Ethernet_IP_Scanner module.
4. Inside the Ethernet_IP_Scanner module, add an Generic_Ethernet_IP_device.
5. Be aware that Codesys gateway is enabled and connected (double click on Control Win V3 device to verify).
6. Double click on the Ethernet module, and select the interface you are using, such as wifi or ethernet.
7. Double click on the Generic_Ethernet_IP_device, set the IP of the ENIP driver, set Strict Compatiblity Check, and uncheck every check in the general tab.
8. Still in the Generic_Ethernet_IP_device, choose the Connections tab and click add connections. 
9. In connection-path add "20 04 2C 66 2C 6C". Set O->T and T->O bytes to "1". Set Connection type in both cases to "Point to point" and to "Fixed". In the left, set the data to "32 bits run/idle", and in the right to "pure data"
10. Now you can compile, go online, and run the driver with the following config:
"""
setup_data.update({
    "enip_generic_device": {
        "DRIVER": "enip_generic_device", 
        "SETUP": {
            "parameters": {
                "ip": "192.168.0.150",
                "read_size": 10,
                "write_size": 10,
            },
            "variables": {
                "IB0":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "IB1":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "QB0":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "QB1":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# fanuc_roboguide
setup_data.update({
    "fanuc_roboguide": {
        "DRIVER": "fanuc_roboguide", 
        "SETUP": {
            "parameters": {
                "port": 60008,
            },
            "variables": {
                "Axis":{"datatype": VariableDatatype.FLOAT, "size": 6, "operation": VariableOperation.READ},
                "DI10":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "DO9":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "GI1":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "GO1":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# hokuyo_uam
setup_data.update({
    "hokuyo_uam": {
        "DRIVER": "hokuyo_uam", 
        "SETUP": {
            "parameters": {
            },
            "variables": {
                "0_134": {"datatype": VariableDatatype.INTEGER, "size": 135, "operation": VariableOperation.WRITE},
                "135_269": {"datatype": VariableDatatype.INTEGER, "size": 135, "operation": VariableOperation.WRITE},
                "270_404": {"datatype": VariableDatatype.INTEGER, "size": 135, "operation": VariableOperation.WRITE},
                "405_539": {"datatype": VariableDatatype.INTEGER, "size": 135, "operation": VariableOperation.WRITE},
                "540_674": {"datatype": VariableDatatype.INTEGER, "size": 135, "operation": VariableOperation.WRITE},
                "675_809": {"datatype": VariableDatatype.INTEGER, "size": 135, "operation": VariableOperation.WRITE},
                "810_944": {"datatype": VariableDatatype.INTEGER, "size": 135, "operation": VariableOperation.WRITE},
                "945_1080": {"datatype": VariableDatatype.INTEGER, "size": 136, "operation": VariableOperation.WRITE},
            }
        }
    }
})

# kuka_varproxy
setup_data.update({
    "kuka_varproxy": {
        "DRIVER": "kuka_varproxy", 
        "SETUP": {
            "parameters": {
                "ip":"192.168.138.128",
            },
            "variables": {
                "Out_BOOL":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "Out_INTEGER":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "Out_FLOAT":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
                "In_BOOL":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "In_INTEGER":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "In_FLOAT":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "$AXIS_ACT": {"datatype": VariableDatatype.FLOAT, "size": 12, "operation": VariableOperation.READ},
            }
        }
    }
})

# micro800_http
setup_data.update({
    "micro800_http": {
        "DRIVER": "micro800_http", 
        "SETUP": {
            "parameters": {
                "port" : "65173",
            },
            "variables": {
                "_IO_EM_DI_00":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "_IO_EM_DO_00":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# modbustcp_master
setup_data.update({
    "modbustcp_master": {
        "DRIVER": "modbustcp_master", 
        "SETUP": {
            "parameters": {
                "host" : "localhost",
                "port" : 502,
            },
            "variables": {
                "1":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "201":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "10001":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "10301":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "30001":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "30031":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "40001":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "40041":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
            }
        }
    }
})

# mqtt_client
setup_data.update({
    "mqtt_client": {
        "DRIVER": "mqtt_client", 
        "SETUP": {
            "parameters": {
            },
            "variables": {
                "inputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "outputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# omron_fins
setup_data.update({
    "omron_fins": {
        "DRIVER": "omron_fins", 
        "SETUP": {
            "parameters": {
                "ip": "192.168.0.1",
                "dest_node_add": 1,
                "srce_node_add": 25,
            },
            "variables": {
                "d0":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "d1":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "d2":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "d4":{"datatype": VariableDatatype.QWORD, "size": 1, "operation": VariableOperation.WRITE},
                "d8":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "d10":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "d11":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "d12":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "d14":{"datatype": VariableDatatype.QWORD, "size": 1, "operation": VariableOperation.READ},
                "d18":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# omron_nexsocket
setup_data.update({
    "omron_nexsocket": {
        "DRIVER": "omron_nexsocket", 
        "SETUP": {
            "parameters": {
            },
            "variables": {
                "Out_BOOL":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "Out_BYTE":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "Out_WORD":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "Out_DWORD":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "Out_QWORD":{"datatype": VariableDatatype.QWORD, "size": 1, "operation": VariableOperation.READ},
                "Out_INTEGER":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "Out_FLOAT":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
                "In_BOOL":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "In_BYTE":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "In_WORD":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "In_DWORD":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "In_QWORD":{"datatype": VariableDatatype.QWORD, "size": 1, "operation": VariableOperation.WRITE},
                "In_INTEGER":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "In_FLOAT":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
            }
        }
    }
})

# opcda_client
setup_data.update({
    "opcda_client": {
        "DRIVER": "opcda_client", 
        "SETUP": {
            "parameters": {
                "server": "Matrikon.OPC.Simulation.1",
                "client_class": "OPC.Automation.1",
            },
            "variables": {
                "GP2.bool":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "GP2.int":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "GP2.wint":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
            }
        }
    }
})

# opcua_client
setup_data.update({
    "opcua_client": {
        "DRIVER": "opcua_client", 
        "SETUP": {
            "parameters": {
                "url":"opc.tcp://127.0.0.1:4840", 
                "rpi":10,
            },
            "variables": {
                "ByteIn":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "ByteOut":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "BoolIn":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "BoolOut":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "WordIn":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "WordOut":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "IntIn":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "IntOut":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "DWordIn":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "DWordOut":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "DIntIn":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "DIntOut":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "RealIn":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "RealOut":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# plcsim_advanced
setup_data.update({
    "plcsim_advanced": {
        "DRIVER": "plcsim_advanced", 
        "SETUP": {
            "parameters": {
                "instanceName": "drivertest",
            },
            "variables": {
                "ByteIn":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "ByteOut":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "BoolIn":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "BoolOut":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "WordIn":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "WordOut":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "WordInHighAdress":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "WordOutHighAdress":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "IntIn":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "IntOut":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "DWordIN":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "DWordOut":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "DIntIn":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "DIntOut":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "RealIn":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "RealOut":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# plcsim
setup_data.update({
    "plcsim": {
        "DRIVER": "plcsim", 
        "SETUP": {
            "parameters": {
                "ip" : "192.168.1.250",
                "rack" : 0,
                "slot" : 1,
            },
            "variables": {
                "IB0":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "QB0":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "I1.2":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "Q1.2":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "IW2":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "QW2":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "IW10000":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "QW10000":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "IW4":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "QW4":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "ID10":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "QD10":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "ID14":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "QD14":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "ID18":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "QD18":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBB0":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBB1":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBX2.0":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBX2.1":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBW4":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBW6":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBW8":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBW10":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBD12":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBD14":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBD20":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBD24":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBD28":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBD32":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},  
            }
        }
    }
})

# robodk_driver
setup_data.update({
    "robodk_driver": {
        "DRIVER": "robodk_driver", 
        "SETUP": {
            "parameters": {
                "controller":"", 
                "rpi":10,
            },
            "variables": {
                "Axis":{"datatype": VariableDatatype.FLOAT, "size": 6, "operation": VariableOperation.READ},
                "inputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "outputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# robotware
setup_data.update({
    "robotware": {
        "DRIVER": "robotware", 
        "SETUP": {
            "parameters": {
                "controller": "Robot"
            },
            "variables": {
                "Axis":{"datatype": VariableDatatype.FLOAT, "size": 6, "operation": VariableOperation.READ},
                "inputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "outputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# rosbridge
setup_data.update({
    "rosbridge": {
        "DRIVER": "rosbridge", 
        "SETUP": {
            "parameters": {
                "host" : "127.0.0.1",
                "port" : 9090,
            },
            "variables": {
                "test_01":{"datatype": "int", "size": 1, "operation": VariableOperation.WRITE},
                "test_02":{"datatype": "int", "size": 1, "operation": VariableOperation.READ},
                "ros_message_request": {"datatype": "str", "size": 1, "operation": VariableOperation.BOTH},
            }
        }
    }
})

# s7protocol
setup_data.update({
    "s7protocol": {
        "DRIVER": "s7protocol", 
        "SETUP": {
            "parameters": {
                "ip" : "192.168.1.192",
                "rack" : 0,# For Logo! 0
                "slot" : 1,# For Logo! 2
            },
            "variables": {
                "IB0":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "QB0":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "I1.2":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "Q1.2":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "IW2":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "QW2":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "IW10000":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "QW10000":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "IW4":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "QW4":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "ID10":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "QD10":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "ID14":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "QD14":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "ID18":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "QD18":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBB0":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBB1":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBX2.0":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBX2.1":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBW4":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBW6":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBW8":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBW10":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBD12":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBD14":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBD20":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBD24":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "DB12.DBD28":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "DB12.DBD32":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},  
            }
        }
    }
})

# simit
setup_data.update({
    "simit": {
        "DRIVER": "simit", 
        "SETUP": {
            "parameters": {
                "SHM_name" : "SIMITShared Memory",
                "big_endian" : False,
            },
            "variables": {
                "MW4":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "MW0":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# sqlite3_conn
ADDRESS = "C:\TEMP\mydb.db"
'''
connection = sqlite3.connect(ADDRESS)
cursor = connection.cursor()
cursor.execute("SELECT count(name) FROM sqlite_master WHERE type="table" AND name="variables"")
if cursor.fetchone()[0] != 1:
    cursor.execute("""CREATE TABLE variables (name TEXT, value TEXT)""")		
    cursor.execute("""INSERT INTO variables (name, value) VALUES ("inputs", "0")""")		
    cursor.execute("""INSERT INTO variables (name, value) VALUES ("outputs", "11")""")		
connection.commit()
connection.close()
'''
setup_data.update({
    "sqlite3_conn": {
        "DRIVER": "sqlite3_conn", 
        "SETUP": {
            "parameters": {
                "address": ADDRESS,
            },
            "variables": {
                "inputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "outputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# twincat_ads
setup_data.update({
    "twincat_ads": {
        "DRIVER": "twincat_ads", 
        "SETUP": {
            "parameters": {
                "net_id" : "192.168.1.125.1.1",
                "port" : 851,
            },
            "variables": {
                "GVL.ByteIn":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "GVL.ByteOut":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "GVL.BoolIn":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "GVL.BoolOut":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
                "GVL.WordIn":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.WRITE},
                "GVL.WordOut":{"datatype": VariableDatatype.WORD, "size": 1, "operation": VariableOperation.READ},
                "GVL.IntIn":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "GVL.IntOut":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "GVL.DWordIn":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.WRITE},
                "GVL.DWordOut":{"datatype": VariableDatatype.DWORD, "size": 1, "operation": VariableOperation.READ},
                "GVL.DIntIn":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.WRITE},
                "GVL.DIntOut":{"datatype": VariableDatatype.INTEGER, "size": 1, "operation": VariableOperation.READ},
                "GVL.RealIn":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.WRITE},
                "GVL.RealOut":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# udp_generic
setup_data.update({
    "udp_generic": {
        "DRIVER": "udp_generic", 
        "SETUP": {
            "parameters": {
            },
            "variables": {
                "inputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "outputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# universal_robots
setup_data.update({
    "universal_robots": {
        "DRIVER": "universal_robots", 
        "SETUP": {
            "parameters": {
            },
            "variables": {
                "actual_q":{"datatype": VariableDatatype.FLOAT, "size": 6, "operation": VariableOperation.READ},
                "input_bit_register_64":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.WRITE},
                "output_bit_register_64":{"datatype": VariableDatatype.BOOL, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})

# yaskawa_plci
setup_data.update({
    "yaskawa_plci": {
        "DRIVER": "yaskawa_plci", 
        "SETUP": {
            "parameters": {
                "ip": "192.168.240.1",
            },
            "variables": {
                "Test_input":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.WRITE},
                "Test_output":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "Test_outputs":{"datatype": VariableDatatype.BYTE, "size": 1, "operation": VariableOperation.READ},
                "AxisControlRetrieval_SliderX2.ActPos":{"datatype": VariableDatatype.FLOAT, "size": 1, "operation": VariableOperation.READ},
            }
        }
    }
})