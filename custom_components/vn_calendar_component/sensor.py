from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_change

from .const import DOMAIN, SENSOR_LUNARTODAY_UNIQUE_ID, SENSOR_LUNARTODAY_UNIQUE_NAME


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    lunarCache = hass.data[DOMAIN][entry.entry_id]["cache"]

    async_add_entities([VnLunarLunarTodaySensor(hass, lunarCache)])


class VnLunarLunarTodaySensor(SensorEntity):
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

        self._state = f"{dayinfo['lunar']['day']}/{dayinfo['lunar']['month']}"
        self._attributes = dayinfo

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

#     sensor = VnLunarLunarTodaySensor(FakeHass(), clsLunar)

#     sensor.update_lunar()

#     print(sensor.state)
#     print(sensor.extra_state_attributes)

