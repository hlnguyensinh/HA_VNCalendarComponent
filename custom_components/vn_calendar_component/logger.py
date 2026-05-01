
import logging
from datetime import datetime

_LOGGER = logging.getLogger(__name__)


class Logger:

    def log(self, main: str, sector: str, message: object) -> None:
        now = datetime.now()
        _LOGGER.warning("%s - [%s][%s]: %s", now.strftime("%Y-%m-%d %H:%M:%S"), main, sector, message,)