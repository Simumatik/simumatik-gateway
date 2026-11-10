# Simumatik Gateway

The Gateway is a middleware between the Simumatik platform and other 3rd party platforms. It defines a generic communication driver based on a thread, used as a base to developed specific driver compatible with any platform, including PLCs and Robots among others.

## Getting Started
Assuming that you have Python3 and Pip installed, you need to clone the repository and install the dependencies:

```Shell
git clone https://github.com/Simumatik/simumatik-gateway.git
cd simumatik-gateway
pip install -r requirements.txt
```

You are now ready to launch it. You can use the debug flag to see all the messages:
```Shell
python src/gateway.py debug
```

Finally, go to the Simumatik App and connect to the Gateway. You have more information available in the [learning documentation](https://simumatik.com/learn/Gateway/gateway/#gateway-connection).

Keep in mind that some drivers will need a special setup-up to work. Don't forget to check their code for more information about dependencies.

The current dependencies only work up to Python 3.11 32bit

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
- Omron FINS
- Omron NexSocket (Sysmac Simulator)
- OPCUA client
- OPCDA Client
- Siemens PLCSim
- Siemens PLCSim Advanced
- RoboDK
- RobotWare (ABB RobotStudio)
- ROSBridge
- S7Protocol
- Siemens Simit (using shared memory)
- Simulink UDP
- SQLite3
- Twincat ADS
- UDP generic
- Universal Robots
- Yaskawa PLCi

## Architecture

You can learn more about the Gateway design and structure on the [Architecture](ARCHITECTURE.md) section, which walks through the most imports part of the code base.

## Contributing

Before opening an issue or PR, please read the content in the [Contributing](CONTRIBUTING.md) section.


## Build

### Manual build 
It is possible to build a distributable package of the Gateway using the PyInstaller library. To do so, simply run the following command:

```Shell
pyinstaller gateway_package.spec
```

The executable file and all additional files will be included inside the folder dist/gateway.

### Github Action workflow

The Github Actions workflow "Manual Build and Sign" can be triggered manually from the repository in Github. The workflow builds and signs the executable and uploads result as a temporary Github artifact (valid for 90 days).
