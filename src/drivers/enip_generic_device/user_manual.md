# User manual

To test this driver you just need to get access to a Ethernet/IP master, which can be emulated by using for example Codesys.

## Test with Codesys

1. Create a project with Control Win V3 or the RPI equivalent.
2. Add an Ethernet (Ethernet) module from Ethernet/IP section as a new device.
3. Inside the Ethernet module, add an Ethernet_IP_Scanner module.
4. Inside the Ethernet_IP_Scanner module, add an Generic_Ethernet_IP_device.
5. Be aware that Codesys gateway is enabled and connected (double click on Control Win V3 device to verify).
6. Double click on the Ethernet module, and select the interface you are using, such as wifi or ethernet.
7. Double click on the Generic_Ethernet_IP_device, set the IP of the ENIP driver, set Strict Compatiblity Check, and uncheck every check in the general tab.
8. Still in the Generic_Ethernet_IP_device, choose the Connections tab and click add connections. 
9. In connection-path add '20 04 2C 66 2C 6C'. Set O->T and T->O bytes to '1'. Set Connection type in both cases to 'Point to point' and to 'Fixed'. In the left, set the data to '32 bits run/idle', and in the right to 'pure data'
10. Now you can compile, go online, and run the driver with the following config:

```
setup = {DriverActions.SETUP: {'parameters': {'driver_ip':'<IP_ADDRESS>', 'connection_path':'', 'read_size':1, 'write_size':1},
                                'data': {'input_data': {'datatype':'str', 'size':1, 'operation':'write'},
                                         'output_data': {'datatype':'str', 'size':1, 'operation':'read'}
                                        }
                              }
        }
```