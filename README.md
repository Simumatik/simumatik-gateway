# Simumatik Gateway

The Gateway is a middleware between the Simumatik platform and other 3rd party platforms. It defines a generic communication driver based on a thread, used as a base to developed specific driver compatible with any platform, including PLCs and Robots among others.

## Getting Started
Assuming that you have Python3 and Pip installed, you need to clone the repository and install the dependencies:

```Shell
git clone https://github.com/Simumatik/simumatik-gateway.git
cd simumatik-gateway
pip install -r requirements.<os>
```

You are now ready to launch it. You can use the debug flag to see all the messages:
```Shell
python src/gateway.py debug
```

Finally, go to the Simumatik App and connect to the Gateway. You have more information available in the [learning documentation](https://simumatik.com/learn/Gateway/gateway/#gateway-connection).

Keep in mind that some drivers will need a special setup-up to work. Don't forget to check their code for more information about dependencies.

The current dependencies only work up to Python 3.8 32bit

## Drivers available

Right now, the following drivers are supported in the Gateway:

- ACS SPiiPlus
- Allen Bradley Logix
- CPRog CRI
- Development (own purpose)
- EthernetIP Generic Device
- Fanuc Roboguide
- Hokuyo UAM
- Kuka VarProxy
- Micro800 HTTP (Rockwell Automation CCW)
- Modbus TCP
- MQTT client
- OPCUA client
- OPCDA Client
- Siemens PLCSim
- Siemens PLCSim Advanced
- RoboDK
- RobotWare (ABB RobotStudio)
- ROSBridge
- S7Protocol
- Siemens Simit (using shared memory)
- SQLite3
- Twincat ADS
- UDP generic
- Universal Robots
- YAskawa PLCi

## Architecture

You can learn more about the Gateway design and structure on the [Architecture](ARCHITECTURE.md) section, which walks through the most imports part of the code base.

## Contributing

Before opening an issue or PR, please read the content in the [Contributing](CONTRIBUTING.md) section.


## Build

It is possible to build an distributable package of the Gateway using pyinstaller library. To do so, simply run the next command:

```Shell
pyinstaller gateway_package.spec
```

The executable file and all additional files will be included inside the folder dist/gateway.
