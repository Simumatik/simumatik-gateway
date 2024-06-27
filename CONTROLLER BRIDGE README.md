# SIMUMATIK CONTROLLER BRIDGE


## Perparation

The file "Controller_Bridge_Setup.json" defines the app configuration. It has two parts, "drivers" and "connections":

```
{
    "drivers":{
        drivers here...
    },
    "connections":{
        connections here....
    }
}
```

### Drivers:

Here we can define several drivers to be created. Each of them will have a unique identifier "Driver_1" below.

```
{
    "drivers":{
        "Driver_1": {
            "DRIVER": "opcua_client", 
            "SETUP": {
                "parameters": {
                    "url":"opc.tcp://127.0.0.1:4840", 
                    "rpi":6
                },
                "variables": {
                    "inputs_1":{"handle":"h0001", "datatype": "word", "size": 1, "operation": "write","invert_byte_order":true},
                    "outputs_1":{"handle":"h0002", "datatype": "word", "size": 1, "operation": "read"}
                }
            }
        },
        ...
    }
}
```

Each driver should include a valid driver type ("DRIVER"), "opcua_client" in the example. Check the Simumatik Manual in the following link: https://docs.simumatik.com/datamodel/communication_driver/

The "SETUP" includes 2 parts "parameters" and "variables". 

- "parameters": These are special key/values depending on each driver type. You can find them in the previous link by selecting the corresponding driver type. Note that all drivers have the "rpi", "forcewrite", and "auto_reset" keys with default values as explained in the documentation.

- "variables" These are the variable definitions to read or write with the driver. Each entry has the variable address (str) which can be the name, tag, id, address or anything to identify the variable depending on the driver. For each address we define 4 parameters.
    - "handle" (str): is a unique identifier to be used later for the connections.
    - "datatype" (str): is used to define the variable data type (bool, byte, int, word, dword, qword, float, str).
    - "size" (int): It defines if the variable is an array. If not defined it is asumed is not an array or dimension 1.
    - "operation" (str): It defines if the variable should be written or read by the driver in the controller (read, write).
    - "invert_byte_order" (bool): When the datatype is "word", "dword" or "qword" this flag can invert the order after reading or before writing.

### Connections

The "connections" part is just a dictionary with the handles to be connected to each other. {<read_variable_handle>:<write_variable_handle>}. Note that it is also possible to write to several variables by using a list as below: 

```
    "connections":{
        "h0002":["h0003","h0004"],
        "h0005": "h0001",
        ...
    }
```

## Execution

Once the Setup file is defined, run the 'ControllerBridge.exe' file. A Command window will open and some logs will be shown telling how many drivers have been created.

To close the application just close the command window.

## Debugging

In order to know what is going on inside the bridge and monitor the status of the drivers and their values, you can open the file named "Driver_Manager_status.txt" in the notepad or any other text editor. The file is updated every second.

## Suport

For any doubts or questions pleas contact us at support@simumatik.com.