from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse
from homeassistant.config_entries import ConfigEntry
from .validators import *

from .const import (
    DOMAIN,
    SERVICE_TODAY,
    SERVICE_GET_DAY,
    SERVICE_GET_MONTH,
    SERVICE_GET_YEAR,
    SERVICE_CLEANUP,
    SERVICE_GOOD_HOURS,
    SERVICE_GOOD_HOURS_TODAY,
)


async def async_setup_services(hass: HomeAssistant, entry: ConfigEntry) -> None:
    clsLogger = hass.data[DOMAIN][entry.entry_id]["logger"]
    
    if hass.services.has_service(DOMAIN, SERVICE_TODAY):
        return
    if hass.services.has_service(DOMAIN, SERVICE_GET_DAY):
        return
    if hass.services.has_service(DOMAIN, SERVICE_GET_MONTH):
        return
    if hass.services.has_service(DOMAIN, SERVICE_GET_YEAR):
        return
    if hass.services.has_service(DOMAIN, SERVICE_CLEANUP):
        return
    if hass.services.has_service(DOMAIN, SERVICE_GOOD_HOURS):
        return
    if hass.services.has_service(DOMAIN, SERVICE_GOOD_HOURS_TODAY):
        return
    
    lunarCache = hass.data[DOMAIN][entry.entry_id]["cache"]
    
    async def handle_today(call: ServiceCall):
        # clsLogger.log("services.py","async_setup_services","handle_today called")
        return lunarCache.today()

    async def handle_get_day(call: ServiceCall):
        # clsLogger.log("services.py","async_setup_services","handle_get_day called")
        day = call.data[PARAM_DAY]
        month = call.data[PARAM_MONTH]
        year = call.data[PARAM_YEAR]

        result = lunarCache.get(
            day,
            month,
            year,
        )

        return result

    async def handle_get_month(call: ServiceCall):
        # clsLogger.log("services.py","async_setup_services","handle_get_month called")
        year = call.data[PARAM_YEAR]
        month = call.data[PARAM_MONTH]

        return lunarCache.get_month(month, year)

    async def handle_get_year(call: ServiceCall):
        # clsLogger.log("services.py","async_setup_services","handle_get_year called")
        year = call.data[PARAM_YEAR]

        result = lunarCache.get_year(
            year,
        )

        return result
    
    async def handle_cleanup(call: ServiceCall):
        # clsLogger.log("services.py","async_setup_services","handle_cleanup called")
        lunarCache.cleanup(0)

    
    async def handle_good_hours(call: ServiceCall):
        # clsLogger.log("services.py","async_setup_services","handle_good_hour called")
        day = call.data[PARAM_DAY]
        month = call.data[PARAM_MONTH]
        year = call.data[PARAM_YEAR]

        result = lunarCache.get_current_hour_info(
            day,
            month,
            year,
        )

        return result
    
    async def handle_good_hours_today(call: ServiceCall):
        # clsLogger.log("services.py","async_setup_services","handle_good_hour_today called")
        result = lunarCache.get_current_hour_info_today()

        return result

    hass.services.async_register(
        DOMAIN,
        SERVICE_TODAY,
        handle_today,
        supports_response=SupportsResponse.ONLY,
    )

    hass.services.async_register(
        DOMAIN,
        SERVICE_GET_DAY,
        handle_get_day,
        schema=GET_DAY_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )

    hass.services.async_register(
        DOMAIN,
        SERVICE_GET_MONTH,
        handle_get_month,
        schema=GET_MONTH_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )

    hass.services.async_register(
        DOMAIN,
        SERVICE_GET_YEAR,
        handle_get_year,
        schema=GET_YEAR_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )

    hass.services.async_register(
        DOMAIN,
        SERVICE_CLEANUP,
        handle_cleanup,
        schema=GET_YEAR_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )

    hass.services.async_register(
        DOMAIN,
        SERVICE_GOOD_HOURS,
        handle_good_hours,
        schema=GET_DAY_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )

    hass.services.async_register(
        DOMAIN,
        SERVICE_GOOD_HOURS_TODAY,
        handle_good_hours_today,
        supports_response=SupportsResponse.ONLY,
    )

async def async_remove_services(hass: HomeAssistant, entry: ConfigEntry) -> None:
    clsLogger = hass.data[DOMAIN][entry.entry_id]["logger"]
    clsLogger.log("services.py","async_remove_services","Remove services called")

    if hass.services.has_service(DOMAIN, SERVICE_TODAY):
        hass.services.async_remove(DOMAIN, SERVICE_TODAY)
    if hass.services.has_service(DOMAIN, SERVICE_GET_DAY):
        hass.services.async_remove(DOMAIN, SERVICE_GET_DAY)
    if hass.services.has_service(DOMAIN, SERVICE_GET_MONTH):
        hass.services.async_remove(DOMAIN, SERVICE_GET_MONTH)
    if hass.services.has_service(DOMAIN, SERVICE_GET_YEAR):
        hass.services.async_remove(DOMAIN, SERVICE_GET_YEAR)
    if hass.services.has_service(DOMAIN, SERVICE_CLEANUP):
        hass.services.async_remove(DOMAIN, SERVICE_CLEANUP)
    if hass.services.has_service(DOMAIN, SERVICE_GOOD_HOURS):
        hass.services.async_remove(DOMAIN, SERVICE_GOOD_HOURS)
    if hass.services.has_service(DOMAIN, SERVICE_GOOD_HOURS_TODAY):
        hass.services.async_remove(DOMAIN, SERVICE_GOOD_HOURS_TODAY)