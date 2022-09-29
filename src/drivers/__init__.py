import platform

from drivers.rosbridge.rosbridge import rosbridge

from .driver import driver, DriverActions, DriverStatus

from .allenbradley_logix.allenbradley_logix import allenbradley_logix
from .cprog_cri.cprog_cri import cprog_cri
from .development.development import development
from .hokuyo_uam.hokuyo_uam import hokuyo_uam
from .matlab_udp.matlab_udp import matlab_udp
from .micro800_http.micro800_http import micro800_http
from .modbustcp_master.modbustcp_master import modbustcp_master
from .mqtt_client.mqtt_client import mqtt_client
from .opcua_client.opcua_client import opcua_client
from .rosbridge.rosbridge import rosbridge
from .s7protocol.s7protocol import s7protocol
from .simit import simit
from .sqlite3_conn import sqlite3_conn
from .twincat_ads import twincat_ads
from .udp_generic.udp_generic import udp_generic
from .universal_robots.universal_robots import universal_robots

# Dict relating drivers with datamodel definition
# NOTE: Datamodel names will be updated to match drivers name
registered_drivers = {
  "allenbradley_logix": (allenbradley_logix, "1"),
  "cprog_cri": (cprog_cri, "1"),
  "development": (development,"1"),
  "hokuyo_uam": (hokuyo_uam,"1"),
  "micro800_http": (micro800_http, "1"),
  "matlab_udp": (matlab_udp, "1"),
  "modbustcp_master": (modbustcp_master,"1"),
  "mqtt_client": (mqtt_client,"1"),
  "opcua_client": (opcua_client, "1"),
  "rosbridge": (rosbridge, "1"),
  "s7protocol": (s7protocol, "1"),
  "simit" : (simit, "1"),
  "sqlite3_conn" : (sqlite3_conn, "1"),
  "twincat_ads" : (twincat_ads, "1"),
  "udp_driver": (udp_generic,"1"),
  "ur_driver": (universal_robots, "1"), # TODO: Fix. Name is different to retrocompatibility
}

if platform.system() == "Windows":
    from .fanuc_roboguide.fanuc_roboguide import fanuc_roboguide
    from .opcda_client.opcda_client import opcda_client
    from .robotware.robotware import robotware
    from .robodk_api.robodk_api import robodk_api
    registered_drivers.update({"opcda_client": (opcda_client, "1")})
    registered_drivers.update({"fanuc_roboguide": (fanuc_roboguide, "1")})
    registered_drivers.update({"abb_driver": (robotware,"1")}) # TODO: Fix. Name is different to retrocompatibility
    registered_drivers.update({"robodk_driver": (robodk_api, "1")}) # TODO: Fix. name is different to retrocompatibility
