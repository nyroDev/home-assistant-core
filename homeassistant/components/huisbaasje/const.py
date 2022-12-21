"""Constants for the Huisbaasje integration."""
from energyflip.const import (
    SOURCE_TYPE_ELECTRICITY,
    SOURCE_TYPE_ELECTRICITY_IN,
    SOURCE_TYPE_ELECTRICITY_IN_LOW,
    SOURCE_TYPE_ELECTRICITY_OUT,
    SOURCE_TYPE_ELECTRICITY_OUT_LOW,
    SOURCE_TYPE_GAS,
)

from homeassistant.const import UnitOfTime, UnitOfVolume

DATA_COORDINATOR = "coordinator"

DOMAIN = "huisbaasje"

FLOW_CUBIC_METERS_PER_HOUR = f"{UnitOfVolume.CUBIC_METERS}/{UnitOfTime.HOURS}"

"""Interval in seconds between polls to huisbaasje."""
POLLING_INTERVAL = 20

"""Timeout for fetching sensor data"""
FETCH_TIMEOUT = 10

SENSOR_TYPE_RATE = "rate"
SENSOR_TYPE_THIS_DAY = "thisDay"
SENSOR_TYPE_THIS_WEEK = "thisWeek"
SENSOR_TYPE_THIS_MONTH = "thisMonth"
SENSOR_TYPE_THIS_YEAR = "thisYear"

SOURCE_TYPES = [
    SOURCE_TYPE_ELECTRICITY,
    SOURCE_TYPE_ELECTRICITY_IN,
    SOURCE_TYPE_ELECTRICITY_IN_LOW,
    SOURCE_TYPE_ELECTRICITY_OUT,
    SOURCE_TYPE_ELECTRICITY_OUT_LOW,
    SOURCE_TYPE_GAS,
]
