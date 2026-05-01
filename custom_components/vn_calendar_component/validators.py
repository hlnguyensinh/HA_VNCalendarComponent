from datetime import date
import voluptuous as vol

from .const import PARAM_DAY, PARAM_MONTH, PARAM_YEAR

MIN_YEAR = 1900
MAX_YEAR = 2199

def validate_date(value):
    day = value[PARAM_DAY]
    month = value[PARAM_MONTH]
    year = value[PARAM_YEAR]

    try:
        date(year, month, day)
    except ValueError as err:
        raise vol.Invalid(str(err))

    return value

GET_DAY_SCHEMA = vol.All(
    vol.Schema(
        {
            vol.Required(PARAM_DAY): vol.All(
                vol.Coerce(int),
                vol.Range(min=1, max=31),
            ),
            vol.Required(PARAM_MONTH): vol.All(
                vol.Coerce(int),
                vol.Range(min=1, max=12),
            ),
            vol.Required(PARAM_YEAR): vol.All(
                vol.Coerce(int),
                vol.Range(min=MIN_YEAR, max=MAX_YEAR),
            ),
        }
    ),
    validate_date,
)

GET_MONTH_SCHEMA = vol.Schema(
    {
        vol.Required(PARAM_MONTH): vol.All(
            vol.Coerce(int),
            vol.Range(min=1, max=12),
        ),
        vol.Required(PARAM_YEAR): vol.All(
            vol.Coerce(int),
            vol.Range(min=MIN_YEAR, max=MAX_YEAR),
        ),
    },
)

GET_YEAR_SCHEMA = vol.Schema(
    {
        vol.Required(PARAM_YEAR): vol.All(
            vol.Coerce(int),
            vol.Range(min=MIN_YEAR, max=MAX_YEAR),
        ),
    }
)