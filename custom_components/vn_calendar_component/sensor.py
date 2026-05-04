from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_change

from .vnlunarcache import VNLunarCache
from .const import (
    DOMAIN,
    SENSOR_LUNARTODAY_UNIQUE_NAME,
    SENSOR_LUNARTODAY_UNIQUE_ID,
    SENSOR_DAYTYPE_UNIQUE_NAME,
    SENSOR_DAYTYPE_UNIQUE_ID,
    SENSOR_SOLARTERM_UNIQUE_NAME,
    SENSOR_SOLARTERM_UNIQUE_ID,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    lunarCache = hass.data[DOMAIN][entry.entry_id]["cache"]

    async_add_entities(
        [VnLunarTodaySensor(hass, lunarCache), VnLunarDayTypeSensor(hass, lunarCache)]
    )


class VnLunarTodaySensor(SensorEntity):
    _attr_icon = "mdi:calendar-month"

    def __init__(self, hass, lunarCache):
        self.hass = hass
        self.lunar = lunarCache

        self._attr_name = SENSOR_LUNARTODAY_UNIQUE_NAME
        self._attr_unique_id = SENSOR_LUNARTODAY_UNIQUE_ID

        self.delaysecs = 5

        self._state = None
        self._attributes = {}

    async def async_added_to_hass(self):
        self.update_lunar()
        self.async_write_ha_state()

        async_track_time_change(
            self.hass,
            self._handle_time_change,
            hour=0,
            minute=0,
            second=self.delaysecs,
        )

    async def _handle_time_change(self, now):
        self.update_lunar()
        self.async_write_ha_state()

    def update_lunar(self):
        dayinfo = self.lunar.today()

        self._state = f"{dayinfo['lunar']['day']}/{dayinfo['lunar']['month']}/{dayinfo['lunar']['year']}"
        self._attributes = {
            "day": dayinfo["lunar"]["canchi"]["day"],
            "month": dayinfo["lunar"]["canchi"]["month"],
            "year": dayinfo["lunar"]["canchi"]["year"],
            "events": dayinfo["lunar"]["events"],
        }

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes


class VnLunarDayTypeSensor(SensorEntity):
    _attr_icon = "mdi:flower-poppy"

    def __init__(self, hass, lunarCache):
        self.hass = hass
        self.lunar = lunarCache

        self._attr_name = SENSOR_DAYTYPE_UNIQUE_NAME
        self._attr_unique_id = SENSOR_DAYTYPE_UNIQUE_ID

        self.delaysecs = 5

        self._state = None
        self._attributes = {}

    async def async_added_to_hass(self):
        self.update_lunar()
        self.async_write_ha_state()

        async_track_time_change(
            self.hass,
            self._handle_time_change,
            hour=0,
            minute=0,
            second=self.delaysecs,
        )

    async def _handle_time_change(self, now):
        self.update_lunar()
        self.async_write_ha_state()

    def update_lunar(self):
        dayinfo = self.lunar.today()

        self._state = f"{dayinfo['dayType'][0]}"
        self._attributes = {
            "dayType": dayinfo["dayType"],
            "goodhours": dayinfo["goodHours"],
        }

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes


class VnLunarSolarTermSensor(SensorEntity):
    _attr_icon = "mdi:weather-dust"

    def __init__(self, hass, lunarCache):
        self.hass = hass
        self.lunar = lunarCache

        self._attr_name = SENSOR_SOLARTERM_UNIQUE_NAME
        self._attr_unique_id = SENSOR_SOLARTERM_UNIQUE_ID

        self.delaysecs = 5

        self._state = None
        self._attributes = {}

    async def async_added_to_hass(self):
        self.update_lunar()
        self.async_write_ha_state()

        async_track_time_change(
            self.hass,
            self._handle_time_change,
            hour=0,
            minute=0,
            second=self.delaysecs,
        )

    async def _handle_time_change(self, now):
        self.update_lunar()
        self.async_write_ha_state()

    def update_lunar(self):
        dayinfo = self.lunar.today()

        self._state = f"{dayinfo['solarTerm'][0]}"
        self._attributes = {"solarTerm": dayinfo["solarTerm"]}

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes


####--------------------------------------------------------------------

# if __name__ == "__main__":

#     class FakeHass:
#         pass

#     clsLunar = VNLunarCache()

#     sensor = VnLunarSolarTermSensor(FakeHass(), clsLunar)

#     sensor.update_lunar()

#     print(sensor.state)
#     print(sensor.extra_state_attributes)
