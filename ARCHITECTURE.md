# Structure

The Gateway code base is found in the scr folder. Inside, you can find the main program (gateway.py), and test and driver folders. All the drivers inside /driver are organized in different subfolders and they have their testing class in /test.

# Gateway

Its role is to manage the different drivers for allowing 3rd party integration and to communicate with the App and the Server. A WebSocket connection is used for the App and a UDP socket for the Server. In both cases the data is sent using JSON messages. 

## App communication

The Simumatik App controls the Gateway and it's main role is to start the communication between the Gateway and the Server by providing the needed parameters.

### Commands

- **Connect**: Connect the gateway to the server with the given ip address.

    App request:
    ```json
    {"request": {"id": 1, "command": "connect", "data": {"ip": "127.0.0"}}}
    ```
    Gateway response:
    ```json
    {"response": {"id": 0, "command": "connect", "data": {"status": "error / connected", "message": "<error>"}}}
    ```

- **Disconnect**: Disconnect the gateway from the server.

    App request:
    ```json
    {"request": {"id": 1, "command": "disconnect"}}
    ```
    Gateway response:
    ```json
    {"response": {"id": 0, "command": "disconnect", "data": {"status": "error / disconnected", "message": "<error>"}}}
    ```

- Reset: Reset the gateway if an error has ocurred.

    App request:
    ```json
    {"request": {"id": 1, "command": "reset"}}
    ```
    Gateway response:
    ```json
    {"response": {"id": 0, "command": "reset", "data": {"status": "error / reseted", "message": "<error>"}}}
    ```

- **Status**: Ask for the current status of the gateway.

    App request:
    ```json
    {"request": {"id": 1, "command": "status"}}
    ```
    Gateway response:
    ```json
    {"response": {"id": 0, "command": "status", "data": {"status": "error / <status>", "message": "<error>"}}}
    ```

- **Version**: Ask for the gateway version.

    App request:
    ```json
    {"request": {"id": 1, "command": "version"}}
    ```
    Gateway response:
    ```json
    {"response": {"id": 0, "command": "version", "data": {"status": "<version>"}}}
    ```

## Server commmunication

The Simumatik Server requests drivers creation/removal on-demand to the Gateway. Once the connection between is established, the commands and I/O data are exchanged in a loop following an interval time.

### Commands

- **REGISTER**: . This message is sent by the Gateway just after the connection is done contains the driver handle, type and the setup data, explained more in detail below.

    Gateway request:
    ```json
    {"ID": "<msg_id>", "COMMAND": "REGISTER", "DATA": {
                                                    "SERVER_KEY": "server key obtained from the user",
                                                    "GATEWAY": {
                                                        "HEARTBEAT": "<heartbeat>", 
                                                        "VERSION": "<version>"
                                                        },
                                                    "DRIVERS": ["<driver_type>"],
                                                    }}
    ```
    Server response:
    ```json
    {"ID": "<request_msg_id>", "COMMAND": "REGISTER", "DATA": "SUCCESS / FAILED"}
    ```

- **SETUP**: Create a new driver. This message contains the driver handle, type and the setup data, explained more in detail below.

    Server request:
    ```json
    {"ID": "<msg_id>", "COMMAND": "SETUP", "DATA": {"<driver_handle>": {"DRIVER": "<driver_type>", "SETUP": "<setup_data>"}}}
    ```
    Gateway response:
    ```json
    {"ID": "<request_msg_id>", "COMMAND": "SETUP", "DATA": {"driver_handle": "SUCCESS / FAILED"}}
    ```

- **CLEAN**: Remove all drivers.

    Server request:
    ```json
    {"ID": "<msg_id>", "COMMAND": "CLEAN", "DATA": "None"}
    ```
    Gateway response:
    ```json
    {"ID": "<request_msg_id>", "COMMAND": "CLEAN", "DATA": "SUCCESS / FAILED"}
    ```

- **POLLING**: This is just a signal to update the polling timestamp. If no messages are detected in a time period, the connection is automatically closed.

    Server/Gateway request:
    ```json
    {"ID": "<msg_id>", "COMMAND": "POLLING", "DATA": {"LAST_PROC_UPDATE": "<last proccessed UPDATE telegram id>"}
    ```

- **UPDATE**: Update a driver I/O data. It uses the unique variable handle assigned on setup and a dict with the var handle and new value.

    Server/Gateway request:
    ```json
    {"ID": "<msg_id>", "COMMAND": "UPDATE", "DATA": {"<var_handle>" : "<var_value>"}}
    ```

- **STATUS**: If a driver's status changes, the Gateway will notify the server.

    Gateway request:
    ```json
    {"ID": "<msg_id>", "COMMAND": "STATUS", "DATA": {"<driver_handle>":"<driver_status>"}}
    ```

- **INFO**: If a driver displays some debug msg using `self.sendDebugInfo`, the Gateway will notify the server.

    Gateway request:
    ```json
    {"ID": "<msg_id>", "COMMAND": "INFO", "DATA": {"<driver_handle>":"<driver_info>"}}
    ```

- **VAR_INFO**: If a driver displays some debug msg using `self.sendDebugVarInfo`, the Gateway will notify the server.

    Gateway request:
    ```json
    {"ID": "<msg_id>", "COMMAND": "VAR_INFO", "DATA": {"<var_handle>":"<driver_info>"}}
    ```
