import platform

from .driver import driver, DriverActions, DriverStatus

from .cprog_cri.cprog_cri import cprog_cri
from .micro800_http.micro800_http import micro800_http
from .development.development import development
from .mqtt_client.mqtt_client import mqtt_client
from .opcua_client.opcua_client import opcua_client
from .s7protocol.s7protocol import s7protocol
from .udp_generic.udp_generic import udp_generic
from .universal_robots.universal_robots import universal_robots
from .fanuc_roboguide.fanuc_roboguide import fanuc_roboguide
from .twincat_ads import twincat_ads
from .simit import simit
from .sqlite3_conn import sqlite3_conn

# Dict relating drivers with datamodel definition
# NOTE: Datamodel names will be updated to match drivers name
registered_drivers = {
  "cprog_cri": (cprog_cri, "1"),
  "development": (development,"1"),
  "mqtt_client": (mqtt_client,"1"),
  "opcua_client": (opcua_client, "1"),
  "s7protocol": (s7protocol, "1"),
  "udp_driver": (udp_generic,"1"),
  "ur_driver": (universal_robots, "1"),
  "micro800_http": (micro800_http, "1"),
  "twincat_ads" : (twincat_ads, "1"),
  "simit" : (simit, "1"),
  "sqlite3_conn" : (sqlite3_conn, "1"),
}

if platform.system() == "Windows":
    from .robotware.robotware import robotware
    from .robodk.robodk import robodk
    registered_drivers.update({"abb_driver": (robotware,"1")})
    registered_drivers.update({"robodk_driver": (robodk, "1")})
    registered_drivers.update({"fanuc_roboguide": (fanuc_roboguide, "1")})
