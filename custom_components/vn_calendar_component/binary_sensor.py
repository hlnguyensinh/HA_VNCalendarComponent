from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_change

from .const import DOMAIN, BSENSOR_VEGDAY_UNIQUE_ID, BSENSOR_VEGDAY_UNIQUE_NAME


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    lunarCache = hass.data[DOMAIN][entry.entry_id]["cache"]

    async_add_entities(
        [
            VnLunarVegBinarySensor(hass, lunarCache),
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
    
####--------------------------------------------------------------------

# if __name__ == "__main__":

#     class FakeHass:
#         pass

#     clsLunar = VNLunarCache()

#     sensor = VnLunarVegBinarySensor(FakeHass(), clsLunar)

#     sensor.update_lunar()

#     print(sensor.state)
#     print(sensor.extra_state_attributes)