# Driver

The base driver class is found in driver/driver.py. It is an abstract class that guides the communication between the Gateway main thread and the specific drivers. Every driver must inherit it and call its parent:

```python
from ..driver import driver

class example_driver(driver):

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.url = 'opc.tcp://localhost:4840'
```

Each driver is launched in a separate thread, using a Pipe for the communication. The information is exchanged using JSON messages enconded as a string. It's the Gateway role to create the driver on-demand with a specific name and pipe.

The init class is also used to declare some driver specific parameter with sane defaults. These parameter will be automatically updated with the setup information received from the Simumatik components.

## Pipe interface

The following table shows the possible messages sent through the pipe to and from the driver:

|DIRECTION    | ACTION    | MESSAGE DATA                            |
|-------------|-----------|-----------------------------------------|
|To driver    | SETUP     | {'SETUP': {"setup data here"}           |
|To driver    | UPDATE    | {'UPDATE':{"address_name": "value"}}    |
|To driver    | RESET     | {'RESET': 'None'}                       |
|To driver    | EXIT      | {'EXIT': 'None'}                        |
|From driver  | UPDATE    | {'UPDATE':{"address_name": "value"}}    |
|From driver  | STATUS    | {'STATUS': "actual status"}             |
|From driver  | INFO      | {'INFO': "debug info"}|

## Status:

The driver exposes the following status to the Gateway:

1. **STANDBY**: Starting state once launched. The driver is not performing any operation and is waiting to the setup message. When received, it moves to RUNNING state. If any error occurs during setup it jumps to ERROR.

2. **RUNNING**: The driver is running normally, receiving and sending updates through the pipe. If any error occurs, it jumps to ERROR state.

3. **ERROR**: The driver is not performing any operation and is waiting to the reset message to cleanup and move back to STANDBY state. If any error occurs during cleanup remains at ERROR state.

When EXIT action is received at any states, the driver does the cleaunp and the thread is finished.

## Setup data

The setup data includes two parts:

- **Parameters**: Specific for each driver, they are defined by a dict that may include several parameters following the next format {parameter_name: parameter_value}, i.e: 

    ```json
        {
            "ip": "192.168.0.1", 
            "port": 1234
        }
    ```

- **Variables**: These are the variables to be accessed in the controller, read and written through the driver. The variables are defined by a dict that may include several definitions following the next format {address: {'datatype':str, 'size':int, 'operation':str}: 

    - address: str -> can be used as name, tag, id, or simply to identify the variable.
    - datatype: str (VariableDatatype) -> is used to define the variable data type.
    - size: int -> to define if the variable is an array. If not defined it is asumed is not an array or dimension 1.
    - operation: str (VariableOperations) -> to define if the variable should be written or read by the driver in the controller.

    An example of the variable definition:

    ```json
        {
            "input": {
                "datatype": "byte", 
                "size": 1, 
                "operation": "write"
            },
            "output": {
                "datatype": "byte", 
                "size": 2, "operation": "read"
            }
        }
    ```

A complete example of the SETUP message:

```json
    {
        "SETUP": {
            "parameters": {
                "ip": "192.168.0.1", 
                "port": 1234},
            "variables": {
                "input": {
                    "datatype": "byte", 
                    "size": 1,
                    "operation": "write"
                },
                "output": {
                    "datatype": "byte", 
                    "size": 2, 
                    "operation": "read"
                }
            }
        }
    }
```

## Lifecycle

1. On driver creation the \__init\__ method is called and the default parameters are set.

2. Afterwards, the connect method is called, which uses the class parameters overwritten with the setup["parameters"] data received from the Server. The client used for the connection should be saved on `self._connection`.

3. If successful, the addVariables method is called. It receives as a parameter the variables declaration found in setup["variables"]. Its role is to register the variables to exchange and add them to `self.variables`:

    ```python
    for var_id, var_data in variables.items():
        # Register var in 3rd party
        # ......

        # If successful, set default value and add it to self.variables
        var_data['value'] = 0
        self.variables[var_id] = var_data
    ````

4. At this point, the communication loop begins. The methods readVariables and writeVariables are called to exchange the data. They receive the var_id (and var_data when writting) as the Gateway expects a list back with each variable state (tuple containing var id, var value and var status):

    ```python
    res = []

    for var_id in variables:
        # Read var data from 3rd party
        # ....

        # If successful, add it with VariableQuality.GOOD. Otherwise, use VariableQuality.BAD
        # Variables declaration data can be accessed using self.variables[var_id] 
        res.append((var_id, self.variables[var_id]['value'], VariableQuality.GOOD))
    
    return res
    ```

5. Finally, on driver clean-up the method disconnect is called.

## Manual usage

The driver is launched as a thread. First the multiprocessing library needs to be imported to include the class Pipe:

```python
from multiprocessing import Pipe
```

Then the a pipe is created:

```python
m_pipe, p_pipe = Pipe()
```

After that, the driver can be created by providing a name and a pipe-end:

```python
d = driver('test', p_pipe)
```

Finally, the driver thread is launched:

```python
d.start()
```

You can use the pipe communication protocol showed above to exchange the information with the driver.

## Datamodel relation

All the drivers developed on the Gateway must be declared on the Datamodel to make them available for the Simumatik components. A relation table can be found in `drivers/__init__.py`, which pairs the drivers names with the right Gateway class.