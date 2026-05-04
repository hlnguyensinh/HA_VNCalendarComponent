from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_change

from .vnlunarcache import VNLunarCache
from .const import (DOMAIN, BSENSOR_VEGDAY_UNIQUE_NAME, BSENSOR_VEGDAY_UNIQUE_ID, BSENSOR_GOODHOUR_UNIQUE_NAME, BSENSOR_GOODHOUR_UNIQUE_ID)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    lunarCache = hass.data[DOMAIN][entry.entry_id]["cache"]

    async_add_entities(
        [
            VnLunarVegBinarySensor(hass, lunarCache),
            VnLunarGoodHourSensor(hass, lunarCache),
        ]
    )


class VnLunarVegBinarySensor(BinarySensorEntity):
    _attr_icon = "mdi:leaf"

    def __init__(self, hass, lunarCache):
        self.hass = hass
        self.lunar = lunarCache

        self._attr_name = BSENSOR_VEGDAY_UNIQUE_NAME
        self._attr_unique_id = BSENSOR_VEGDAY_UNIQUE_ID

        self.delaysecs = 5

        self._attr_is_on = False

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

        self._attr_is_on = dayinfo["isVeg"]

    @property
    def is_on(self):
        return self._attr_is_on


class VnLunarGoodHourSensor(BinarySensorEntity):

    def __init__(self, hass, lunarCache):
        self.hass = hass
        self.lunar = lunarCache

        self._attr_name = BSENSOR_GOODHOUR_UNIQUE_NAME
        self._attr_unique_id = BSENSOR_GOODHOUR_UNIQUE_ID

        self.delaysecs = 5

        self._attr_is_on = False
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
        hourinfo = self.lunar.get_current_hour_info_today()

        self._attr_is_on = hourinfo["isgoodhour"]
        self._attributes = {
            "hour": hourinfo["hour"],
            "range": hourinfo["range"]
        }

    @property
    def is_on(self):
        return self._attr_is_on

    @property
    def extra_state_attributes(self):
        return self._attributes
    
    @property
    def icon(self):
        return (
            "mdi:clock-check"
            if self.is_on
            else "mdi:clock-remove"
    )
    
####--------------------------------------------------------------------

# if __name__ == "__main__":

#     class FakeHass:
#         pass

#     clsLunar = VNLunarCache()

#     sensor = VnLunarGoodHourSensor(FakeHass(), clsLunar)

#     sensor.update_lunar()

#     print(sensor.state)
#     print(sensor.extra_state_attributes)

