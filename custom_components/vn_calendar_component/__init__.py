from datetime import datetime
from pathlib import Path
from aiohttp import web

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.storage import Store
from homeassistant.helpers import issue_registry as ir

from .vnlunarcache import VNLunarCache
from .logger import Logger
from .services import async_setup_services, async_remove_services

from .const import DOMAIN, VERSION

PLATFORMS = ["sensor", "binary_sensor"]


ISSUE_RESTART = "restart_required_after_update"
STORAGE_VERSION = 1
STORAGE_KEY = f"{DOMAIN}_version"

async def detect_version_update(hass):
    """Detect integration version changes and warn user to restart HA."""

    store = Store(hass, STORAGE_VERSION, STORAGE_KEY)

    data = await store.async_load() or {}

    old_version = data.get("version")

    # First install -> just save version
    if old_version is None:
        await store.async_save({
            "version": VERSION,
            "pending_restart": False,
        })
        return

    # Version changed -> create warning
    if old_version != VERSION:

        ir.async_create_issue(
            hass,
            DOMAIN,
            ISSUE_RESTART,
            is_fixable=False,
            severity=ir.IssueSeverity.WARNING,
            translation_key=ISSUE_RESTART,
        )

        # Save new version
        await store.async_save({
            "version": VERSION,
            "pending_restart": True,
        })

    if data.get("pending_restart"):

        ir.async_delete_issue(
            hass,
            DOMAIN,
            ISSUE_RESTART,
        )

        await store.async_save({
            "version": VERSION,
            "pending_restart": False,
        })


""" 
from homeassistant.components.http import HomeAssistantView
from homeassistant.components.frontend import add_extra_js_url

URL_PATH = "/vn_calendar_component"
FRONTEND_FILE = "vn_lunar_calendar.js"

def register_frontend(hass):
    frontend_path = Path(__file__).parent / "frontend"
    js_file = frontend_path / FRONTEND_FILE

    class VNLunarJSView(HomeAssistantView):
        url = f"{URL_PATH}/{FRONTEND_FILE}"
        name = FRONTEND_FILE
        requires_auth = False

        async def get(self, request):
            return web.FileResponse(js_file)

    hass.http.register_view(VNLunarJSView())

    add_extra_js_url(
        hass,
        f"{URL_PATH}/{FRONTEND_FILE}?v={VERSION}"
    )
 """

async def register_services(hass, entry):
    now = datetime.now()

    lunarCache = VNLunarCache()
    lunarCache.preload([now.year - 1, now.year, now.year + 1])

    clsLogger = Logger()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "cache": lunarCache,
        "logger": clsLogger,
    }

    await async_setup_services(hass, entry)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    clsLogger.log("__init__.py", "async_setup_entry", "Setup services done.")


async def async_setup(hass: HomeAssistant, config: dict):
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    # register_frontend(hass)

    await register_services(hass, entry)

    await detect_version_update(hass)
    
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    await async_remove_services(hass, entry)

    hass.data[DOMAIN].pop(entry.entry_id)

    return True
